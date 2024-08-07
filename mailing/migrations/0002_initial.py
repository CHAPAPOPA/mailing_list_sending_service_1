# Generated by Django 5.0.6 on 2024-06-26 11:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mailing", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="clients",
            field=models.ManyToManyField(
                blank=True,
                related_name="clients",
                to="mailing.client",
                verbose_name="Клиенты",
            ),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="message",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="message",
                to="mailing.message",
                verbose_name="Сообщение",
            ),
        ),
        migrations.AddField(
            model_name="newsletter",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AddField(
            model_name="attempt",
            name="newsletter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="newsletter",
                to="mailing.newsletter",
            ),
        ),
    ]
