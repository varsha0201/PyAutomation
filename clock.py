from datetime import datetime
from whatsup_love import send_love

from apscheduler.schedulers.blocking import BlockingScheduler


sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_love, 'interval', hours=10)

sched.start()