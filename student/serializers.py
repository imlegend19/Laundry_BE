from rest_framework import serializers


from .models import StudentExcelData, Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Student

        model = Student
        fields = ('card_no', 'erp', 'registered')


class StudentExcelDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentExcelData
        fields = ('id', 'excel_file')
