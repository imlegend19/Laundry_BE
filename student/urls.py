from django.urls import path
from .views import StudentView, FileView

app_name = "student-details"

urlpatterns = [
    path('student/', StudentView.as_view(), name="student-list"),
    path('upload/', FileView.as_view(), name="student-excel-sheet")
]
