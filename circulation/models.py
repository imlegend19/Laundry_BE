from django.db import models
from django.utils.text import gettext_lazy as _

from student.models import Student


class CheckIn(models.Model):
    check_in_date = models.DateTimeField(_('Create Date/Time'), auto_now_add=True)
    card_no = models.ForeignKey(to=Student, on_delete=models.PROTECT, verbose_name=_("Card Number"))
    clothes = models.IntegerField(verbose_name=_('Number of Clothes'), default=15)

    class Meta:
        ordering = ['-check_in_date']
        verbose_name = _('Check In')
        verbose_name_plural = verbose_name


class CheckOut(models.Model):
    check_out_date = models.DateTimeField(_('Create Date/Time'), auto_now_add=True)
    card_no = models.ForeignKey(to=Student, on_delete=models.PROTECT, verbose_name=_("Card Number"))
    clothes = models.IntegerField(verbose_name=_('Number of Clothes'), default=15)

    class Meta:
        ordering = ['-check_out_date']
        verbose_name = _('Check Out')
        verbose_name_plural = verbose_name
