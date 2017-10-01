class pycent:
    def __init__(self):
        pass

    def percent_of(self, percent, whole):
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

    def percentage(self, part, whole):
        """Calculates the percentage of a number, given a part and a whole
        ie: 5 is what percent of 20 --> 25

        Args:
            part (float): The part of a number
            whole (float): The whole of a number

        Returns:
            float: The percentage

        Examples:
        >>> percentage(10, 25)
        40.0
        >>> percentage(5, 20)
        25.0

        """
        if whole == 0:
            raise ZeroDivisionError

        return 100 * float(part)/float(whole)

