
import os, platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')




if os.path.exists('tovabbi_algoritmusok\\valogatas.txt'):
    fajl = open('tovabbi_algoritmusok\\valogatas.txt', 'r')
else:
    print('nem talalom a fajlt')

butrok = {}
butor = []
raktaron = []

for sor in fajl:
    butrok_adatai= sor.split(';')
    butor.append(butrok_adatai[0])

print(butor)