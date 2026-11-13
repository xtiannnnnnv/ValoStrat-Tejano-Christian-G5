from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model for ValoStrat with role-based access.
    Roles: Coach (admin-level) and Player (regular user).
    """

    class Role(models.TextChoices):
        COACH = 'COACH', 'Coach'
        PLAYER = 'PLAYER', 'Player'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.PLAYER,
    )
    contact_number = models.CharField(max_length=20, blank=True)
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True,
    )
    favorite_agent = models.CharField(
        max_length=50,
        blank=True,
        help_text='Your favorite Valorant agent',
    )
    rank = models.CharField(
        max_length=50,
        blank=True,
        help_text='Your current Valorant rank',
    )

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'
