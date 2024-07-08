aeiou = ['a', 'e', 'i', 'o', 'u']
def check1(password):
    check_aeiou = 0
    for spell in aeiou:
        check_aeiou += password.count(spell)
    if check_aeiou == 0:
        return False
    else:
        return True

def check2(password):
    if len(password) < 3:
        return True
    for i in range(2, len(password)):
        if (password[i-2] in aeiou) and (password[i-1] in aeiou) and (password[i] in aeiou):
            return False
        if (password[i-2] not in aeiou) and (password[i-1] not in aeiou) and (password[i] not in aeiou):
            return False
    return True

def check3(password):
    if len(password) < 2:
        return True
    for i in range(1, len(password)):
        if password[i-1] == password[i]:
            if (password[i] == 'e') or (password[i] == 'o'):
                continue
            else:
                return False
    return True

while True:
    password = input()
    if password == 'end':
        break
    else:
        if (check1(password) == True) and (check2(password) == True) and (check3(password) == True):
            print(f'<{password}> is acceptable.')
        else:
            print(f'<{password}> is not acceptable.')
