from django.db import models
from django.utils.text import gettext_lazy as _

from student.models import Student


class InsideLaundry(models.Model):
    check_in_date = models.DateTimeField(_('Check In Date'), auto_now_add=True)
    card_no = models.OneToOneField(to=Student, on_delete=models.PROTECT, verbose_name=_("Card Number"),
                                   primary_key=True)
    clothes = models.IntegerField(verbose_name=_('Number of Clothes'), default=15)
    ready = models.BooleanField(verbose_name=_("Bag Ready ?"))

    class Meta:
        ordering = ['-check_in_date']
        verbose_name = _('Check In')
        verbose_name_plural = verbose_name


class LaundryCirculation(models.Model):
    card_no = models.ForeignKey(to=Student, on_delete=models.PROTECT, verbose_name=_("Card Number"))
    check_out_date = models.DateTimeField(_('Check Out Date'), auto_now_add=True)
    clothes = models.IntegerField(verbose_name=_('Number of Clothes'), default=15)
    check_in_date = models.DateTimeField(verbose_name=_('Check In Date'), null=True)

    class Meta:
        verbose_name = _('Laundry Circulation')
        verbose_name_plural = verbose_name

