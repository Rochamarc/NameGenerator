from names_controller import NamesController

contoller = NamesController()

equals = "="*50
welcome = "\tWelcome to Names Generator"
welcome_2 = "What task do you want to accomplish?"
welcome_3 = "\n*[1] - Insert a new first name\n\
*[2] - Insert a new last name\n\
*[3] - Select first name\n\
*[4] - Select last name\n\
*[5] - Select full name\n"

print(equals, welcome, equals, welcome_2, welcome_3, equals, sep='\n')

action = int(input(".: "))

if action == 1:
    while True:
        
        print(equals, "Insert First Name", equals, sep="\n")
        
        name = input("Type the name.: ")
        gender = input("Type the gender.:")
        nationality = input("TYpe the nationality.:")

        name_string = f"Name: {name}, Gender: {gender}, Nationality: {nationality}"

        print(equals, "NAME REVIEW", name_string, equals, sep='\n')
        cont = input("Enter to continue...")

        contoller.insert_first_name(name, gender, nationality)

        another = input("Insert another name? [y/n].: ")

        if another == 'n':
            print("Bye Bye!")
            break