from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler: Is transaction active? {transaction.get_connection().in_atomic_block}")

def create_user_in_transaction():
    with transaction.atomic():
        print(f"Before User creation: Is transaction active? {transaction.get_connection().in_atomic_block}")
        user = User.objects.create(username="test_user")
        print(f"After User creation: Is transaction active? {transaction.get_connection().in_atomic_block}")

create_user_in_transaction()
