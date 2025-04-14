#Escreva um programa que converta um intervalo de tempo dado em minutos,
#em horas, minutos e segundos. Por exemplo, se o tempo dado for 145,87
#minutos, o programa deve fornecer 2 h 25 min 52,2 s.

tmin = float(input("Insira o tempo em minutos"))
tempo = None

if tmin>=60:
    hora = tmin//60
    tmin = tmin - (hora*60)

if tmin>=1:
    min = tmin//1
    tmin = tmin - (min*1)

seg = "xxxx"