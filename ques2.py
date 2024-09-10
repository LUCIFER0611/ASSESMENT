import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handled in thread: {threading.current_thread().name}")

# Printing the thread name where the user is created
print(f"User creation in thread: {threading.current_thread().name}")
user = User.objects.create(username="test_user")
