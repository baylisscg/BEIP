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

    def __init__(self,name,location=None):
        """
        """
        self.__name = name
        if location is not None : self.__location = location 

    def add_detector(self,detector):
        """
        """
        self.__detector.append(detector)

    def __str__(self):
        """
        """
        return "{0:>10}@{1:>10}".format(self.__name,self.__location)
        

class Detector:
    """A device capable of measuring a single property"""

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        "{} {}".format(self.)

    @staticmethod
    def from_json(json):
        name = json["name"]
        quantity = json["type"]
        return Detector(name,quantity) 
