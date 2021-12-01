sinais = open("Nivel 3 txt", "r").read()
import re

#print(sinais)
sinais_list = []
for linhas in sinais:
    for sinal in linhas:
        sinais_list.append(sinal) if sinal not in sinais_list else None


print(''.join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", sinais)))

#Respota: linkedlist