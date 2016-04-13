from register import Register
from datetime import datetime


def log(log):
    if Register.LOGS_FLAG:
        f = open('/opt/log/aquapc.log', 'a')
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        tmp = time + " " + log
        f.write(tmp + "\n")
        f.close()

        if len(Register.LOGS_EVENTS) > 20:
            del(Register.LOGS_EVENTS[-1])

        Register.LOGS_EVENTS = [{'date': time,
                                 'message': log}] + Register.LOGS_EVENTS

