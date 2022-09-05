# AutoBudgeter

paste a monthly csv file of expenses into the folder, run py script, and have each expense categorized and summed to export to budget excel sheet for easy sorting and viewing of monthly budget status

## WORKING

- 'sorter.py' looks for CSV file named 'export.csv'

- reads file

- imports 'Debit' and 'Credit' columns

- creates 'dolval' column to consolidate 'Debit' and 'Credit' columns

- converts 'Debit' and 'Credit' columns into series

- sums values of 'Debit' and 'Credit' columns into 'DebitTotal' and 'CreditTotal' values (currently saves each as columns with the value repeating down as a series, working on getting it saved as a value in a single cell)

- converts dataframe into excel sheet, and saves into 'testBudget.xlsx' as new sheet appended to end

## WIP

- import dictionary of expense categories (food, entertainment, etc.) from 'expensecategories.json'
- sort through list of expenses in 'export.csv' assigning each line item a category from the json file using keywords in the description
- if no current keywords are found, prompt for addition of new keywork/category and append to 'expensecategories' dictionary
- sum the total of each category into a value that will be written to a cell when exporting dataframe into 'testBudget.xlsx' 
- overwrite the existing 'expensecategories.json' dictionary with the new appended one to be used on the next bankstatement csv import

## COMPLETED

### CCpayoffCalc.py

- 'CCpayoffCalc.py' imports CreditCard class from 'CC'

- on execution, asks prompts and makes 3 different calculations for pay off time and pay off amount 

## FUTURE PLANS

have each expense csv named and archived into subfolder after exporting into Budget excel sheet
have category sumtotal values saved in Monthly Expenses sheet for previous month when importing new month expenses for comparison 
have 'sorter.py' flag credit card payments in 'export.csv', recalculate, and update values for existing credit cards in 'testBudget.xlsx'
