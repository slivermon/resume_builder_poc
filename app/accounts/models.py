from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # pass
    '''
    Fields:
    id, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined
    '''    

    def __str__(self):
        return self.username   
