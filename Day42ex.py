import winsound
import datetime
import time


def alarm(hour, minute):
    current_time = datetime.datetime.now()
    alarm_time = current_time.replace(
        hour=hour, minute=minute, second=0, microsecond=0)
    if alarm_time < current_time:
        alarm_time += datetime.timedelta(days=1)
    print("Alarm set for {}".format(alarm_time.strftime("%I:%M %p")))
    time.sleep((alarm_time - current_time).total_seconds())
    winsound.PlaySound("alarm.wav", winsound.SND_FILENAME)


alarm(19, 30)
