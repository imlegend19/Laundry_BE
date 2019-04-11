from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = ('id', 'card_no', 'erp', 'registered')
