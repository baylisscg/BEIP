#
#
#

class Location:
    
    def __init__(self,northing,easting):
       self.__northing = northing
       self.__easting = easting
    
    def __str__(self):
        return "{0:>9},{1:>9}".format(self.__northing,self.__easting)

    @staticmethod
    def from_geojson(json):
      objtype = json["type"]
      x = float(json["coordinates"][0])
      y = float(json["coordinates"][1])
      return Location(x,y)

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
        

class Detector:
    """A device capable of measuring a single property"""

    def __init__(self,name,quantity,sensor=None):
        self.name = name
        self.quantity = quantity
        if sensor is not None: self.sensor = sensor

    def __str__(self):
        "{} {}".format(self.name,self.quantity)

      

    @staticmethod
    def from_json(json,sensor):
        name = json["name"]
        quantity = None
        if "type" in json: quantity = json["type"]

        if quantity is None: quantity = sensor.type

        return Detector(name,quantity,sensor) 
