# Controllers

## Base Controller

### Class Variables
---
* database_config : dict
    <p>Database configuration</p>

### Class Methods
---
* get_query : str
    <p>Select a query from the queries directory</p>

<!-- Start names controller part -->
## Names Controller    
    Inherits from the base controller

### Class Methods
---
* first_name_match(name: str, gender: str, nationality: str)
    <p>Try to find a match for a specific first name</p>
* last_name_match(name: str, gender: str, nationality: str)
    <p>Try to find a match for a specific last name</p>
* insert_first_name(name: str, gender: str, nationality: str)
    <p>Insert first name on database</p>
* insert_last_name(name: str, nationality: str)
    <p>Insert last name on database</p>
* select_first_name(name: str, gender: str, nationality: str)
    <p>Select for a specific first name on database</p>         
* select_first_names()
    <p>Select all first names on database</p>        
* select_first_names_by_gender(gender: str)
    <p>Select all first names on database by gender</p>
* select_first_names_by_nationality(nationality: str)
    <p>Select all first names on database by nationality</p>
* select_first_names_by_gender_and_nationality(gender: str, nationality: str)
    <p>Select all first names on database by gender AND nationality</p>
* select_last_name(name: str, nationality: str)
    <p>Select for a specific last name on database</p>         
* select_last_names()
    <p>Select all last names on database</p>
* select_last_names_by_nationality(nationality: str)
    <p>Select all last names on database by nationality</p>
* select_full_name_by_nationality(nationality: str)
    <p>Select a random full name by nationality</p>
    <p><b>NOT WORKING</b></p>