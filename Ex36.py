import random

codi = "".join(list(map(lambda x: str(x), random.sample(range(0, 9), 4))))
print(""" Això és el teu primer Mastermind
       	Has d'adivinar un número de 4 xifres diferents.
       	""")
latevaproposta = input("Introduexi un codi de 4 xifres: ")

intents = 0
while latevaproposta != codi:
    intents += 1
    encerts = 0
    coincidencies = 0
    for i in range(4):
        if latevaproposta[i] == codi[i]:
            encerts += 1
        elif latevaproposta[i] in codi:
            coincidencies += 1
    print("La teva proposta (", latevaproposta, ") te", encerts, "encerts i", coincidencies, "coincidències.")
    latevaproposta = input("Torna a introduir un codi de 4 xifres: ")

print("Felicitats! Has endevinat el codi en ", intents, "intents.")
