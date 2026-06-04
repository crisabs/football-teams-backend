from django.urls import path
from store.api.views import CoinsAcquireAPIView

app_name = "store"

urlpatterns = [
    path("coins-acquire/", CoinsAcquireAPIView.as_view(), name="coins_acquire")
]
