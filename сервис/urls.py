from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import clientView, broadcastView, messageAPI, broadcastdetailView, clientdetailView
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('client/', clientView.as_view()),
    path('client/details/<int:id>/', clientdetailView.as_view()),

    path('broadcast/', broadcastView.as_view()),
    path('broadcast/details/<int:id>/', broadcastdetailView.as_view()),

    path('message/details/', messageAPI.as_view()),


]

urlpatterns += doc_urls
