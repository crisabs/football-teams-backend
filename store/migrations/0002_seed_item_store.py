from django.db import migrations


def seed_item_store(apps, schema_editor):
    StoreItem = apps.get_model("store", "StoreItem")
    items = [
        {
            "name": "Silver Profile Crown",
            "description": "A shiny crown for a silver player",
            "price": 50.00,
        },
        {
            "name": "Bronze Profile Crown",
            "description": "A sturdy crown for a bronze player",
            "price": 25.00,
        },
        {
            "name": "Golden Profile Crown",
            "description": "A majestic crown fit for a golden player",
            "price": 100.00,
        },
        {
            "name": "Platinum Profile Crown",
            "description": "An exclusive crown for a platinum player",
            "price": 150.00,
        },
        {
            "name": "Diamond Profile Crown",
            "description": "A dazzling crown for a diamond player",
            "price": 200.00,
        },
    ]
    for item in items:
        StoreItem.objects.get_or_create(name=item["name"], defaults=item)


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_item_store),
    ]
