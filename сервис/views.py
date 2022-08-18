from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from сервис.models import client_s, broadcast, message
from сервис.serializer import InfoClient, Infobroadcast, Infomessage


# добавления нового клиента
class clientView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = client_s.objects.all()
    serializer_class = InfoClient

    def get_queryset(self, id):
        return self.queryset.filter(id=id)

    # добавления нового клиента
    def post(self, request):
        serializer = InfoClient(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # получить информацию о клиента
    def get(self, request):
        comments = client_s.objects.all()
        serializer = InfoClient(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class clientdetailView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = client_s.objects.all()
    serializer_class = InfoClient()

    def get_queryset(self, id):
        return self.queryset.filter(id=id)

    # получить информацию о клиента
    def get(self, request):
        comments = client_s.objects.all()
        serializer = InfoClient(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # удаления клиента
    def delete(self, request, id):
        client = client_s.objects.get(id=id)
        client.delete()
        return Response('Successfully deleted')

    # обновления данных атрибутов клиента
    def put(self, request, id):
        queryset = client_s.objects.get(pk=id)
        serializer = InfoClient(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class broadcastView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer = Infobroadcast()

    # добавления новой рассылки
    def post(self, request):
        serializer = Infobroadcast(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # получения общей статистики по созданным рассылкам
    def get(self, request):
        broadcas_t = broadcast.objects.all()
        serializer = Infobroadcast(broadcas_t, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class broadcastdetailView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    queryset = client_s.objects.all()
    serializer_class = InfoClient()

    def get(self, request):
        broadcas_t = broadcast.objects.all()
        serializer = Infobroadcast(broadcas_t, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # обработки активных рассылок
    @csrf_exempt
    def put(self, request, id):
        broadcas_t = broadcast.objects.get(pk=id)
        serializer = Infobroadcast(broadcas_t, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(broadcastdetailView, self).dispatch(*args, **kwargs)

    # удаления рассылки
    def delete(self, request, id):
        broadcas_t = broadcast.objects.get(pk=id)
        broadcas_t.delete()
        return Response('Successfully deleted')


class messageAPI(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer = Infomessage()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['status']
    search_fields = ['id']

    # получения детальной статистики отправленных сообщений по конкретной рассылке
    def get(self, request):
        messages = message.objects.all()
        serializer = Infomessage(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





