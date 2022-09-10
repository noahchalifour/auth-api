from django.db import models
import uuid
import secrets


def generate_secret():
    return secrets.token_hex(64)


class Client(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    secret = models.CharField(
        max_length=128,
        default=generate_secret,
        editable=False)
    name = models.CharField(
        max_length=32)
    description = models.CharField(
        max_length=128,
        blank=True)
    services = models.JSONField(
        default=list)
    date_created = models.DateTimeField(
        auto_now=True,
        editable=False)