import json
import csv
import numpy as np

months=('2016_01','2016_02','2016_03','2016_04','2016_05','2016_06','2016_07','2016_08','2016_09','2016_10','2016_11','2016_12','2017_01','2017_02','2017_03','2017_04','2017_05','2017_06','2017_07','2017_08','2017_09','2017_10','2017_11','2017_12','2018_01','2018_02','2018_03','2018_04','2018_05','2018_06')

def getCategoriesFromWardFile (fname):
    try:
        dt = json.load(open(fname))
    except:
        return None
    categories = set()
    for entry in dt:
        categories.add(entry['category'])
    return categories

allCategories=set()

for line in open('london_ward_ids_only.csv'):
    id = line.strip()
    for month in months:
        fname = 'london_month_'+month+'/crime_month_'+month+'_area_'+id+'_0.json'
    
    categories=getCategoriesFromWardFile(fname)
    if categories:
        allCategories.update(categories)


                    
