
number_of_weeks = int(input("Hetek szama = "))
goal = float(input("Elerni kivant testomeg (kg) = "))


values = []


for week in range(1, number_of_weeks + 1):
    akt_ertek = float(input(f'{week}.heten='))
    values.append(akt_ertek)


success = 0

for index, weight in enumerate(values):
    if weight <= goal:
        success = index + 1
        break

if success:
    print(f'Mari neni a(z) {success}. heten erte el a celt! ')
else:
    print('Sajos Mari neni nem erte el a celjat.')


grow = 0

for index in range(number_of_weeks - 2):
    if values[index] < values[index + 1]:
        grow += 1  

if grow:
    print(f'A tomege {grow} esetben nott az egyik hetrol a masikra')
else:
    print('A tomege nem nott egyik hetrol a masikra')