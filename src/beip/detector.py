#
#
#

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
