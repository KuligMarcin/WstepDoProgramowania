# • Dla osób poniżej 4 roku życia wstęp jest bezpłatny. (0,4)
# • Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.[4,18]
# • Dla osób powyżej 18 roku życia bilet kosztuje 20zł.{18
# Przykład: Wprowadź wiek klienta: 5
# Cena biletu: 10zł
x = int(input("podaj wiek"))
if  0<=x<=4:
    print("free")
elif 4<  x <=18:
    print("10zł")
elif x<0:
    print("nie możliwe")
else:
    print("20zł")