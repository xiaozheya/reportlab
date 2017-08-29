import datetime,os
import test,send_email
def run_task(filename):
    test.rpt()
    send_email.sendemail(filename)
    print 'send successfully on'.format(sched_Timer)

def timerFun(sched_Timer):
    flag=0
    while True:
        now = datetime.datetime.now()
        if(now==sched_Timer):
            run_task('bug.pdf')
            flag=1
        else:
            if flag==1:
                sched_Timer+=datetime.timedelta(days=1)
                flag=0

if __name__=="__main__":
    sched_Timer=datetime.datetime(2017,8,15,16,24,59)

    timerFun(sched_Timer)
