import math

a = float(input("Input Nilai A: "))
b = float(input("Input Nilai B: "))
c = float(input("Input Nilai C: "))

determinan = b**2 - 4*a*c

if determinan > 0:
    jenis_akar = "Akar Berbeda"
    x1 = (-b + math.sqrt(determinan)) / (2*a)
    x2 = (-b - math.sqrt(determinan)) / (2*a)
elif determinan == 0:
    jenis_akar = "Akar Kembar"
    x1 = x2 = -b / (2*a)
else:
    jenis_akar = "Akar Imaginer"
    x1 = f"-{int(b)} + √{int(determinan)}/2*{int(a)}"
    x2 = f"-{int(b)} - √{int(determinan)}/2*{int(a)}"

print(f"Persamaan kuadrat: {int(a)}x² + ({int(b)})x + {int(c)}")
print(f"Determinannya = {int(determinan)}")
print(f"ini adalah jenis {jenis_akar}")
print(f"Akar x1 = {x1}")
print(f"Akar x2 = {x2}")
3