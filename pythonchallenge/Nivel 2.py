sinais = open("Nivel 2 txt", "r")

sinais_list = []
for linhas in sinais:
    for sinal in linhas:
        sinais_list.append(sinal) if sinal not in sinais_list else None
print(sinais_list)
#Respota: equality