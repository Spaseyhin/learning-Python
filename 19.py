mass = float(input())
height = float(input())

calculations  = mass / (height * height) 

if calculations < 18.5:
    print("Недостаточная масса")
elif calculations > 25:
   print("Избыточная масса")
else:
     print("Оптимальная масса")