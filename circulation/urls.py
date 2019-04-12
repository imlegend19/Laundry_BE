from django.urls import path
from .views import CheckInListView, CheckOutListView

app_name = "circulation"

urlpatterns = [
    path('check-in/', CheckInListView.as_view(), name="check-in-list"),
    path('check-out/', CheckOutListView.as_view(), name="check-out-list"),
]
