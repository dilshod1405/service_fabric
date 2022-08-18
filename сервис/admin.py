from django.contrib import admin

from сервис.models import broadcast, client_s, message

admin.site.register([broadcast, client_s, message])


