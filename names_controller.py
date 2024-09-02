import sys
import os 

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from base_controller import BaseController

import mysql.connector

from mysql.connector import cursor

import alive_progress

class NamesController(BaseController):
    """
    Class that handles the CRUD between the DB and main file

    Class Variables
    ---------------
    sucess_insertion
        string containing sucessfull insertion on database
    error_insertion
        string containing unsucessfull insertion on database

    Methods
    -------
    insert_first_name(name, gender, nationality)
        Insert first name on database
    insert_last_name(name, nationality)
        Insert last name on database
    select_first_name(name, gender, nationality)
        Select for a specific first name on database         
    select_first_names()
        Select all first names on database        
    select_first_names_by_gender(gender)
        Select all first names on database by gender
    select_first_names_by_nationality(nationality)
        Select all first names on database by nationality
    select_first_names_by_gender_and_nationality(gender, nationality)
        Select all first names on database by gender AND nationality
    select_last_name(name, nationality)
        Select for a specific last name on database         
    select_last_names()
        Select all last names on database
    select_last_names_by_nationality(nationality)
        Select all last names on database by nationality
    select_full_name_by_nationality(nationality)
        Select a random full name by nationality
    """
    
    sucess_insertion = "Name inserted sucessfully on database!"
    error_insertion = "Name already on database!"

    @classmethod
    def insert_first_name(cls, name: str, gender: str, nationality: str) -> None:
        """Insert a first name into the database

        Parameters
        ----------
        name : str
            A string with more or equal then 3 characters and less or equal then 200 with no numbers on it
        gender : str
            One character that can be 'M', 'F' or 'N'

        Raises
        ------
        Exception : If the same name, gender & nationality is already is database
        
        Returns
        -------
        None : None
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()
        
        try:
            cursor.execute(cls.get_query('insert','insert_first_name'), [name, gender, nationality])
            print(cls.sucess_insertion)
        except:
            print(cls.error_insertion)

        conn.commit()
        conn.close()

        return None

    @classmethod
    def insert_first_names(cls, insert_point: str, file_insertion: any) -> None:
        """Insert first names on the databse

        Parameters
        ----------
        insert_point : str
            Available formats: `file` or `list`
        file_insertion : any
            A string with the path for the file if insert_point is `file` or
            a two dimentional list if insert_point is `list`
        
        Raises
        ------
        NameError : If the value doesn't match the insert_point

        Returns
        -------
        None
        """

        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        query = cls.get_query('insert','insert_first_name')

        if insert_point == 'file':
            cls.insert_first_names_by_csv(file_insertion, query, cursor)
        elif insert_point == 'list':
            cls.insert_first_names_by_list(file_insertion, query, cursor)
        else:
            raise NameError("Name doesn't match insert_point")

        conn.commit()
        conn.close()

        return None

    @classmethod
    def insert_first_names_by_list(cls, list_file: list,  query: str, mysql_cursor: cursor) -> None:
        """Execute a list of first names to mysql database

        Parameters
        ----------
        list_file : list
            A list of last names ex.: [name, gender, nationality]
        query : str
            A isnertion query
        mysql_cursor : cursor
            A mysql database cursor

        Returns
        -------
        None 
        """
        with alive_progress.alive_bar(len(list_file)) as bar:
            for f in list_file:
                name, gender, nationality = f[0], f[1], f[2]
                data = [name, gender, nationality]
                
                try:
                    mysql_cursor.execute(query, data)
                    print(cls.sucess_insertion)
                except:
                    print(cls.error_insertion)
                
                bar()

        return None

    @classmethod
    def insert_first_names_by_csv(cls, file_path: str, query: str, mysql_cursor: cursor) -> None:
        """Execute a list file of first names to mysql database
        
        Parameters
        ----------
        file_path : str
            A path to a csv file 
        query : str
            A insertion query
        mysql_cursor : cursor
            A mysql database cursor
        
        Returns
        -------
        None
        """
        
        with open(file_path, 'r') as file:
            file = file.readlines()

            with alive_progress.alive_bar(len(file)) as bar:
                for f in file:
                    f = f.split(',')
                    name, gender, nationality = f[0], f[1], f[2].replace('\n', '')
                    
                    data = [name, gender, nationality]

                    try:
                        mysql_cursor.execute(query, data)
                        print(cls.sucess_insertion)
                    except:
                        print(cls.error_insertion)            

                    bar()

        return None

    @classmethod
    def insert_last_name(cls, name: str, nationality: str) -> None:
        """
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()
        
        try:
            cursor.execute(cls.get_query('insert','insert_last_name'), [name, nationality])
            print(cls.sucess_insertion)
        except:
            print(cls.error_insertion)

        conn.commit()
        conn.close()

        return None

    @classmethod
    def insert_last_names(cls, insert_point: str, file_insertion: any) -> None:
        """Insert last names on the databse

        Parameters
        ----------
        insert_point : str
            Available formats: `file` or `list`
        file_insertion : any
            A string with the path for the file if insert_point is `file` or
            a two dimentional list if insert_point is `list`
        
        Raises
        ------
        NameError : If the value doesn't match the insert_point

        Returns
        -------
        None
        """
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        query = cls.get_query('insert', 'insert_last_name')

        if insert_point == 'file':
            cls.insert_last_names_by_csv(file_insertion, query, cursor)
        elif insert_point == 'list':
            cls.insert_last_names_by_list(file_insertion, query, cursor)
        else:
            raise NameError("Name doesn't match insert_point")

        conn.commit()
        conn.close()

        return None
    
    @classmethod
    def insert_last_names_by_list(cls, list_file: list,  query: str, mysql_cursor: cursor) -> None:
        """Execute a list of last names to mysql database

        Parameters
        ----------
        list_file : list
            A list of last names ex.: [name, nationality]
        query : str
            A isnertion query
        mysql_cursor : cursor
            A mysql database cursor

        Returns
        -------
        None 
        """
        
        with alive_progress.alive_bar(len(list_file)) as bar:
            for f in list_file:
                name, nationality = f[0], f[-1]
                data = [ name, nationality ]
                
                try:
                    mysql_cursor.execute(query, data)
                    print(cls.sucess_insertion)
                except:
                    print(cls.error_insertion)
                
                bar()

        return None

    @classmethod
    def insert_last_names_by_csv(cls, file_path: str, query: str, mysql_cursor: cursor) -> None:
        """Execute a list file of last names to mysql database
        
        Parameters
        ----------
        file_path : str
            A path to a csv file 
        query : str
            A insertion query
        mysql_cursor : cursor
            A mysql database cursor
        
        Returns
        -------
        None
        """
        
        with open(file_path, 'r') as file:
            file = file.readlines()

            with alive_progress.alive_bar(len(file)) as bar:
                for f in file:
                    f = f.split(',')
                    name, nationality = f[0], f[-1].replace('\n', '')

                    data = [name, nationality]

                    try:
                        mysql_cursor.execute(query, data)
                        print(cls.sucess_insertion)                        
                    except:
                        print(cls.error_insertion)
                    
                    bar()

        return None

    # Select First Names Methods

    @classmethod
    def select_first_name(cls, name: str, gender: str, nationality) -> list[tuple]:
        """Select a first name that matches by value, gender and nationality

        Parameters
        ----------
        name : str
            A value for a first name
        gender : str
            A char string: M, F or N
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
    def select_first_names(cls) -> list[tuple]:
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
    def select_first_name_by_gender(cls, gender: str) -> list[tuple]:
                
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_name_by_gender'), [gender])
        res = cursor.fetchall()

        conn.close()

        return res
    
    @classmethod
    def select_first_name_by_nationality(cls, nationality: str) -> list[tuple]:
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_name_by_nationality'), [nationality])
        res = cursor.fetchall()

        conn.close()

        return res

    @classmethod
    def select_first_name_by_gender_and_nationality(cls, gender: str, nationality: str) -> list[tuple]:
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_first_name_by_gender_and_nationality'), [gender, nationality])
        res = cursor.fetchall()

        conn.close()

        return res        

    # Select Last Names methods
    
    @classmethod
    def select_last_name(cls, name: str, nationality: str) -> list[tuple]:
        """
        """
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_last_name'), [name, nationality])
        res = cursor.fetchall()

        conn.close()

        return res


    @classmethod
    def select_last_names(cls) -> list[tuple]:
        """
        """
                
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select','select_last_names'))
        res = cursor.fetchall()

        conn.close()

        return res


    @classmethod
    def select_last_names_by_nationality(cls, nationality: str) -> list[tuple]:
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

    @classmethod
    def select_random_full_name_by_nationality_and_gender(cls, gender:str, nationality: str) -> list[tuple]:
        """"""
        
        conn = mysql.connector.connect(**cls.database_config)
        cursor = conn.cursor()

        cursor.execute(cls.get_query('select', 'full_name_by_nationality_and_gender'), [nationality, nationality, gender])
        res = cursor.fetchall()

        conn.close()
        return res
