from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# рассылка
class broadcast(models.Model):
    date_launch = models.DateTimeField()                    # дата и время запуска рассылки
    delivered_message = models.TextField(max_length=500)    # текст сообщения для доставки клиенту
    mobile_code = models.CharField(max_length=6)            # фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег)
    scheduled_message = models.DateTimeField()              # дата и время окончания рассылки

    class Meta:
        db_table = 'рассылка'

    def __str__(self):
        return f'{self.delivered_message} ---  {self.mobile_code} --- {self.date_launch} --- {self.scheduled_message}'


# клиент
class client_s(models.Model):
    number_client = models.CharField(max_length=11)         # номер телефона клиента
    mobile_code = models.CharField(max_length=6)            # код мобильного оператора
    date = models.DateTimeField()                           # часовой пояс

    class Meta:
        db_table = 'клиент'

    def __str__(self):
        return f'{self.mobile_code} --- {self.number_client} --- {self.date}'


# сообщение
ok = 'отправлено'
no = 'не отправлено'
my_status = (
    (ok, 'отправлено'),
    (no, 'не отправлено')
)


class message(models.Model):
    date_making = models.DateTimeField()                                        # дата и время создания (отправки)
    status = models.CharField(max_length=13, choices=my_status)                 # статус отправки
    sent_message_id = models.ForeignKey(broadcast, on_delete=models.CASCADE)    # id рассылки, в рамках которой было отправлено сообщение
    client_id = models.ForeignKey(client_s, on_delete=models.CASCADE)           # id клиента, которому отправили
    user = models.ForeignKey(User, on_delete=models.CASCADE)                    # админ пользователь

    class Meta:
        db_table = 'сообщение'

    def __str__(self):
        return f'{self.date_making}  {self.sent_message_id}  {self.client_id}'
