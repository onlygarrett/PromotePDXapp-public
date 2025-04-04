from django.db import models


class UserAccount(models.Model):
    email = models.CharField(unique=True, max_length=50)
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.email
