import logging

from .config import DJANGO_DB_LOGGER_ENABLE_FORMATTER

db_default_formatter = logging.Formatter()


class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        from .models import LogMessage
        from django.contrib.auth.models import User

        trace = None

        if record.exc_info:
            trace = db_default_formatter.formatException(record.exc_info)

        if DJANGO_DB_LOGGER_ENABLE_FORMATTER:
            msg = self.format(record)
        else:
            msg = record.getMessage()

        kwargs = {
            'logger_name': record.name,
            'level': record.levelno,
            'msg': msg,
            'user': User.objects.get(username='admin'),
            'trace': trace,
        }

        LogMessage.objects.create(**kwargs)

    def format(self, record):

        if self.formatter:
            fmt = self.formatter
        else:
            fmt = db_default_formatter

        if type(fmt) == logging.Formatter:
            record.message = record.getMessage()
            return fmt.formatMessage(record)
        else:
            return fmt.format(record)
