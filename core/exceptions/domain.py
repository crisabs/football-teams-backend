from .base import AppException
from rest_framework import status


class AccountRegistrationError(AppException):
    default_code = "ACCOUNT_REGISTRATION_ERROR"
    default_detail = "Account registration failed"


class UserNotFoundError(AppException):
    default_code = "USER_NOT_FOUND"
    default_detail = "User not found"


class PlayerNotFoundError(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "PLAYER_NOT_FOUND"
    default_detail = "The authenticated user has no player profile."


class PlayerTeamNotFoundError(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "PLAYER_TEAM_NOT_FOUND"
    default_detail = (
        "The authenticated user has no team associated according to the request"
    )


class PlayerItemNotFoundError(AppException):
    default_code = "PLAYER_ITEM_NOT_FOUND"
    default_detail = (
        "The authenticated user has no item associated according to the request"
    )


class TeamNotFoundError(AppException):
    default_code = "TEAM_NOT_FOUND"
    default_detail = "Team not found"


class ItemStoreNotFoundError(AppException):
    default_code = "ITEM_NOT_FOUND"
    default_detail = "Item not found"


class NotEnoughCoinsError(AppException):
    status_code = status.HTTP_409_CONFLICT
    default_code = "NOT_ENOUGH_COINS"
    default_detail = "Not enough coins"


class ZoneAlreadySetError(AppException):
    status_code = status.HTTP_409_CONFLICT
    default_code = "ALREADY_IN_ZONE"
    default_detail = "Fisher already in the zone"


class InvalidZoneError(AppException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "INVALID_ZONE"
    default_detail = "Invalid zone"
