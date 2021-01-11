from celery import Celery
# from time import sleep

app = Celery(
    'tasks',
    result_backend="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0",
    broker="redis://127.0.0.1:6379/0"
)


@app.task
def reverse(text):
    # sleep(5)
    print ("task running")
    print (text[::-1])
    return text[::-1]
    
	
 # celery -A tasks worker --loglevel=info --pool=solo	