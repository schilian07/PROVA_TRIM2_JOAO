dia = int(input("Digite um dia:"))
mes = int(input("Digite um mes:"))

if (mes == 1 or mes == 2):
    print("Você está no Verão!")
elif (mes == 3) and (dia < 21):
    print("Você está no Verão!")
elif (mes >= 3) and (mes < 6):
    print("Você está no Outono!")
elif (mes == 6) and (dia <= 21):
    print("Você está no Outono!")
elif (mes == 6) and (dia > 21):
    print("Você está no Inverno!")    
elif(mes <= 9 and dia < 23):
    print("Você está no Inverno!")
elif(mes == 9 and dia >= 23):
    print("Você está na Primavera")
elif(mes >= 10 and mes <= 11):
    print("Você está na Primavera")
elif(mes == 12 and dia < 21):
    print("Você está na Primavera")
elif(mes ==12 and dia >= 21):
    print("Você está no Verão")
