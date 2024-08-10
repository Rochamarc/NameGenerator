import sys
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from base_controller import BaseController

import mysql.connector


class NamesController(BaseController):
    # TODO
    # update this summary
    """
    Class that handle tournament_name database

    Methods
    -------
    first_name_match(name: str, gender: str, nationality: str)
        Try to find a match for a specific first name
    last_name_match(name: str, gender: str, nationality: str)
        Try to find a match for a specific last name
    insert_first_name(name: str, gender: str, nationality: str)
        Insert first name on database
    insert_last_name(name: str, nationality: str)
        Insert last name on database
    select_first_name(name: str, gender: str, nationality: str)
        Select for a specific first name on database         
    select_first_names()
        Select all first names on database        
    select_first_names_by_gender(gender: str)
        Select all first names on database by gender
    select_first_names_by_nationality(nationality: str)
        Select all first names on database by nationality
    select_first_names_by_gender_and_nationality(gender: str, nationality: str)
        Select all first names on database by gender AND nationality
    select_last_name(name: str, nationality: str)
        Select for a specific last name on database         
    select_last_names()
        Select all last names on database
    select_last_names_by_nationality(nationality: str)
        Select all last names on database by nationality
    select_full_name_by_nationality(nationality: str)
        Select a random full name by nationality
    """
    
    @classmethod
    def first_name_match(cls, name: str, gender: str, nationality: str) -> bool:
        """Try to find a match for first name, gender & nationality

        Returns
        -------
        bool : based on the match being true
        """

        match = cls.select_first_name(name, gender, nationality)

        return len(match) > 0

    @classmethod
    def last_name_match(cls, name: str, nationality: str) -> bool:
        """Try to find a match for last name & gender

        Returns
        -------
        bool : based on the match being true
        """

        match = cls.select_last_name(name, nationality)

        return len(match) > 0

    @classmethod
    def insert_first_name(cls, name: str, gender: str, nationality: str) -> None:
        """
        """
        
        # Verify if the name is on the database
        name_match = cls.first_name_match(name, gender, nationality)
        
        if name_match:
            print("Name already in the database!")
            return None 
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()
        
        cursor.execute(cls.get_query('insert','insert_first_name'), [name, gender, nationality])
            
        conn.commit()
        conn.close()

        print("Name inserted sucessfully!")
        return None

    @classmethod
    def insert_last_name(cls, name: str, nationality: str) -> None:
        """
        """
        
        # Verify if the name is on the database
        name_match = cls.last_name_match(name, nationality)
        
        if name_match:
            print("Name already in the database!")
            return None 
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()
        
        cursor.execute(cls.get_query('insert','insert_last_name'), [name, nationality])
            
        conn.commit()
        conn.close()

        print("Name inserted sucessfully!")
        return None

    # Select First Names Methods

    @classmethod
    def select_first_name(cls, name: str, gender: str, nationality) -> list:
        """Select a first name that matches by value, gender and nationality

        Parameters
        ----------
        name : str
            A value for a first name
        gender : str
            A char string containing M, F or N
        nationality : str
            A country name
        Returns
        -------
        list : with name info: name, gender, nationality
        """
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_name'), [name, gender, nationality])
        res = cursor.fetchall()

        conn.close()

        return res

    @classmethod
    def select_first_names(cls) -> list:
        """Select first names based on nationality
        
        Parameters
        ----------
        nationality : str
            Str used to select the nationality of first names
        
        Returns
        -------
        list : with list containing first names info: id, value, gender, nationality 
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_names'))
        res = cursor.fetchall()

        conn.close()

        return res

    @classmethod
    def select_first_name_by_gender(cls, gender: str) -> list:
                
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_name_by_gender'), [gender])
        res = cursor.fetchall()

        conn.close()

        return res
    
    @classmethod
    def select_first_name_by_nationality(cls, nationality: str) -> list:
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_name_by_nationality'), [nationality])
        res = cursor.fetchall()

        conn.close()

        return res

    @classmethod
    def select_first_name_by_gender_and_nationality(cls, gender: str, nationality: str) -> list:
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_name_by_gender_and_nationality'), [gender, nationality])
        res = cursor.fetchall()

        conn.close()

        return res        

    # Select Last Names methods
    
    @classmethod
    def select_last_name(cls, name: str, nationality: str) -> list:
        """
        """
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_last_name'), [name, nationality])
        res = cursor.fetchall()

        conn.close()

        return res


    @classmethod
    def select_last_names(cls) -> list:
        """
        """
                
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_last_names'))
        res = cursor.fetchall()

        conn.close()

        return res


    @classmethod
    def select_last_names_by_nationality(cls, nationality: str) -> list:
        """Select last names from tournament_name.last_names
        
        Parameters
        ----------
        nationality : str
            Str used to select the nationality of last names
        
        Returns
        -------
            A list of lists with last names 
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_last_names_by_nationality'), [nationality])
        res = cursor.fetchall()

        conn.close()

        return res

if __name__ == "__main__":
    ...