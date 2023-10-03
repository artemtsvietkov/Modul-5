my_names = []

# my_names = ["Artem", "Dmytro", "Dan"]

# print(len(my_names))

# print(my_names)

# my_names[1] = "Dima"

# print(my_names[1])

# new_name = input("Skriv in ett nytt namn ")

# my_names.append(new_name)

# print(my_names)

# print(len(my_names))


# janej_name = input("Vill du ta bort ett namn? Ja/Nej ")
# if janej_name == 'Ja':
#     delete_name = input(f"Vilket namn vill du ta bort? {my_names}")
#     if delete_name in my_names:
#             my_names.pop(my_names.index(delete_name))
#             print(f"{delete_name} är borta")
#             print(my_names)
#     elif delete_name not in my_names:
#             print("no name")
# elif janej_name == 'Nej':
#     print("Okej :(")

# while True:
#     add_name = input("Lägg till ett namn i lista: ")
#     my_names.append(add_name)
#     print(my_names)

my_names = []
while True:  
        user_answer = input("Add/Remove. Om du inte vill lägga till eller ta bort ett namn - skriv *stop*: ")
        if user_answer == "stop":
            break

        elif user_answer == "Add":
             added_name = input("Lägg till ett namn: ")
             my_names.append(added_name)
             for name in my_names:
                print(name)
             
        elif user_answer == "Remove":  
            if len(my_names) == 0:
                print("Listan är tom!")
            else:
                 for name in my_names:
                    print(name)
            user_remove_answer = input("Vilket namn du vill ta bort? ")
            if user_remove_answer not in my_names:
                print("Namn finns inte i listan.")
            else:
                my_names.pop(my_names.index(user_remove_answer))
                print("Namnet har tagits bort!")
                for name in my_names:
                    print(name)

# my_fav_car = {"weight" : "4.5t", "lenght" : "2.5m", "number_of_seats" : "4"}

# print(my_fav_car["number_of_seats"])

    