from rest_framework.generics import ListAPIView
import xlrd
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView

from student.models import Student
from student.serializers import StudentExcelDataSerializer


class StudentView(ListAPIView):
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
    search_fields = ('card_no', 'erp', )


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    @staticmethod
    def post(request):

        file_serializer = StudentExcelDataSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            file = file_serializer.data.get('excel_file')

            Student.objects.all().delete()

            wb = xlrd.open_workbook(file)
            sheet = wb.sheet_by_index(0)

            num_rows = sheet.nrows
            num_cells = sheet.ncols

            lst = []

            for i in range(num_cells):
                lst.append(sheet.cell_value(0, i))
            lst[0] = 'id'

            for i in range(1, num_rows):

                id = None
                card_no = None
                name = None
                erp = None
                registered = None
                mobile = None

                for j in range(num_cells):
                    tpe = lst[j]
                    if tpe == 'registered':
                        if sheet.cell_value(i, j) in ('OK', 'ok', 'Ok', 'oK'):
                            registered = 1
                        else:
                            registered = 0
                    elif tpe == 'name':
                        name = sheet.cell_value(i, j).title()
                    elif tpe == 'erp':
                        erp = sheet.cell_value(i, j)
                    elif tpe == 'card_no':
                        card_no = int(sheet.cell_value(i, j))
                    elif tpe == 'id':
                        id = int(sheet.cell_value(i, j))
                    elif tpe == 'mobile':
                        mobile = sheet.cell_value(i, j)

                instance = Student()
                instance.name = name
                instance.card_no = card_no
                instance.registered = registered
                instance.mobile = mobile
                instance.erp = erp
                instance.id = id

                instance.save()

            return HttpResponse(status=201)

        return HttpResponse(status=500)
