from argparse import ArgumentParser
import re
import sys
# replace this comment with your implementation of the Address class
# and read_addresses() function. Uncomment the __repr__() method below
# and include it in your Address class.


class Address:
      """ The Address class use regular expressions to parse street addresses from a text file. 
            Attributes: address(str),house_number,street,city, state zip
            The __init__ methode take a single line of text as an argument and set the attributes to
             Address class.
             Arg:
                 self 
        """
      def __init__(self):
        self.expr = r'''(?xm)
                    ^ #match the beginning of line
                    (?P<house_num>\S+) # house number
                    \s
                    (?P<street_name>[^,]+) # street name
                    ,\s
                    (?P<city>\w+(?:\s\w+([^A-Z]{,2}))?(?:\s\w+\s\w+([^A-Z]{,2}))?)\s # City name
                    (?P<state>\w+) #state name 
                    \s
                    (?P<zip>\d+) # zip code 
                    $ # match end of line
                    '''
    
      def __repr__(self):
         """Return a formal representation of the Address object."""
         return (
            f"address:      {self.address}\n"
            f"house number: {self.house_number}\n"
            f"street:       {self.street}\n"
            f"city:         {self.city}\n"
            f"state:        {self.state}\n"
            f"zip:          {self.zip}"
            
        )


def read_addresses(filepath):
    ''' this function convery each line to an address object and return a list
        Args: filepath contain one address per line 
        and 
        returns:
                list that contain one instance of Class Address'''
    with open(filepath,'r', encoding ='utf-8') as f:
        addy = f.read()
        loc = [Address(filepath) for addy in f ]
        return loc
        



def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        print(f"{address!r}\n")
