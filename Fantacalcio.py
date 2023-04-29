# https://github.com/polito-info-2021/Esempi-esame/tree/master/esami/fantacalcio

FILE = "fantacalcio.txt"
import random

def read_file(file_name):
    calcio_list = list()
    with open(file_name) as open_file:
        lines = open_file.readlines()
        for i in lines:
            line = i.rstrip().split(", ")
            calcio_list.append(line)
    return calcio_list

def main():
    calcio_list = list()
    difensore = list()
    difensore_budget = 40
    difensore_number = 8
    chosen_difensore = list()
    centrocampista = list()
    centrocampista_budget = 80
    centrocampista_number = 8
    chosen_centrocampista = list()
    attaccante = list()
    attaccante_budget = 120
    attaccante_number = 6
    chosen_attaccante = list()
    portiere = list()
    portiere_budget = 20
    portiere_number = 3
    chosen_portiere = list()
    calcio_list = read_file(FILE)

    for i in calcio_list:
        if i[2] == "difensore":
            difensore.append(i)
        elif i[2] == "centrocampista":
            centrocampista.append(i)
        elif i[2] == "attaccante":
            attaccante.append(i)
        elif i[2] == "portiere":
            portiere.append(i)

    p = 1
    while p <= portiere_number:
        a = random.randrange(0, len(portiere))

        if portiere_budget - int ( portiere[a][3] ) >= 0:
            portiere_budget = portiere_budget - int ( portiere[a][3] )
            chosen_portiere.append(portiere[a])
            portiere.remove(portiere[a])

        else:
            a = random.randrange(0, len(portiere))
            if portiere_budget - int(portiere[a][3]) >= 0:
                portiere_budget = portiere_budget - int(portiere[a][3])
                chosen_portiere.append(portiere[a])
                portiere.remove(portiere[a])
        p+=1

    q = 1
    while q <= difensore_number:
        b = random.randrange(0, len(difensore))

        if difensore_budget - int ( difensore[b][3] ) >= 0:
            difensore_budget = difensore_budget - int ( difensore[b][3] )
            chosen_difensore.append(difensore[b])
            difensore.remove(difensore[b])


        else:
            b = random.randrange(0, len(difensore))
            if difensore_budget - int(difensore[b][3]) >= 0:
                difensore_budget = difensore_budget - int(difensore[b][3])
                chosen_difensore.append(difensore[b])
                difensore.remove(difensore[b])
        q+=1

    x = 1
    while x <= centrocampista_number:
        c = random.randrange(0, len(centrocampista))

        if centrocampista_budget - int(centrocampista[c][3]) >= 0:
            centrocampista_budget = centrocampista_budget - int(centrocampista[c][3])
            chosen_centrocampista.append(centrocampista[c])
            centrocampista.remove(centrocampista[c])


        else:
            c = random.randrange(0, len(centrocampista))
            if centrocampista_budget - int(centrocampista[c][3]) >= 0:
                centrocampista_budget = centrocampista_budget - int(centrocampista[c][3])
                chosen_centrocampista.append(centrocampista[c])
                centrocampista.remove(centrocampista[c])
        x += 1

    y = 1
    while y <= attaccante_number:
        d = random.randrange(0, len(attaccante))

        if attaccante_budget - int(attaccante[d][3]) >= 0:
            attaccante_budget = attaccante_budget - int(attaccante[d][3])
            chosen_attaccante.append(attaccante[d])
            attaccante.remove(attaccante[d])


        else:
            d = random.randrange(0, len(attaccante))
            if attaccante_budget - int(attaccante[d][3]) >= 0:
                attaccante_budget = attaccante_budget - int(attaccante[d][3])
                chosen_attaccante.append(attaccante[d])
                attaccante.remove(attaccante[d])
        y += 1


    print(f"Portieri: {chosen_portiere}")
    print(f"Difensori: {chosen_difensore}")
    print(f"Centrocampisti: {chosen_centrocampista}")
    print(f"Attaccanti: {chosen_attaccante}")


if __name__  == "__main__":
    main()
