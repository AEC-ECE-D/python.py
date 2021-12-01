e = input('Enter a mathematical expression: ')
print(e)
c= ''
for i in range(len(e)-1):
    if e[i].isalnum() and (e[i+1].isalpha() or e[i+1] == '('):
        c += e[i] + '*'
    elif e[i] == ')' and e[i+1] == '(':
        c += e[i] + '*'
    else:
        c += e[i]
c += e[i+1]
print(c)
