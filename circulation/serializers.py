from rest_framework import serializers


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import CheckIn

        model = CheckIn
        fields = ('id', 'check_in_date', 'card_no', 'clothes')


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import CheckOut

        model = CheckOut
        fields = ('id', 'check_out_date', 'card_no', 'clothes')
