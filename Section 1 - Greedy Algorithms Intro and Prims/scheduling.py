#%%
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#%%
file = open('jobs.txt', 'r')

n = file.readline() #first line, number of jobs
jobs = []

for line in file.readlines():
    jobs.append([int(x) for x in line.split(' ')])
#%%
test = []
jobs = [list(range(6,1, -1)),list(range(1, 10, 2))]
for i in range(5):
    test.append([jobs[0][i], jobs[1][i]])    


#%%
def WeightedCT(sched):
    WCT = 0 #Total Weighted Completion
    CT = 0 #Completion Time
    while sched:
        job = sched.pop(0) #job is [weight, length]
        CT += job[1]
        WCT += (CT * job[0])
    return WCT
        

#%%
def DiffWeight(jobs):
    sched = {}
    for job in jobs:
        spot = job[0] - job[1]
        if spot not in sched.keys():
            sched[spot] = [job]
        else:
            sched[spot].append(job)
    print(sorted(sched)[::-1])
    final = []
    for key in sorted(sched)[::-1]:
        if len(sched[key]) > 1:
            sched[key] = sorted(sched[key], key = lambda x: x[1], reverse = True)
            for job in sched[key]:
                final.append(job)
        else:
            final.append(sched[key][0])
    return final            
#Correct Answer: 69119377652, got it

#%%
def RatioWeight(jobs):
    sched = {}
    for job in jobs:
        spot = job[0]/job[1]
        if spot not in sched.keys():
            sched[spot] = [job]
        else:
            sched[spot].append(job)
    print(sorted(sched)[::-1])
    final = []
    for key in sorted(sched)[::-1]:
        if len(sched[key]) > 1:
            sched[key] = sorted(sched[key], key = lambda x: x[1], reverse = True)
            for job in sched[key]:
                final.append(job)
        else:
            final.append(sched[key][0])
    return final            
#Correct ANswer: 67311454237, got it