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


def seat_assign(event_id, user_id, n):
    # ACONSEGUIR STRING SEATS DE L'EVENT I LES DISTANCIES DE LA SALA EN QUESTIO
    event = Events.objects.get(_id=event_id)
    room = Rooms.objects.get(_id=event.id_room)
    matrix = string_to_matrix(event.seats)

    # CALCULAR OFFSET DE SEATS
    offset = get_offset(room.distance_between_seats, room.seats_size)

    # ASSIGNAR SEIENT
    seients = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'T':
                matrix[i][j] = str(user_id)
                seients.append(str(i) + "-" + str(j))
                # INVALIDAR SEIENT(s) COVID HORITZONTALS
                for f in range(offset):
                    if j + f + 1 < room.columns:
                        matrix[i][j + f + 1] = 'F'
                # INVALIDAR SEIENT COVID VERTICAL
                matrix[i + 1][j] = 'F'
                save_matrix(event_id, matrix)
                return seients
