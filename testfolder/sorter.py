import pandas as pd 
import json as js
import time

############################### Completed and working ##########################################

# import data from csv file as a dataframe with selected columns

importtest = pd.read_csv('export.csv')

importtest['Date'] = importtest['Date']
importtest['Description'] = importtest['Description']
importtest['Debit'] = importtest['Debit'].fillna(0)
importtest['Credit'] = importtest['Credit'].fillna(0)

importtest["dolval"] = (importtest["Debit"] + importtest["Credit"])

print(importtest.head())

############################# Working on and tidying up ############################################

# import dictionary of keyword/category for expenses

with open('expensecategories.json') as json_file:
    expensecategories = js.load(json_file)
 
print(expensecategories)

with open('expensecategorieslist.json') as json_file:
    expensecategorieslist = js.load(json_file)
    
print(expensecategorieslist)

time.sleep(2)

# reset list and dictionary values to default for testing

expensecategories = {'testkey' : 'testvalue'}
expensecategorieslist = ["test1","test2"]


# Sort expenses using list for keyword detection, then dictionary for category assignment

def categorizer(expensecategories, expensecategorieslist, expense_name):
    expense_name = expense_name.lower()
    for item in expensecategorieslist:
        if item in expense_name.lower():
            return expensecategories[item]
        else:
            print(expensecategories)
            newcat = input(f"{expense_name} doesn't seem to contain any of the keywords. Is this a new category? y/n").lower()
            if newcat == 'y':
                newcategory = input("What's the new category?").lower()
                print(expense_name)
                newkeyword = input(f"What keyword in {expense_name} would you like to associate with this new category?").lower()
                while expense_name.find(newkeyword) == -1:
                    newkeyword = input(f"{newkeyword} was not found in {expense_name}. Please choose a keyword found in the expense description.")
                expensecategorieslist.append(newkeyword)
                expensecategories[newkeyword] = newcategory
                print("Adding new category and keyword...")
                time.sleep(2)
                return expensecategories[newkeyword]
            elif newcat == 'n':
                print(expensecategories)
                newkey = input("Would you like to create a new keyword to an existing category? Y/N").lower()
                if newkey == 'y':
                    print(expensecategories)    
                    newcategory = input("What category is the new keyword going to be associated with?").lower()
                    print(expense_name)
                    newkeyword = input(f"What keyword in {expense_name} would you like to associate with {newcategory}?").lower()
                    while expense_name.find(newkeyword) == -1:
                        newkeyword = input(f"{newkeyword} was not found in {expense_name}. Please choose a keyword found in the expense description.")
                    expensecategorieslist.append(newkeyword)
                    expensecategories[newkeyword] = newcategory
                    print("Adding new keyword to existing category...")
                    time.sleep(2)
                    return expensecategories[newkeyword]
                elif newkey == 'n':
                    print("no actions chosen") 
                else:
                    print("possible error")
            else:
                print("This appears to be an error. Please consult YOUR MOM'S ASS for further assistance.")           
                    
                
importtest['Category'] = importtest['Description'].apply(lambda x: categorizer(expensecategories,expensecategorieslist,x))

categoryvalues = importtest.groupby('Category')['dolval'].sum()

print(categoryvalues)
time.sleep(5)

# write new list and dictionary values to original json import file for future use

with open('expensecategories.json', 'w') as json_file:
    js.dump(expensecategories, json_file)

with open('expensecategorieslist.json', 'w') as json_file:
    js.dump(expensecategorieslist, json_file)

print(importtest)

# write dataframe to new sheet in pre-built testBudget.xlsx file

importtest2 = importtest.copy()
with pd.ExcelWriter('testBudget.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    importtest2.to_excel(writer, sheet_name='importtest')
    
with pd.ExcelWriter('testBudget.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    categoryvalues.to_excel(writer, sheet_name='categoryvalues')

######################### Working on later ###########################

# write category totals 

# secondary sheet containing amounts broken out by category

# rest of xlsx file sheets to update and reflect based on addition of importtest sheet

# script to archive csv file upon completion for recordkeeping 

