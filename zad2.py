# (2.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała

litera = input("podaj litere")
if len(litera)>1:
    print("źle")
    exit()
if 'a' <= litera <= 'z':
    print("mała")
elif 'A' <= litera <= 'Z':
    print(" Duża")
else:
    print("nie jest litera")