from names_controller import NamesController
from alive_progress import alive_bar

controller = NamesController()

failed = 0

with open('files/first_names.csv', 'r') as file:
    file = file.readlines()

    print('INSERTING FIRST NAMES INTO DATABASE')
    with alive_bar(len(file)) as bar:
        for f in file:
            f = f.split(',')
            nationality = f.pop().strip('\n')
            name, gender = f

            try:
                controller.insert_first_name(name, gender, nationality)
            except:
                failed += 1
            bar()

print(failed)