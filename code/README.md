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
