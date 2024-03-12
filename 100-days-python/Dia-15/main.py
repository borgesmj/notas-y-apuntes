exit = ""
while exit != 'yes':
    print('What animal do you want? ')
    animal = input(" > ").lower()
    if animal == "cow":
        print('The cow says moo')
        print('do you want to exit?')
        exit = input('yes or no > ')
    elif animal == "cat":
        print('the cat says meaow')
        print('do you want to exit?')
        exit = input('yes or no > ')
    elif animal == 'dog':
        print('the dog says woof')
        print('exit?')
        exit = input('yes or no > ')
    else:
        print("sorry, i don't know that animal")
        print('do yu want to exit?')
        exit = input('yes or no > ')
else:
    print("bye")