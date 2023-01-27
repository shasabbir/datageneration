import datetime
import requests
import json
from time import sleep

date_time_str = '2023-01-23'
enddate = '2023-01-28'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

rev =True
enddate_obj = datetime.datetime.strptime(enddate, '%Y-%m-%d')
skipdates = ['2023-01-24', '2023-01-26', '2023-01-23']

url = 'https://api.bscl.gov.bd/api/dayparts/save'
#url = 'https://jsonplaceholder.typicode.com/postsmmm'
#sleep(200)
range = [30, 15]
type = ['', 'stb', 'ott']
while date_time_obj < enddate_obj:
    #skip >
    if str(date_time_obj)[0:10] in skipdates:
        ndate = date_time_obj + datetime.timedelta(days=1)
        print(str(ndate)[0:10])
        date_time_obj = ndate
        continue
    #>skip
    for r in range:

        for t in type:
            #skip >
            # if str(date_time_obj)[0:10] == '2023-01-23'  and( (r == 15 and (t == '' or t == 'stb')) or (r == 30 and (t == '' or t == 'ott' or t == 'stb'))):
            #     continue
            #>skip
            myobj = {"range": r, "type": t, "start": str(date_time_obj)[0:10]}
            f = open("file.txt", "r")
            history = json.loads(f.read())
            
            if myobj in history:
                print("already done")
                continue
            else:
                f = open("file.txt", "w")
                history.append(myobj)
                f.write(json.dumps(history))
                f.close()
            print(myobj)
            try:
                
                x = requests.post(url, json=myobj,timeout=3)
                sleep(500)
                print("slept 8 minutes")
            except:
                print("error")
                #sleep(5)
            #print(x.text)
    ndate = date_time_obj + datetime.timedelta(days=1)
    print(str(ndate)[0:10])
    date_time_obj = ndate
    if str(ndate)[0:10]=='2023-01-28' and rev:   
        date_time_str = '2023-01-02'

        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
        enddate = '2023-01-20'

        enddate_obj = datetime.datetime.strptime(enddate, '%Y-%m-%d')
    
print ("Done")
