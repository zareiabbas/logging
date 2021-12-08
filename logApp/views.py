import logging

from django.http import HttpResponse

logger = logging.getLogger('db')


def sayHello(request):
    try:
        int('Zarei')
    except:
        logger.exception("gfdrrmtfmjuygu")

    return HttpResponse('Hello!!!!!!!')