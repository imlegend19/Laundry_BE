from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView, CreateAPIView

from circulation.models import InsideLaundry
from .serializers import InsideLaundrySerializer


class InsideLaundryListView(ListCreateAPIView):
    from rest_framework.permissions import AllowAny

    permission_classes = (AllowAny,)
    queryset = InsideLaundry.objects.all()
    serializer_class = InsideLaundrySerializer

    def perform_create(self, serializer):
        check_in_data = InsideLaundry.objects.create(
            card_no=serializer.validated_data['card_no'],
            clothes=serializer.validated_data['clothes'])

        return self.get_serializer(check_in_data)


class InsideLaundryView(UpdateAPIView):
    from rest_framework.permissions import AllowAny

    permission_classes = (AllowAny,)
    queryset = InsideLaundry.objects.all()
    serializer_class = InsideLaundrySerializer


class LaundryCirculationView(CreateAPIView):
    from rest_framework.permissions import AllowAny

    from .models import LaundryCirculation
    from .serializers import LaundryCirculationSerializer

    permission_classes = (AllowAny, )
    queryset = LaundryCirculation.objects.all()
    serializer_class = LaundryCirculationSerializer


class LaundryCirculationListView(ListAPIView):
    from rest_framework.permissions import AllowAny

    from .models import LaundryCirculation
    from .serializers import LaundryListSerializer

    permission_classes = (AllowAny, )
    queryset = LaundryCirculation.objects.all()
    serializer_class = LaundryListSerializer
