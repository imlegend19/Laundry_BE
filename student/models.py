from django.db import models
from django.utils.text import gettext_lazy as _


class Student(models.Model):
    card_no = models.IntegerField(verbose_name=_('Card Number'), primary_key=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    erp = models.CharField(verbose_name=_('Enrollment Number'), max_length=200)
    registered = models.BooleanField(verbose_name=_('Registered ?'), default=0)
    mobile = models.CharField(_('Mobile Number'), max_length=15, blank=True, null=True)

    class Meta:
        ordering = ['card_no']
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    def __str__(self):
        return self.name


class StudentExcelData(models.Model):
    excel_file = models.FileField(verbose_name=_('Excel Sheet'))

    class Meta:
        verbose_name = _('Excel Sheet')
        verbose_name_plural = _("Excel Sheets")
