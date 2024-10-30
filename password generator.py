import random, string

def generator(password):
    #Append random characters for the length subtracted by the number of specific characters
    num = 0
    while num < (int(length) - len(chars)):
        password.append(char_list[random.randint(0, len(char_list) - 1)])
        num += 1
    
    #Insert the specific characters and join into list
    for i in chars:
        password.insert((random.randint(0, len(password) - 1)), i)
    "".join(password)
    return password

length = input("PASSWORD GENERATOR:\n\n\nInsert the length you would like your password to be: ")
chars = input("\nInput any characters you would like to be in it (seperate by comma): ")
chars = chars.split(",")
password = []
char_list = list(string.printable)

#Remove potential space from any character
num = 0
for i in chars:
    chars[num] = i.strip(" ")
    num += 1

print(generator(password))