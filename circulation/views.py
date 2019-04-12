from rest_framework.generics import ListCreateAPIView


class CheckInListView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import CheckIn
    from .serializers import CheckInSerializer

    permission_classes = (AllowAny,)
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer

    filter_backends = (SearchFilter, DjangoFilterBackend,)
    filter_fields = ('card_no', 'check_in_date',)
    search_fields = ('id', 'card_no', 'check_in_date',)

    def perform_create(self, serializer):
        from .models import CheckIn

        check_in_data = CheckIn.objects.create(
            card_no=serializer.validated_data['card_no'],
            clothes=serializer.validated_data['clothes'])

        return self.get_serializer(check_in_data)


class CheckOutListView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny
    from rest_framework.filters import SearchFilter
    from django_filters.rest_framework.backends import DjangoFilterBackend

    from .models import CheckOut
    from .serializers import CheckOutSerializer

    permission_classes = (AllowAny,)
    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer

    filter_backends = (SearchFilter, DjangoFilterBackend,)
    filter_fields = ('card_no', 'check_out_date',)
    search_fields = ('id', 'card_no', 'check_out_date',)

    def perform_create(self, serializer):
        from .models import CheckOut

        check_in_data = CheckOut.objects.create(
            check_out_date=serializer.validated_data['check_out_date'],
            card_no=serializer.validated_data['card_no'],
            clothes=serializer.validated_data['clothes'], )

        return self.get_serializer(check_in_data)
