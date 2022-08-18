from rest_framework import serializers

from сервис.models import client_s, broadcast, message


# API по добавления нового клиента
class InfoClient(serializers.ModelSerializer):
    class Meta:
        model = client_s
        fields = ('number_client', 'mobile_code', 'date', 'id')


# API по добавления новой рассылки со всеми её атрибутами
class Infobroadcast(serializers.ModelSerializer):
    class Meta:
        model = broadcast
        fields = ('date_launch', 'delivered_message', 'mobile_code', 'scheduled_message', 'id')


# API для сообщение
class Infomessage(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = ('date_making', 'status', 'sent_message_id', 'client_id', 'id')
