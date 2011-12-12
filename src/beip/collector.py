#
#
#

import avro
import avro.datafile
import avro.schema
import avro.io

from time import time,sleep
import asyncore
import glob
import threading
from multiprocessing import Pool
import multiprocessing
import logging

import json

json_schema = '''{
  "namespace": "au.edu.unimelb.eresearch.beip",
  "name":"SensorReading",
  "type":"record",
  "doc":"A simple record for holding a result from a sensor",
  "fields":[{"name":"DateStamp","type":"long","doc":"Test"},
            {"name":"Name","type":"string"},
            {"name":"Value","type":"long"}]
}'''

SCHEMA = avro.schema.parse(json_schema)

#logger = multiprocessing.log_to_stderr()
#logger.setLevel(logging.INFO)

def sysfs_read(path):
    
    logger.info(path[:-6]+"_label")
    label = open(path[:-6]+"_label",'r').readline().strip()
    f = open(path,"r")
    logger.info("Opening {0}".format(path[:-6].rsplit('/')[-1]))
 
    datum_writer = avro.io.DatumWriter(SCHEMA)

    target = open(path[:-6].rsplit('/')[-1],'wb+')
    writer = avro.datafile.DataFileWriter(target,datum_writer, writers_schema = SCHEMA)
    try:
        while True:
            writer.append({"DateStamp":long(time()*100),
                           "Name":label,
                           "Value": int(f.readline().strip())})
            f.seek(0)
            sleep(0.5)
    except KeyboardInterrupt:
        raise KeyboardInterruptError()
    finally:
        f.close()
        writer.close()
        target.close()



    
