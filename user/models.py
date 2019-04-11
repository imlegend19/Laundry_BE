from django.db import models
from django.utils.text import gettext_lazy as _


class User(models.Model):
    card_no = models.IntegerField(verbose_name=_('Card Number'), unique=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    erp = models.CharField(verbose_name=_('Enrollment Number'), max_length=200, unique=True)
    registered = models.BooleanField(verbose_name=_('Registered ?'), default=0)
    mobile = models.IntegerField(verbose_name=_('Mobile'), null=True, blank=True)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class ExcelData(models.Model):
    excel_file = models.FileField(verbose_name=_('Users Excel File'))
