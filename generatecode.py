import random
import PasswordCheck as p

lalpha=[chr(x) for x in range(97,122)]
num=[f'{i}' for i  in range(10)]
abond_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", ":", ";", "<", ">", ".", "/",
                  "?",
                  "'", "[", "]", "{", "}", "|", "\\"]
#this function for generate code for mail login
def generate_code():
    data = lalpha+num
    code = random.choices(data,k=8)
    return ''.join(code)

#this function for create a pin for user and save this pin in db for future use
def generate_pin():
    return ''.join(random.choices(num,k=6))

#this function only generate the strong password there is no need to check the password strength
#because the generated password is always strong by mixing of characters
def generate_password():
    alpha = random.choices(lalpha,k=4)
    number = random.choices(num,k=3)
    charcters = random.choices(abond_char,k=1)
    shufle = number+charcters
    random.shuffle(shufle)
    password = alpha+shufle
    return ''.join(password)
