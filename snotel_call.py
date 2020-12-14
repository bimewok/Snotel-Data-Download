import requests
import pandas as pd
import copy
import os
import datetime
import time

stations = ['836:MT', '835:MT', '760:MT', '930:MT']
end_date = '04-12-2020'
start_date = '04-01-2020'
filepath = r'C:\Ben\DATA'
features = r'/WTEQ::value,PRCP::value,TMAX::value,TMIN::value'
#the header is set for these particular fields. If you change the number of fields you may need to set the header to match the .csv's
header = 56





def get_data(stations, end_date, start_date, filepath, features, header):
    #parse dates
    sd = datetime.datetime.strptime(start_date, '%m-%d-%Y')
    ed = datetime.datetime.strptime(end_date, '%m-%d-%Y')
    cd = datetime.datetime.now()
    left_delta = cd - sd
    right_delta = cd - ed
    left_days = -left_delta.days
    right_days = -right_delta.days
    
    
    #create DF to merge data into
    snotel = pd.DataFrame(columns=['date'])
    for i in pd.date_range(start =start_date,  end =end_date, freq ='D'):
        snotel = snotel.append({'date': i}, ignore_index=True)
        
        
    #make requests    
    for i in stations:
        url = 'https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customSingleStationReport/daily/'+str(i)+':SNTL%7Cid=%22%22%7Cname/'+str(left_days)+','+str(right_days)+features
        file = requests.get(url)
        path = os.path.join(filepath, str(i)[:3]+'snotel.csv')
        
        
        open(path, 'wb').write(file.content)
        print('finished getting '+str(i))
        station = copy.copy(str(i)[:3])
        i = pd.read_csv(path, header=header)
        
        i.columns = [str(col) + str(station) for col in i.columns]
        i['Date'] = pd.to_datetime(i['Date'+str(station)])
        snotel = snotel.merge(i, how='left', left_on='date', right_on='Date')
        print('finished merging '+str(station))
        time.sleep(5)
    #clean up data a bit
    for i in snotel.columns.unique():
        if 'Date' in str(i):
            snotel = snotel.drop(i, axis=1)
    #save DF
    snotel.to_csv(os.path.join(filepath, 'snotel.csv'))
    return snotel
