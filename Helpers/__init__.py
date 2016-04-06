from register import Register
from datetime import datetime


def log(log):
    if Register.LOGS_FLAG:
        f = open('/opt/log/aquapc.log', 'a')
        tmp = datetime.now().strftime('%y-%m-%d %H:%M:%S') + " " + log
        f.write(tmp + "\n")
        f.close()
        print(tmp)
