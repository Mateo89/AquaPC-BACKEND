import threading
import time
import DbDriver
from subprocess import Popen, PIPE
from Helpers import AtlasI2C
from register import Register
import datetime


class PhThread(threading.Thread):

    mail_flag = True

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:

            output = ''
            try:
                process = Popen(["/usr/bin/python", "/root/ph_meter.py"], stdout=PIPE)
                (output, err) = process.communicate()
                process.wait()
                float(output)

            except ValueError:
                if self.mail_flag:
                    self.send_email("mateusz.jaskolowski@gmail.com", "99344539022772", "mateusz.jaskolowski@gmail.com",
                               "NIE DZIALA POMIAR PH", "NIE DZIALA POMIAR PH")
                    self.mail_flag = False
                    time.sleep(60)
                continue

            self.mail_flag = True
            ph_value = float(output)
            Register.PH_VALUE = ph_value
            Register.PH_UPDATE_DATE = str(datetime.datetime.now().replace(microsecond=0))
            DbDriver.db_queue.put(lambda: DbDriver.save_ph_values(ph_value))

            time.sleep(300)  # 5 min

    def send_email(self, user, pwd, recipient, subject, body):
        import smtplib

        gmail_user = user
        gmail_pwd = pwd
        FROM = user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body

        # Prepare actual message
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print 'successfully sent the mail'
        except:
            print "failed to send mail"

