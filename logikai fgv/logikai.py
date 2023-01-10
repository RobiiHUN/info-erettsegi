import os
import platform
import random


def torles():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    
torles()

a = random.randint(-100,101)
b = random.randint(-100,101) 

def atlag(a,b):
    atl = (a+b) / 2
    print(f'A ket szam atlaga: {round(atl)}')

def szorzat(a,b):
    szorz = a * b
    print(f'A ket szam szorzata: {szorz}')

def osszeg(a,b):
    ossz = a + b
    print(f'A ket szam osszege: {ossz}')

def kisebb(a,b):
    if a > b:
        print(f'A {b} kisebb, mint {a}')
    elif a < b:
        print(f'A {a} kisebb, mint a {b}')
    else:
        print('A ket szam egyenlo!')

def pozitiv(a,b):
    if a > 0 and b > 0:
        print('Mindket szam pozitiv!')
    else:
        print('Az egyik szam nem pozitiv')
    
def paratlan(a,b):
    if a % 2 == 1 or b % 2 == 1:
        print('van koztuk paratlan szam')
    else:
        print('Az egyik szam paros')
    
def tobbszoros(a,b):
    if a % b == 0:
        print(f'A {a}, {b} tobbszorose')
    elif b % a == 0:
        print(f'A {b}, {a} tobbszorose')
    else:
        print('A szamok nem egymas tobbszorosei')



print(a)
print(b)
atlag(a,b)
szorzat(a,b)
osszeg(a,b)
kisebb(a,b)
pozitiv(a,b)
paratlan(a,b)
tobbszoros(a,b)
   