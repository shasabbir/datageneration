import datetime
import requests
from time import sleep

date_time_str = '2023-01-23'

date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
enddate = '2023-01-28'
skipdate1 = '2023-01-24'
skipdate2 = '2023-01-26'
skipdate1_obj = datetime.datetime.strptime(skipdate1, '%Y-%m-%d')
skipdate2_obj = datetime.datetime.strptime(skipdate2, '%Y-%m-%d')
enddate_obj = datetime.datetime.strptime(enddate, '%Y-%m-%d')

url = 'https://api.bscl.gov.bd/api/dayparts/save'
url = 'https://jsonplaceholder.typicode.com/posts'

range = [30, 15]
type = ['', 'stb', 'ott']
while date_time_obj < enddate_obj:
    #skip >
    if date_time_obj == skipdate1_obj or date_time_obj == skipdate2_obj:
        ndate = date_time_obj + datetime.timedelta(days=1)
        print(str(ndate)[0:10])
        date_time_obj = ndate
        continue
    #>skip
    for r in range:

        for t in type:
            #skip >
            if (str(date_time_obj)[0:10] == '2023-01-23' and r == 30 and (t == '' or t == 'stb')):
                continue
            #>skip
            myobj = {"range": r, "type": t, "start": str(date_time_obj)[0:10]}
            try:
                print(myobj)
                x = requests.post(url, json=myobj,timeout=3)
            except:
                print("sleeping for 16 minutes")
                sleep(800)
            #print(x.text)
    ndate = date_time_obj + datetime.timedelta(days=1)
    print(str(ndate)[0:10])
    date_time_obj = ndate
print ("Done")
