# Module dedicated to create validation decorators
#
#

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
        name, nationality = args[1], args[-1]

        name_val = 3 <= len(name) <= 200 and name.isalpha()
        nationality_val = 3 <= len(nationality) <= 200 and nationality.isalpha()
        
        if name_val and nationality_val:
            return func(*args, **kwargs)
        
        raise Exception('Name or Nationality string is not set correctly. Please verify')

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