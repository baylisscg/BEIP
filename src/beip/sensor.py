#
#
#

from beip.location import Location

class Sensor:
    """Models a single sensor"""

    def __init__(self,name,location=None,sensor_type=None):
        """
        """
        self.__name = name
        self.__detectors = {}
        self.__location = location
        self.__type = sensor_type

    def add_detector(self,detector):
        """
        """
        self.__detectors[detector.name] = detector

    def type(self):
        return self.__type
    

    def __str__(self):
        """
        """
        return "{0:>10}@{1:>10}\n{2}".format(self.__name,self.__location,self.__detectors)
