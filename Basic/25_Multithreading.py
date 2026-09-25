import threading
import time

def download_policy():
    print("downloading policy...............")
    time.sleep(5)
    print("policy downloaded................")

def sendEmail():
    print("sending email...................")
    time.sleep(2)
    print("email send......................")


t1=threading.Thread(target=download_policy)
t2=threading.Thread(target=sendEmail)

t1.start()
t2.start()
t1.join()
t2.join()

print("program terminated................")