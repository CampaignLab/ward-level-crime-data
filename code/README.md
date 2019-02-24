## What is included in this repository:

--- DATA ---

FOLDER 2018-05 boundaries - this contains raw data in multiple JSON files extracted from https://data.police.uk using the API the data covers the period Jan-2016 to May-2018 (all analysis and additional files are based on this data)

CrimeByWard-LabourVoteChange.csv - aggregated crime count data by ward and year with percentage change in Labour vote between the 2014 and 2018 labour council elections

crimes_by_ward_by_month.csv - count of crimes in each ward in each month

LabourChangeByWard.csv - increase / decrease percentage of Labour vote share by ward comparing local elections in 2014 and 2018

--- CODE ---

Crime_and_labour_vote_change_total_processFEB19.ipynb - complete notebook for processing the raw json data into dataframes and doing correlation / regression analysis. Runtime ~ 5min

Have a look at the fork for the notebook which contains the API request script for creating the jsons from the police data site

## What was I looking for?

We were interested in looking for relationships between crime and
change in Labour vote share. For instances, there have been large
increases in violent crime in London over the last few years. Are
those areas more likely to vote Labour?

## What did I do?

We have crime data for each London ward on a monthly basis from Jan
2016 - June 2018. I looked at two variables across a number of categories.

* Rate of increase over the 2.5 years (through regression)
* Amount of crime on March 2018

The categories were
* theft-from-the-person
* bicycle-theft
* anti-social-behaviour
* vehicle-crime
* possession-of-weapons
* shoplifting
* drugs
* public-order
* criminal-damage-arson
* burglary
* other-crime
* robbery
* other-theft
* violent-crime

I looked for correlations between these variables and the pct change
of the labour vote share.

Two files...
generateCrimeIncreaseForWard.py - goes through the .json files which contain the crime data and generates a file based on the category containing increases or amounts

import generateCrimeIncreaseForWard
generateCrimeIncreaseForWard.generateCrimeIncreases(category)
generateCrimeIncreaseForWard.generateCrimeAmounts(category)

import runCorrelation
runCorrelation.getCorrelation (regime)
the regime is either 'rates' or 'amounts'

## What did I find?

I did not find any significant correlations between any of the
categories and the pct change of the labour vote share. 
