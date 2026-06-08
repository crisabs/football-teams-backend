from django.urls import path
from store.api.views import CoinsAcquireAPIView, StoreItemAcquireAPIView

app_name = "store"

urlpatterns = [
    path("coins-acquire/", CoinsAcquireAPIView.as_view(), name="coins_acquire"),
    path(
        "store-item-acquire/",
        StoreItemAcquireAPIView.as_view(),
        name="store_item_acquire",
    ),
]
