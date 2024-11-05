'''In a company, worker efficiency is determined on the basis of the time required for a worker
to complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the
worker is said to be highly efficient. If the time required by the worker is between 3 – 4 hours,
then the worker is ordered to improve speed. If the time taken is between 4 – 5 hours, the
worker is given training to improve his speed, and if the time taken by the worker is more than 5 hours, then the worker has to leave the company. If the time taken by the worker is
input through the keyboard, find the efficiency of the worker.'''

time=int(input("Enter time to complete job: "))
if time>=2 and time<=3:
    print("Highly efficient")
elif time>=3 and time<=4:
    print("Improve speed")
elif time>=4 and time<=5:
    print("Give training")
else:
    print("Leave the company")