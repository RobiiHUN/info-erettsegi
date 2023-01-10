
print("1. feladat")


doc_name = input('Adja meg a bemeneti fajl nevet! ')
line  = int(input('Adja meg egy sor szamat! ')) - 1
column = int(input('Adja meg egy oszlop szamat! ')) - 1

spreadsheet = []
steps = []


with open(doc_name, 'r') as doc:
    for doc_line in doc:
        doc_line = doc_line.strip().split()
        values = [int(data) for data in doc_line]
        if len(values) == 9:
            spreadsheet.append(values)
        else:
            steps.append(values)


print("3.feladat")

if spreadsheet[line][column] == 0:
    print('Az adott helyet meg nem toltottek ki')
else:
    print(f'Az adott helyen szreplo szam: {spreadsheet[line][column]}')
print(f'A hely {3 * (line // 3) + (column // 3) + 1} a resztablahoz tartozik.')

print("4.feladat")

empty_places = 0 

for l in spreadsheet:
    for value in l:
        if value == 0:
            empty_places += 1
print(f'Az ures helyek aranya {empty_places / 81 *100:.1f}%')

print("5.feladat")


for step in steps:
    exist = False
    number = step[0]
    line = step[1] - 1
    column = step[2] - 1
    print(f'A kivalasztott sor: {step[1]} oszlop: {step[2]} a szam: {step[0]}')

    if spreadsheet[line][column]:
        print("A helyet mar kitoltottek")
    else:
        if number in spreadsheet[line]:
            print('Az adott sorban mar szerepel szam')  
        else:
            for l in range(9):
                if spreadsheet[l][column] == number:
                    exist = True
                    break
            if exist:
                print('Az adott oszlopban mar szerepel szam.')
            else:
                for l in range(3* (line // 3), 3* (line // 3) + 3):
                    for c in range(3 * (column // 3), 3 * (column // 3) +3):
                        if spreadsheet[l][c] == number:
                            exist = True
                if exist:
                    print('A resztablazatban mar szerepel a szam.')
                else:
                    print('A lepes megteheto.')