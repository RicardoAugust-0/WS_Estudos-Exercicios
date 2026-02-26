anosInput = input("Coloque quantos anos você tem de idade: ")
mesesInput = input("Coloque quantos meses você tem idade: ")
diasInput = input("Coloque quantos dias você tem idade: ")

anos = int(anosInput)
meses = int(mesesInput)
dias = int(diasInput)
totalDias = (anos * 365) + (meses * 30) + dias
print("Você tem " + str(totalDias) + " dias de idade.")