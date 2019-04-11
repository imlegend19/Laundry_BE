from rest_framework.generics import ListAPIView


class UserView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import Student
    from .serializers import StudentSerializer

    permission_classes = (AllowAny, )
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = (SearchFilter, DjangoFilterBackend, )
    filter_fields = ('card_no', 'erp', )
    search_fields = ('id', 'card_no', 'erp', )
