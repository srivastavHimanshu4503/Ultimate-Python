"""
A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.
"""

hori_l7 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
veri_l7 = ""
for num in hori_l7:
    veri_l7 += "{}\n".format(num)
print(veri_l7)