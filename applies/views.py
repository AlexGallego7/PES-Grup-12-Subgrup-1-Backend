from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from applies.models import Applies
from applies.serializers import AppliesSerializer
from securEvent import settings


def send_email(name, email):
    subject = "S'ha registrat la vostre sol·licitud"
    message = f'Moltes gràcies per contactar amb nosaltres {name}, \n ' \
              f'\n' \
              f'En un termini màxim de 48h ens posarem amb contacte amb vosté pels canals proporcionats per tal de ' \
              f'poder ajustar el nostre servei a les seves necessitats.\n' \
              f'\n' \
              f'De nou, moltes gràcies,\n' \
              f'\n' \
              f'Atentament, SecurEvent'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail(subject, message, email_from, recipient_list)


class AppliesView(APIView):

    @staticmethod
    def post(request):
        serializer = AppliesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        send_email(serializer.data["name"], serializer.data["email"])
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
