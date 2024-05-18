import random
#this function for generate code for mail login
def generate_code():
    ualpha=[chr(x) for x in range(65,91)]
    lalpha=[chr(x) for x in range(97,122)]
    num=[f'{i}' for i  in range(10)]
    data = ualpha+lalpha+num
    code = random.choices(data,k=8)
    return ''.join(code)

#this function for create a pin for user and save this pin in db for future use
def generate_pin():
    num=[x for x in range(10)]
    return random.choices(num,k=6)
