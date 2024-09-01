from names_controller import NamesController

from tests.names import last_names

last_names_path = 'tests/last_names.csv'

if __name__ == "__main__":
    NamesController().insert_last_names('list', last_names)
    NamesController().insert_last_names('file', last_names_path)