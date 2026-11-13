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

    class Rank(models.TextChoices):
        IRON_1 = 'IRON_1', 'Iron 1'
        IRON_2 = 'IRON_2', 'Iron 2'
        IRON_3 = 'IRON_3', 'Iron 3'
        BRONZE_1 = 'BRONZE_1', 'Bronze 1'
        BRONZE_2 = 'BRONZE_2', 'Bronze 2'
        BRONZE_3 = 'BRONZE_3', 'Bronze 3'
        SILVER_1 = 'SILVER_1', 'Silver 1'
        SILVER_2 = 'SILVER_2', 'Silver 2'
        SILVER_3 = 'SILVER_3', 'Silver 3'
        GOLD_1 = 'GOLD_1', 'Gold 1'
        GOLD_2 = 'GOLD_2', 'Gold 2'
        GOLD_3 = 'GOLD_3', 'Gold 3'
        PLATINUM_1 = 'PLATINUM_1', 'Platinum 1'
        PLATINUM_2 = 'PLATINUM_2', 'Platinum 2'
        PLATINUM_3 = 'PLATINUM_3', 'Platinum 3'
        DIAMOND_1 = 'DIAMOND_1', 'Diamond 1'
        DIAMOND_2 = 'DIAMOND_2', 'Diamond 2'
        DIAMOND_3 = 'DIAMOND_3', 'Diamond 3'
        ASCENDANT_1 = 'ASCENDANT_1', 'Ascendant 1'
        ASCENDANT_2 = 'ASCENDANT_2', 'Ascendant 2'
        ASCENDANT_3 = 'ASCENDANT_3', 'Ascendant 3'
        IMMORTAL_1 = 'IMMORTAL_1', 'Immortal 1'
        IMMORTAL_2 = 'IMMORTAL_2', 'Immortal 2'
        IMMORTAL_3 = 'IMMORTAL_3', 'Immortal 3'
        RADIANT = 'RADIANT', 'Radiant'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.PLAYER,
    )
    contact_number = models.CharField(max_length=20, blank=True)
    rank = models.CharField(
        max_length=20,
        choices=Rank.choices,
        blank=True,
    )

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'
