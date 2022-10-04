from django.db import models
from .managers import DiscordUserManager

# Create your models here.

class user_class(models.Model):
    objects = DiscordUserManager()

    id = models.BigIntegerField(primary_key=True)
    discord_tag = models.CharField(max_length=30)
    avatar = models.CharField(max_length=200)
    public_flags = models.IntegerField()
    flags = models.BigIntegerField()
    locale = models.CharField(max_length=100)
    mfa_enabled = models.BooleanField()
    last_login = models.DateTimeField(null=True)

    family_name = models.CharField(max_length=15, null=True)
    guild_code = models.CharField(max_length=100,null=True)

    def is_authenticated(self, request):
        return True