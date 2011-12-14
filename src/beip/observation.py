#
#
#

from datetime import datetime

class Observation:

    __slots__ = ["timestamp","value"]

    def __init__(self,value,timestamp):
        self.timestamp = timestamp
        self.value = value

    def __str__(self):
        return "{}-{}".format(self.timestamp,self.value)
        
