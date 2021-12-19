import random

#password must have at least one special character

numPasswords = int(input('How many passwords should I generate?: '))
numCharacters = int(input('How long should each password be?: '))

num_upper = 0
num_lower = 0
num_digits = 0
num_per_element = 0
num_per_element = int(num_per_element)

if((numCharacters - 1) % 3 == 0):
    num_per_element = (numCharacters - 1) // 3
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
    
    randomSpecial = chr(random.randint(33, 47))
    password_list.append(randomSpecial)

    for i in password_list:
        password += i
    
    print(password)