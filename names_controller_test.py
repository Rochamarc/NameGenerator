from names_controller import NamesController

from tests.names import last_names, first_names

last_names_path = 'tests/last_names.csv'
first_names_path = 'tests/first_names.csv'

if __name__ == "__main__":
    # Last Names
    print('Testing last names insertion by list')
    NamesController().insert_last_names('list', last_names)
    print('Testing last names insertion by file')
    NamesController().insert_last_names('file', last_names_path)

    # First names tests
    print('Testing first names insertion by list')
    NamesController().insert_first_names('list', first_names)
    print('Testing first names insertion by file')
    NamesController().insert_first_names('file', first_names_path)