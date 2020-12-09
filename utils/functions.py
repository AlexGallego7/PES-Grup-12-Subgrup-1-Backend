import numpy

from events.models import Events
from events.serializers import EventsSerializer
from rooms.models import Rooms


def create_matrix(id_room):
    sala = Rooms.objects.get(_id=id_room)
    matrix = [['T'] * sala.columns] * sala.rows
    return matrix


def matrix_to_string(matrix):
    string = '\n'.join('\t'.join(x for x in y) for y in matrix)
    return string


def string_to_matrix(string):
    prematrix = string.split('\n')
    matrix = []
    for i in prematrix:
        matrix.append(i.split('\t'))
    return matrix


def get_offset(distance_between_seats, seats_size):
    offset = 0
    distance = distance_between_seats
    while distance < 1.5:
        distance += seats_size + distance_between_seats
        offset += 1
    return offset


def save_matrix(event_id, matrix):
    event = Events.objects.get(_id=event_id)
    data = {"seats": matrix_to_string(matrix)}
    serializer = EventsSerializer(event, data=data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()


def enough_space(matrix, i, j, reserves, llocs):
    if reserves >= llocs:
        return False
    else:
        for seats in range(reserves):
            if matrix[i][j + seats] != 'T':
                return False
        return True


def seat_assign(event_id, user_id, n):
    # ACONSEGUIR STRING SEATS DE L'EVENT I LES DISTANCIES DE LA SALA EN QUESTIO
    event = Events.objects.get(_id=event_id)
    room = Rooms.objects.get(_id=event.id_room)

    # PROUS LLOCS LLIURES I GENERAR MATRIU
    seients = []
    reserves = int(n)
    if event.seats.count('T') < reserves:
        return seients
    matrix = string_to_matrix(event.seats)

    # CALCULAR OFFSET DE SEATS
    offset = get_offset(room.distance_between_seats, room.seats_size)

    # ASSIGNAR SEIENT (PRIO BUSCAR SEIENTS JUNTS)
    skip_row = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if len(seients) == reserves:
                save_matrix(event_id, matrix)
                return seients
            if matrix[i][j] == 'T':
                if enough_space(matrix, i, j, reserves, room.columns - j):
                    for s in range(reserves):
                        matrix[i][j + s] = str(user_id)
                        seients.append(str(i) + "-" + str(j + s))
                        # INVALIDAR SEIENTS COVID VERTICALS
                        if i + 1 < room.rows:
                            matrix[i + 1][j + s] = 'F'
                        # INVALIDAR SEIENT(s) COVID HORITZONTALS, si som l'últim de la reserva
                        if s == reserves - 1:
                            for f in range(offset):
                                if j + s + f + 1 < room.columns:
                                    matrix[i][j + s + f + 1] = 'F'
                        # SI ENS HEM SALTAT UNA ROW, HEM D'INVALIDAR ELS DE SOTA
                        if skip_row:
                            matrix[i - 1][j + s] = 'F'
                else:  # NO HI CABEN TOTES LES RESERVES A LA MATEIXA FILA
                    skip_row = True

    # c_matrix = numpy.array(matrix)
    # index = numpy.where(c_matrix == 'T')
    # print(index)
    # seient1 = str(index[0][0]) + "-" + str(index[1][0])
    # seient2 = str(index[0][1]) + "-" + str(index[1][1])
    # seient3 = str(index[0][2]) + "-" + str(index[1][2])
    # print(seient1)
    # print(seient2)
    # print(seient3)
    return seients
