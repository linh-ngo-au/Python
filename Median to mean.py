# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 14:11:16 2022

@author: Linh
"""

# Import packages

import pandas as pd
import numpy as np
import math

# Define functions

def mean_convert(author, outcome, q2, q1, q3, a, b, s):
    if q1>0:
        mean=round((q1+q2+q3)/3, 1)
        sd=round((q3-q1)/1.35, 1)
    else:
        mean=round((a+2*q2+b)/4, 1)
        if s<=15:
            sd=round(1/math.sqrt(12)*math.sqrt(((b-a)**2 +(a-2*q2+b)**2/4)), 1)
        elif s<=70:
            sd=round((b-a)/4, 1)
        else:
            sd=round((b-a)/6, 1)
    result=[author, outcome, mean, sd]
    print(result)
    return result

data=pd.DataFrame(columns=['Author, year', 'Outcome', 'Mean', 'SD'])

def mean_combined (author, outcome, x_mean, x_sd, x_s, y_mean, y_sd, y_s):
    mean = round((x_mean*x_s + y_mean*y_s)/(x_s+y_s), 1)
    q1=(x_s-1)*x_sd*x_sd + x_s*x_mean*x_mean 
    q2=(y_s-1)*y_sd*y_sd + y_s*y_mean*y_mean
    qc=q1+q2
    sd=round(math.sqrt((qc-(x_s+y_s)*mean*mean)/(x_s+y_s-1)), 1)
    result =[author, outcome, mean, sd]
    print(result)
    return result
    
# Execute the functions

data.loc[len(data.index)] = mean_convert('Metzner 2010', 'AF duration', 5, 4, 9, 0, 0, 32)

data.loc[len(data.index)] = mean_convert('Metzner 2010', 'LAD', 43, 38, 46, 0, 0, 32)

data.loc[len(data.index)]=mean_convert('Metzner, 2010', 'Follow-up time', 1400/365.25, 930/365.25, 1568/365.25, 0, 0, 32)

data.loc[len(data.index)] = mean_convert('Ouyang 2010', 'Follow-up time', 4.8, 0.33, 5.5, 0, 0, 161)

data.loc[len(data.index)] = mean_combined('Tayebjee 2010', 'Age', 56, 10, 277, 60, 10, 142)

data.loc[len(data.index)] = mean_combined('Tayebjee 2010', 'AF duration', 56/12, 38/12, 277, 63/12, 49/12, 142)

data.loc[len(data.index)] = mean_combined('Tayebjee 2010', 'LAD', 38, 9, 277, 42, 10, 142)

data.loc[len(data.index)] = mean_convert('Tayebjee 2010', 'Follow-up time', 1.7, 0.9, 5.0, 0, 0, 419)

data.loc[len(data.index)] = mean_convert('Weerasooriya 2011', 'Follow-up', 60/12, 56/12, 62/12, 0, 0, 100)

data.loc[len(data.index)] = mean_combined('Machino 2012', 'AF duration', 5, 3, 16, 6, 6, 321)

data.loc[len(data.index)] = mean_combined('Machino 2012', 'EF', 64, 8, 16, 65, 10, 321)

data.loc[len(data.index)] = mean_combined('Machino 2012', 'LAD', 40, 6, 16, 40, 7, 321)

data.loc[len(data.index)] = mean_convert('Sorgente 2012', 'Follow-up', 6, 4.88, 7.27, 0, 0, 103)

data.loc[len(data.index)] = mean_combined('Yagishita 2011', 'LVEF', 64.5, 9.8, 429, 64.5, 8.5, 95)

data.loc[len(data.index)] = mean_combined('Yagishita 2011', 'LAD', 39.5, 6.0, 429, 40.0, 7.1, 95)

data.loc[len(data.index)] = mean_combined('Lin 2012', 'Age', 56.7, 9.3, 85, 55.2, 9.4, 45)

data.loc[len(data.index)] = mean_combined('Lin 2012', 'LVEF', 56.0, 10.5, 85, 59.3, 9.6, 45)

data.loc[len(data.index)] = mean_combined('Lin 2012', 'LAD', 47, 6, 85, 47, 7, 45)

print('Lin 2012, HBP is', round(50.1*85/100,0) + round(66.7*45/100,0))

print('Lin 2012, HF is', round(8.2*85/100, 0) + round(13.3*45/100, 0))

print('Lin 2012, CAD is', round(25.9*85/100,0) +round(22.2*45/100,0))

data.loc[len(data.index)] = mean_combined('Lin 2012', 'AF duration', 5.1, 4.8, 85, 6.7, 5.8, 45)

data.loc[len(data.index)] = mean_convert('Tilz 2012', 'Follow-up', 56/12, 0, 0, 49/12, 67/12, 202)

data.loc[len(data.index)] = mean_convert('Zhou 2013', 'AF duration', 53/12, 16/12, 100/12, 0, 0, 200)

data.loc[len(data.index)] = mean_convert('Zhou 2013', 'LVEF', 64, 60, 67, 0, 0, 200)

print('Number of men in study by Bertaglia 2010 is', round(74.6*177/100,0))

print('Bertaglia 2010, PAF', round(57.6*177/100, 0))

print('Bertaglia 2010, Hypertension is', round(31.7/100*177, 0))

print('Bertaglia 2010, DCM is', round(5.5*177/100,0))

print('Bertaglia 2010, IHD is', round(3.5*177/100,0))

print('Hunter 2010, Heart journal, Male is', round(75/100*285,0))

print('Hunter 2010, Heart journal, hypertension', round(37/100*285,0))

print('Hunter 2010, Heart journal, prior stroke is', round(5/100*285,0))

data.loc[len(data.index)] = mean_convert('Hunter 2010, Heart', 'Follow-up time', 3.3, 2.4, 7.5, 0, 0, 285)

print('Hunter 2010, Europace, Male', round(73/100*350, 0))

print('Hunter 2010, Europace, hypertension is', round(31/100*350,0))

print('Hunter 2010, Europace, prior stroke is', round(5/100*350,0))

data.loc[len(data.index)] = mean_convert('Hunter 2010, Europace', 'Follow-up', 3.1, 2.0, 7.5, 0, 0, 335)

data.loc[len(data.index)] = mean_combined('Klemm 2010', 'Age', 63, 7, 102, 62, 8, 102)

data.loc[len(data.index)] = mean_combined('Klemm 2010', 'LAD', 44, 6, 102, 45, 7, 102)

data.loc[len(data.index)] = mean_convert('Klemm 2010', 'Follow-up time', 2.1, 0, 0, 0.3, 6.3, 204)

data.loc[len(data.index)] = mean_convert('Daly 2011', 'Age', 51, 0, 0, 24, 71, 187)

data.loc[len(data.index)] = mean_convert('Daly 2011', 'LAD', 44, 0, 0, 24, 64, 187)

data.loc[len(data.index)] = mean_convert('Daly 2011', 'Follow-up time', 33/12, 0, 0, 6/12, 72/12, 187)

data.loc[len(data.index)] = mean_combined('Chang 2012', 'AF duration', 4, 5, 37, 4, 3, 31)

data.loc[len(data.index)] = mean_combined('Chang 2012', 'LVEF', 61, 8, 37, 60, 7, 31)

data.loc[len(data.index)] = mean_combined('Change 2012', 'LAD', 36, 5, 37, 38, 4, 31)

data.loc[len(data.index)] = mean_combined('Chao 2012', 'Age', 51.4, 9.6, 63, 54.5, 12.3, 25)

data.loc[len(data.index)] = mean_combined('Chao 2012', 'LVEF', 53, 9.9, 63, 55.1, 10.6, 25)

data.loc[len(data.index)] = mean_combined('Chao 2012', 'LAD', 45.6, 6.3, 63, 42.1, 7.0, 25)

data.loc[len(data.index)] = mean_convert('Hunter 2012', 'AF duration', 36/12, 24/12, 70/12, 0, 0, 1273)

data.loc[len(data.index)] = mean_convert('Hunter 2012', 'Follow-up, index procedure', 3.1, 1.0, 9.6, 0, 0, 1273)

data.loc[len(data.index)] = mean_convert('Anselmino', 'AF duration', 9/12, 6/12, 73/12, 0, 0, 196)

data.loc[len(data.index)] = mean_convert('Anselmino 2013', 'Follow-up time, index', 26.5/12, 9.7/12, 52.2/12, 0, 0, 1990)

data.loc[len(data.index)] = mean_convert('Hu 2014', 'Follow-up time', 51/12, 41/12, 56/12, 0, 0, 227)

data.loc[len(data.index)] = mean_convert('Lin 2014', 'Follow-up time', 43/12, 16/12, 108/12, 0, 0, 743)

data.loc[len(data.index)] = mean_convert('Fiala 2015', 'AF duration', 60/12, 34/12, 96/12, 0, 0, 203)

data.loc[len(data.index)] = mean_convert('Fiala 2015', 'Follow-up time', 48/12, 30/12, 60/12, 6/12, 80/12, 203)

data.loc[len(data.index)] = mean_convert('Gal 2015', 'Follow-up time', 5.5, 4.3, 6.1, 0, 0, 28)

data.loc[len(data.index)] = mean_convert('Karasoy 2015', 'Age', 59.5, 52.9, 65.2, 0, 0, 4050)

data.loc[len(data.index)] = mean_convert('Karasoy 2015', 'AF duration', 3.0, 1.2, 6.5, 0, 0, 4050)

data.loc[len(data.index)] = mean_convert('Karasoy 2015', 'Follow-up time', 3.4, 2.0, 5.6, 0, 0, 4050)

data.loc[len(data.index)] = mean_convert('Scherr 2015', 'AF duration', 60/12, 36/12, 120/12, 0, 0, 150)

data.loc[len(data.index)] = mean_convert('Scherr 2015', 'Follow-up time', 58/12, 43/12, 73/12, 0, 0, 150)

data.loc[len(data.index)] = mean_convert('Zhao 2015', 'AF duration', 24/12, 7/12, 120/12, 0, 0, 49)

data.loc[len(data.index)] = mean_convert('Zhao 2015', 'Follow-up time', 45/12, 36/12, 64/12, 0, 0, 49)

data.loc[len(data.index)] = mean_convert('Davies 2016', 'Follow-up', 33/12, 0, 0, 24/12, 63/12, 40)

data.loc[len(data.index)] = mean_combined('Roh 2016', 'Follow-up time', 45/12, 31/12, 18, 58/12, 39/12, 13)

data.loc[len(data.index)] = mean_convert('Zhao 2016', 'Follow-up time', 40/12, 24/12, 70/12, 0, 0, 89)

data.loc[len(data.index)] = mean_combined('Zhao 2016', 'Age', 47.6, 8.3, 395, 59.3, 10.8, 263)

data.loc[len(data.index)] = mean_combined('Zhao 2016', 'AF duration', 6.5, 1.7, 395, 15.7, 4.6, 263)

data.loc[len(data.index)] = mean_combined('Zhao 2016', 'LVEF', 56.1, 5.7, 395, 52.9, 7.8, 263)

data.loc[len(data.index)] = mean_combined('Zhao 2016', 'LAD', 31.5, 4.1, 395, 39.8, 6.6, 263)

data.loc[len(data.index)] = mean_convert('Bertaglia 2017', 'AF duration', 5, 2, 10, 0, 0, 137)

data.loc[len(data.index)] = mean_convert('Bertaglia 2017', 'LVEF', 60, 55, 65, 0, 0, 137)

data.loc[len(data.index)] = mean_convert('Brooks 2018', 'AF duration', 8, 5, 12, 0, 0, 174)

data.loc[len(data.index)] = mean_convert('Brooks 2018', 'Follow-up time', 89/12, 63/12, 89/12, 0, 0, 174)

data.loc[len(data.index)] = mean_combined('Chen 2019', 'Age', 65, 9, 62, 66, 7, 124)

data.loc[len(data.index)] = mean_convert('Chen 2019', 'AF duration', 12/12, 3/12, 36/12, 0, 0, 62)

data.loc[len(data.index)] = mean_convert('Chen 2019', 'AF duration', 12/12, 5/12, 45/12, 0, 0, 124)

data.loc[len(data.index)] = mean_combined('Chen 2019', 'AF duration', 1.4, 2.0, 62, 1.7, 2.5, 124)

data.loc[len(data.index)] = mean_convert('Chen 2019', 'LVEF, RHD group', 60, 58, 64, 0, 0, 62)

data.loc[len(data.index)] = mean_convert('Chen 2019', 'LVEF, control group', 62, 58, 65, 0, 0, 124)


data.loc[len(data.index)] = mean_combined('Chen 2019', 'LVEF, combined', 60.7, 4.4, 62, 61.7, 5.2, 124)


data.loc[len(data.index)] = mean_convert('Chen 2019', 'LAD, RHD group', 49, 45, 52, 0, 0, 62)

data.loc[len(data.index)] = mean_convert('Chen 2019', 'LAD, control group', 43, 38, 47, 0, 0, 124)

data.loc[len(data.index)] = mean_combined('Chen 2019', 'LAD, combined', 48.7, 5.2, 62, 42.7, 6.7, 124)

data.loc[len(data.index)] = mean_convert('Chen 2019', 'Follow-up time, RHD group', 65/12, 23/12, 140/12, 0, 0, 62)

data.loc[len(data.index)] = mean_convert('Chen 2019', 'Follow-up time, control', 64/12, 24/12, 140/12, 0, 0, 124)

data.loc[len(data.index)] = mean_combined('Chen 2019', 'Follow-up time, combined', 6.3, 7.2, 62, 6.3, 7.2, 124)

data.loc[len(data.index)] = mean_convert('Chen 2019, young', 'AF duration', 18/12, 7/12, 36/12, 0, 0, 75)

data.loc[len(data.index)] = mean_convert('Chen 2019, young', 'Follow-up', 61/12, 5/12, 102/12, 0, 0, 75)

data.loc[len(data.index)] = mean_convert('Packer 2019', 'Age', 68, 62, 72, 0, 0, 1108)

data.loc[len(data.index)] = mean_convert('Packer 2019', 'AF duration', 1.1, 0.3, 4.1, 0, 0, 1108)

data.loc[len(data.index)] = mean_convert('Packer 2019', 'Follow-up time', 48.5/12, 29.9/12, 62.1/12, 0, 0, 1108)






















# Export dataframe to excel file

data.to_excel("CAAF review.xlsx", sheet_name="Mean")