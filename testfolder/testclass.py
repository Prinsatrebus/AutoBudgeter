

class Expense:
    
    def __init__(self, description, amount, category):
        self.description = description
        self.amount = float(amount)
        self.category = category
        
    def categorize(self):
        self.category = item.find(expensecategories.keys())
        