from __future__ import absolute_import, unicode_literals 
from celery import shared_task
from celery.utils.log import get_task_logger
import time

logger = get_task_logger(__name__)

@shared_task
def sum(a,b):
    time.sleep(10)
    return a+b
	
@shared_task
def add():
    return 5+4	
	