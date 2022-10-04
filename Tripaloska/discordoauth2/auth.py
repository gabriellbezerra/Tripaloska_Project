from django.contrib.auth.backends import BaseBackend
from .models import user_class

class DiscordAuthentication(BaseBackend):
    def authenticate(self, request, user) -> user_class:
        find_user = user_class.objects.filter(id = user['id']).first()

        if find_user:
            return find_user
        else:
            discord_tag = '%s%s' %(user['username'], user['discriminator'])
            new_user = user_class.objects.create_new_user(user)
            return new_user

    def get_user(self, user_id):
        try:
            return user_class.objects.filter(pk = user_id).first()
        except user_class.DoesNotExist:
            return None