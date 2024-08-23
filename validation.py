# Module dedicated to create validation decorators
#
#

def alpha_string(string: str, logical_response: bool) -> bool:
    """Checks if the string is all alphabetic

    Parameters
    ----------
    string : str
        A string value
    logical_response : bool
        Another boolean response for the previous validation

    Returns
    -------
    bool : using a 'and' operator between this and the previous validation
    """

    if ' ' in string:
        return logical_response and string.replace(' ', '').isalpha()
    return logical_response and string.isalpha()
    
def accurate_len_string(string: str, min_str: int, max_str: int) -> bool:
    """Check if the strings is between the length intervall

    Parameters
    ----------
    string : str
        String value
    min_str : int
        Minimum value for the string
    max_str : int
        Maximum value for the string
    
    Returns
    -------
    bool : based on the string length
    """

    return min_str <= len(string) <= max_str

def validates_name_nationality(func) -> bool:
    """Validates if the name and nationality strings value is: 
    all alphabetic and his length is between 3 and 200 letters
    
    Parameters
    ----------
    func : function
        An insert controller method

    Returns
    -------
    func : Exec function if validation is True
    """
    
    def inner1(*args, **kwargs):
        name, nationality = args[1], args[3]
    
        # name_val = accurate_len_string(name, 1, 200)
        nationality_val = accurate_len_string(nationality, 3, 200)
        
        name_val = alpha_string(name, name_val)
        nationality_val = alpha_string(nationality, nationality_val)

        if name_val and nationality_val:
            return func(*args, **kwargs)
        
        raise Exception(f'Error during name and nationalionality validation.\
                        Name validation: {name_val} and Nationality validation: {nationality_val}')

    return inner1

def validates_gender(func) -> bool:
    """Validates if the gender string value is: 
    is one length longer and belongs to 'M', 'N' or 'F'
    
    Parameters
    ----------
    func : function
        An insert controller method

    Returns
    -------
    func : Exec function if validation is True
    """

    def inner1(*args, **kwargs):

        value = args[2]

        options = ['M', 'F', 'N']
        if value.islower() : value = value.upper()

        if len(value) == 1 and value in options:
            return func(*args, *kwargs)
        
        raise Exception("Gender string is not set correctly. Please verify")
    
    return inner1