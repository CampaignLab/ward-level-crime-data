import csv
import numpy as np
import scipy.stats

def getCorrelation (category,regime='rates'):

    votein = csv.reader(open('wardIDToVote.csv'))
    next(votein)

    votes = dict()
    for row in votein:
        if len(row[3]):
            votes[row[0]] = float(row[3])

    crimein = csv.reader(open('ward_'+regime+'_'+category+'.csv'))
    next(crimein)

    crimes = dict()
    for row in crimein:
        crimes[row[0]] = float(row[1])

    wards=set(crimes.keys()).intersection(set(votes.keys()))

    data = list()

    for ward in wards:
        data.append((crimes[ward],votes[ward]))

    adata = np.array(data)
    print (category,scipy.stats.pearsonr(adata[:,0],adata[:,1]))
    return adata

