from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    #- Userをimpotし、1対1使用している
    user = models.OneToOneField(User, on_delete='CASCADE')
    website = models.URLField(blank=True)
    picture = models.FileField(upload_to='user/', blank=True)

    def __str__(self):
        return self.user.username