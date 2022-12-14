# Generated by Django 4.0.6 on 2022-08-16 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('сервис', '0003_alter_message_sent_message_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='mobile_code',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='client_s',
            name='mobile_code',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('отправлено', 'отправлено'), ('не отправлено', 'не отправлено')], max_length=13),
        ),
    ]
