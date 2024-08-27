import os
import pathlib

import json

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()

class BaseController:
    """
    Base class that contains every property and functions used in other controllers

    Class Variables
    ---------------
    database_config
        dict containing database configuration 

    Methods
    -------
    get_query(db_method, file_name)
        return a str with a sql query
    """

    with open(os.path.join(CURRENT_PATH, 'config.json')) as f:
        database_config = json.load(f)
    
    @classmethod
    def get_query(cls, db_method: str, file_name: str) -> str:
        """Get one query on queries/select

        Parameters
        ----------
        db_method : str
            Name of the action that the user wanna made ex: select | insert
        file_name : str
            Name of the file inside the path without the file extension

        Raises
        ------
        FileNotFoundError : If the file doesnt exists        
        
        Returns
        -------
        str : A string with sql query
        """

        file_path = os.path.join(
            CURRENT_PATH,
            'queries',
            db_method,
            '{}.sql'.format(file_name)
        )
        
        try:
            with open(file_path, 'r') as file:
                return ''.join(file.readlines())
        except: 
            raise FileNotFoundError("File {} doesn't exists".format(file_path))
