
word = input("Kerem a robot parancsait: ")
min_path = " "



count_e = word.count("E")
count_d = word.count("D")
count_n = word.count("N")
count_k = word.count("K")


print(f"E betuk szama: {count_e}")
print(f"D betuk szama: {count_d}")
print(f"K betuk szama: {count_k}")
print(f"N betuk szama: {count_n}")




"""
                    É-D elmozdulás
"""

vertical = count_e - count_d

if vertical > 0:
    min_path += vertical * "E"
elif vertical < 0:
    min_path += abs(vertical) * "D"


"""
            K-NY elmozdulás
"""

horizontal = count_k - count_n

if horizontal > 0:
    min_path += horizontal * "K"
elif horizontal < 0:
    min_path += abs(horizontal) * "N"

print(f"Egy legrovidebb ut parancsszava: {min_path}")

