import random

#password must have at least one special character
numPasswords = 0
while numPasswords != -1:

    numPasswords = int(input('How many passwords should I generate? (enter -1 to quit): '))
    while(numPasswords < -1):
        numPasswords = int(input('Invalid number of passwords try again: '))
    if(numPasswords == -1):
        break

    numCharacters = int(input('How long should each password be? (enter a value above 5): '))
    while(numCharacters < 6):
        numCharacters = int(input('Length is too short try again: '))

    num_upper = 0
    num_lower = 0
    num_digits = 0
    num_per_element = 0
    num_per_element = int(num_per_element)
    special_characters = ['!', '#', '?', '-']

    if((numCharacters - 1) % 3 == 0):
        num_per_element = (numCharacters - 1) // 3
    elif((numCharacters - 1) % 3 == 2):
        num_per_element = (numCharacters - 1) // 3
        num_upper = 1
        num_lower = 1
    else:
        num_per_element = (numCharacters - 1) // 3
        num_upper = 1

    num_upper += num_per_element
    num_lower += num_per_element
    num_digits += num_per_element

    password_list = []
    password = ""

    for i in range(numPasswords):
        password = ""
        password_list = []

        for i in range(num_upper):
            password_list.append(chr(random.randint(65, 90)))

        for i in range(num_lower):
            password_list.append(chr(random.randint(97, 122)))

        for i in range(num_digits):
            password_list.append(chr(random.randint(48, 57)))
        
        if(numCharacters > 0):
            random_special = random.randint(0, len(special_characters) - 1)
            password_list.append(special_characters[random_special])

        for i in range(len(password_list)):
            randInt = random.randint(0, len(password_list) - 1)
            password += password_list[randInt]
            del password_list[randInt]
        
        print(password)