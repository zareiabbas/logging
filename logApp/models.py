from django.db import models
import logging
from django.utils.translation import gettext_lazy as _
from six import python_2_unicode_compatible

LEVELS = (
    (logging.INFO, _('Info')),
    (logging.WARNING, _('Warning')),
    (logging.ERROR, _('Error')),
    (logging.CRITICAL, _('Critical')),
)


@python_2_unicode_compatible
class LogMessage(models.Model):
    logger_name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=LEVELS,
                                             default=logging.ERROR,
                                             db_index=True)
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.level}:: {self.msg}"

    class Meta:
        ordering = ('-create_datetime', )
