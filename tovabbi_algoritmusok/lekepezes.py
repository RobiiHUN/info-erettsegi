
'''

# lower(), upper(), capitalize(), swapcase()
# isupper(), islower(), isalpha(), isdecimal()

def atvalto(szo):
    return szo.lower()


gyumolcsok = ['ALMA', 'KÖRTE', 'EPER', 'BANÁN']
# map(fgv, tarolo)
atalakitott = list(map(atvalto, gyumolcsok))
print(f'{atalakitott=}')    


'''


rendszamok = ['ABC123', 'ABCD777', 'WN25L']
#atalakitva = ['|||***', '||||***', '||**|']

i = 0
atalakitva =[]
while i < len(rendszamok):
    for betu in rendszamok[i]:
        if betu.isdigit():
            betu = '*'
        else:
            betu = '|'
        atalakitva.append(betu)
        
    i += 1

print(*atalakitva)