def check_legal(id):
    id=id.copy()
##Position check
    if not(    not id[0].isnumeric() and
            not id[1].isnumeric() and
            ''.join(id[2:9]).isnumeric()):
        return False

## modulo 11 check
    return check_digit_calculate(id)==int(id[8])

def check_digit_calculate(num):
    total = 0
    num = num.copy()
    for i in range(8):
        if num[i].isnumeric() == False:
            if num[i] == " ":
                num[i] = 36
            else:
                num[i] = ord(num[i])-55
        total += int(num[i]) * (9-i)
    return 11-total%11

def input_test(): #True = legal, False = illegal
    if len(known) !=9:
        return False
    for i in known[:2]:
        if not(i.isalpha() or i == ' '):
            return False
    for i in known[2:]:
        if not(i.isnumeric() or i == ' '):
            return False
    return True

def generate(id):
    id = id.copy()
    
    if id[1:2] == ' ':
        for i in ( ' A', ' B', ' C', ' D', ' E', ' F', ' G', ' H', ' J', ' K', ' L', ' M', ' N', ' P', ' R', ' S', ' T', ' V', ' W', ' Y', ' Z', 'WX', 'XA', 'XB', 'XC', 'XD', 'XE', 'XG', 'XH'):
            id[0] = i[0]
            id[1] = i[1]
            generate(id)
    for _ in range(2,8):
        if  id[_] == " ":
            if recommend[_] == []:
                print(f"empty position detected({_+1}), any recommend number?")
                recommend[_] = [i for i in input() if i.isnumeric]
            if recommend[_] == []:
                recommend[_] = [i for i in range(10)]
            for j in recommend[_]:
                id[_] = str(j)
                generate(id)
    if  id[8] == " ":
        id[8] = str(check_digit_calculate(id))
    if check_legal(id):
        output.append(''.join(id))


recommend =[[] for i in range(9)]
known = []
output = []
while not input_test(): #if can't pass the test, then loop
        
    print('''enter the known position of the ID
Please enter a space before the ID number if there are only one alphabet
If you don't know the character, just use space
    ''')
    known = [str(i) for i in input().upper()]

if ''.join(known[1:9]).find(' ') == -1:
    print(check_legal(known))
else:
    generate(known)
    print(*list(dict.fromkeys(output)),sep = '\n')
    input()
