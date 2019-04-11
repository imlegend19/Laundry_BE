from requests import Response
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FileUploadParser


class UserView(ListAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import User
    from .serializers import UserSerializer

    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_backends = (SearchFilter, DjangoFilterBackend, )
    filter_fields = ('card_no', 'erp', )
    search_fields = ('id', 'card_no', 'erp', )


class ExcelView(ListAPIView):
    parser_classes = (FileUploadParser, )

    @staticmethod
    def post(request):
        file = request.FILES['file']

        destination = open()

        return Response()

