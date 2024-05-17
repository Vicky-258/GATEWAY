
def check_password(password):
    if len(password) < 8:
        return "lenerror"

    abond_char = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", ":", ";", "<", ">", ".", "/",
                  "?",
                  "'", "[", "]", "{", "}", "|", "\\"]

    cnt = 0

    for i in password:
        if i in abond_char:
            cnt += 1
        if cnt > 1:
            return "charerror"

    strong = False
    if len(password) >= 8:
        for i in password:
            if i.isupper():
                for i in password:
                    if i.islower():
                        for i in password:
                            if i.isnumeric():
                                for i in password:
                                    if not (i.isalpha() or i.isdigit()):
                                        strong = True
    if strong:
        return True
    else:
        return False
