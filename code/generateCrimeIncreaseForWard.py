import json
import csv
import numpy as np

months=('2016_01','2016_02','2016_03','2016_04','2016_05','2016_06','2016_07','2016_08','2016_09','2016_10','2016_11','2016_12','2017_01','2017_02','2017_03','2017_04','2017_05','2017_06','2017_07','2017_08','2017_09','2017_10','2017_11','2017_12','2018_01','2018_02','2018_03','2018_04','2018_05','2018_06')

def getCrimeStatsFromWardFile (fname, category=None):
    try:
        dt = json.load(open(fname))
    except:
        return -1
    if not category:
        return len(dt)
    else:
        count = 0
        for entry in dt:
            if entry['category'] == category:
                count += 1
    return count

def getChangeForWardFile(ward,category=None):
    data = list()
    mcount = 0
    for month in months:
        fname = 'london_month_'+month+'/crime_month_'+month+'_area_'+ward+'_0.json'
        res = getCrimeStatsFromWardFile(fname,category)
        if res>-1:
            data.append((mcount,res))
        mcount += 1
    if len(data):
        adata = np.array (data) 
        return np.polyfit(adata[:,0],adata[:,1],1)[0]
    else:
        return None

def getAmountForWardFile(ward,month='2018_03',category=None):
    data = list()
    mcount = 0
    fname = 'london_month_'+month+'/crime_month_'+month+'_area_'+ward+'_0.json'
    res = getCrimeStatsFromWardFile(fname,category)
    if res == -1:
        return None
    return res;

    
def generateCrimeIncreases(category):
    dout = csv.writer(open('ward_rates_'+category+'.csv','w'))
    dout.writerow(('ward','rate of change'))
    for line in open('london_ward_ids_only.csv'):
        id = line.strip()
        rate = getChangeForWardFile(id,category=category)
        if not rate is None:
            dout.writerow((id,rate))

def generateCrimeAmounts(category):
    dout = csv.writer(open('ward_amounts_'+category+'.csv','w'))
    dout.writerow(('ward','amount'))
    for line in open('london_ward_ids_only.csv'):
        id = line.strip()
        rate = getAmountForWardFile(id,category=category)
        if not rate is None:
            dout.writerow((id,rate))
            


                    
