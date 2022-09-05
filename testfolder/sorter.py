import pandas as pd 
import json as js
import time

############################### Completed and working ##########################################

importtest = pd.read_csv('testfolder/export.csv')

importtest['Debit'] = importtest['Debit'].fillna(0)
importtest['Credit'] = importtest['Credit'].fillna(0)

importtest["dolval"] = (importtest["Debit"] + importtest["Credit"])
DebitTotalSeries = pd.Series(importtest["Debit"])
importtest["DebitTotal"] = (DebitTotalSeries.sum())
CreditTotalSeries = pd.Series(importtest["Credit"])
importtest["CreditTotal"] = (CreditTotalSeries.sum())

print(importtest.head())

importtest2 = importtest.copy()
with pd.ExcelWriter('testfolder/testBudget.xlsx', engine='openpyxl', mode='a') as writer:
    importtest2.to_excel(writer, sheet_name='importtest')

############################ Working on and tidying up ############################################

# import dictionary of keyword/category for expenses

with open('testfolder/expensecategories.json') as json_file:
    expensecategories = js.load(json_file)
 
print(expensecategories)

time.sleep(2)

expensecategories = {'test2' : 'value2'}

########################  Need HAALELPPP !!11!!!1  #####################################

# Sort expenses into dictionaries of name and dolval

for x in importtest['Description']:
    if x in expensecategories:
        pass

expenses = [item for item in importtest['Description'] if item in list(expensecategories.keys())]

dict_you_want = { your_key: old_dict[your_key] for your_key in your_keys }
expenses = {key: importtest['Description'][key] for key in list(expensecategories.keys())}
        
    # If expense doesn't contain existing category keyword, prompt for addition of new item in category dictionary

######################## Working on later ####################

# Create category float dolval sumtotal counters

# write category totals 

# export modified category dictionary to original import file 
  
with open('testfolder/expensecategories.json', 'w') as export_file:
    js.dump(expensecategories, export_file)
