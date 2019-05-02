from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = ('card_no', 'erp', 'registered', 'name', 'mobile')


class StudentExcelDataSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import StudentExcelData

        model = StudentExcelData
        fields = ('id', 'excel_file')
