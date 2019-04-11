from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import User

        model = User
        fields = ('id', 'card_no', 'erp', 'registered')


class ExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import ExcelData

        model = ExcelData
        fields = ('id', )
