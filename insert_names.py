from names_controller import NamesController
from alive_progress import alive_bar

controller = NamesController()

def insert_names(file_path: str, name_pointer: str) -> int:
    """
    """

    failed = 0 

    with open(file_path, 'r') as file:
        file = file.readlines()
        
        with alive_bar(len(file)) as bar:
            for f in file:
                f = f.split(',')
                nationality = f.pop().strip('\n')

                try:
                    if name_pointer == 'first_names':
                        name, gender = f
                        controller.insert_first_name(name, gender, nationality)
                    else:
                        name = f[0]
                        controller.insert_last_name(name, nationality)
                except:
                    failed += 1
                bar()

    return failed

if __name__ == "__main__":
    print('INSERTING FIRST NAMES INTO DATABASE')
    a = insert_names('files/last_names.csv', 'last_names')
    print(a)