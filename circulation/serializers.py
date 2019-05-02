from rest_framework import serializers

from circulation.models import LaundryCirculation, InsideLaundry


class InsideLaundrySerializer(serializers.ModelSerializer):

    class Meta:
        from .models import InsideLaundry

        model = InsideLaundry
        fields = ('check_in_date', 'card_no', 'clothes', 'ready')


class LaundryCirculationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        card_no = validated_data.pop('card_no')
        ready = InsideLaundry.objects.get(card_no=card_no).ready

        if ready:
            check_in_date = InsideLaundry.objects.get(card_no=card_no).check_in_date
            clothes = InsideLaundry.objects.get(card_no=card_no).clothes

            InsideLaundry.objects.get(card_no=card_no).delete()

            return LaundryCirculation.objects.create(
                card_no=card_no,
                check_in_date=check_in_date,
                clothes=clothes,
            )
        else:
            return Exception('The bag is not yet ready.')

    class Meta:
        model = LaundryCirculation
        fields = ('id', 'card_no', 'check_in_date', 'check_out_date', 'clothes')
        read_only_fields = ('check_in_date', 'check_out_date',)


class LaundryListSerializer(serializers.ModelSerializer):

    class Meta:
        from .models import LaundryCirculation

        model = LaundryCirculation
        fields = ('id', 'card_no', 'check_in_date', 'check_out_date', 'clothes')
