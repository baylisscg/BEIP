#!/usr/bin/env python2.7
#
#

from __future__ import print_function, unicode_literals

import sys
import os.path
import logging
import multiprocessing
import json

sys.path[0] = ( os.path.join(os.getcwd(), "src") )

import collector
from collector.sensor import Sensor, Detector, Location

logger =  multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)

#
#
#
def load_sensors(file_path):

    sensors_out = []

    with open(file_path,'r') as f :
        sensors = json.load(f)
        logger.info("Sensors {}".format(len(sensors)))
        for json_sensor in sensors:
            location = Location.from_geojson(json_sensor['location'])
            name = json_sensor['name']    
            sensor = Sensor(name,location=location)
            for json_detector in json_sensor["detectors"]:
                sensor.add_detector(Detector.from_json(json_detector))
            sensors_out.append( sensor )
    return sensors_out
                         
#
#
#
def main():
    # Only grab inputs$
    targets = [] #glob.glob('/sys/class/hwmon/hwmon0/device/*_input')
    try:
        pool = Pool(len(targets))
        pool.map(sysfs_read,targets)
        pool.close()
        logger.debug('pool map complete')
    except KeyboardInterrupt:
        logger.error('got ^C while pool mapping, terminating the pool')
        pool.terminate()
        logger.debug('pool is terminated')
    except Exception, e:
        logger.error('got exception: %r, terminating the pool' % (e,))
        pool.terminate()
        logger.debug('pool is terminated')
    finally:
        logger.info('joining pool processes')
        pool.join()
        logger.info('join complete')

#
#
#
if __name__ == '__main__':
    logger.info("Starting up")
    
    try:
        sensors = load_sensors(os.path.join(os.getcwd(),"config","sensors.json"))
    except ValueError, e:
        logger.error(e)
    
    for sensor in sensors: logger.info(sensor)

    #main()
    logger.info("Closing down")
