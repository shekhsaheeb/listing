from django.db import models

# Create your models here.

class user_info(models.Model):
	user_name = models.CharFiedl(max_length = 50)
	