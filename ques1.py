import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal received, starting processing...")
    time.sleep(5)  # Simulate long processing
    print("Processing finished")

# Creating a new user instance
user = User.objects.create(username="test_user")
print("User created")
