from django.urls import path
from .views import InsideLaundryListView, LaundryCirculationView, LaundryCirculationListView, InsideLaundryView

app_name = "circulation"

urlpatterns = [
    path('check-in/', InsideLaundryListView.as_view(), name="check-in-post"),
    path('check-in/<int:pk>', InsideLaundryView.as_view(), name="check-i-detail"),
    path('check-out/', LaundryCirculationView.as_view(), name="check-out-list"),
    path('history/', LaundryCirculationListView.as_view(), name="history")
]
