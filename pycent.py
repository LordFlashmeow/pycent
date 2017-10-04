from typing import Union

FloatIn = Union[int, float, str]

class pycent:
    def __init__(self):
        pass

    def percent_of(self, percent: FloatIn, whole: FloatIn):
        """Calculates the value of a percent of a number
        ie: 5% of 20 is what --> 1
        
        Args:
            percent (float): The percent of a number
            whole (float): The whole of the number
            
        Returns:
            float: The value
            
        Example:
        >>> percent_of(25, 100)
        25.0
        >>> percent_of(5, 20)
        1.0
        
        """
        return (percent * whole) / 100

    def percentage(self, part: FloatIn, whole: FloatIn, resolution: int=2):
        """Calculates the percentage of a number, given a part and a whole
        ie: 5 is what percent of 20 --> 25

        Args:
            part (float): The part of a number
            whole (float): The whole of a number
			resolution (integer): How many decimal points you want (Defaults to 2)

        Returns:
            float: The percentage

        Examples:
        >>> percentage(10, 25)
        40.0
        >>> percentage(5, 19, 3)
        26.316

        """
        if whole == 0:
            raise ZeroDivisionError

        return round(100 * float(part)/float(whole), resolution)
