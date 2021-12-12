import logging
from django.http import HttpResponse
logger = logging.getLogger('db_logger')


def sayHello(request):
    try:
        int('Zarei')
    except:
        logger.exception(ValueError)

    return HttpResponse('Hello!!!!!!!')