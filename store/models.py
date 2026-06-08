from django.db import models


class StoreItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class PlayerStoreItem(models.Model):
    player = models.ForeignKey(
        "player.Player", on_delete=models.CASCADE, related_name="store_items"
    )
    store_item = models.ForeignKey(
        StoreItem, on_delete=models.CASCADE, related_name="player_items"
    )

    acquired_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("player", "store_item")

    def __str__(self):
        return f"{self.player.user.username} - {self.store_item.name}"
