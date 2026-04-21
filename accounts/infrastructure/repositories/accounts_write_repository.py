from django.contrib.auth.models import User
from django.db import transaction, IntegrityError, DatabaseError
from core.exceptions.bd import RepositoryError, AccountAlreadyExistsError
from player.models import Player


def create_account_repository(email, password) -> User:
    try:
        with transaction.atomic():
            user = User.objects.create_user(username=email, password=password)
            player = Player.objects.create(user=user, nickname=email.split("@")[0])
            player.save()
            return user
    except IntegrityError as e:
        raise AccountAlreadyExistsError from e
    except DatabaseError as e:
        raise RepositoryError from e
