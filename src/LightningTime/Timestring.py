
class Timestring:

    """
    A class that represents a lightning timestring.
    """
    def __init__(self, timestring:str=None) -> None:
        self.timestring = timestring if timestring is not None else "0~0~0|0"
        try:
            self.bolts = self.timestring.split("~")[0]
            self.zaps = self.timestring.split("~")[1]
            self.sparks = self.timestring.split("~")[2].split("|")[0]
            self.charges = self.timestring.split("|")[1]
            if len(self.charges) > 1:
                raise IndexError
        except IndexError:
            raise ValueError("Invalid timestring.")
        
    def __str__(self) -> str:
        return self.timestring
    
    def get_parts(self):
        return (self.bolts, self.zaps, self.sparks, self.charges)