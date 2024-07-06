import csv
import locale
locale.setlocale(locale.LC_ALL, 'C')

class Expense:
    dept_name: str
    expense_amount: float

    def __init__(self, dept_name, expense_amount):
        self.dept_name = dept_name
        self.expense_amount = expense_amount


def read_file(file_path):
    expense_list = []
    with open(file_path) as file:
        reader = csv.reader(file, delimiter=",")
        #skip reader
        next(reader)
        for row in reader:
            expense = Expense(row[0], row[3])
            expense_list.append(expense)
    return expense_list


def get_expense_dict(expense_list):
    expense_dict = {}
    for item in expense_list:
        if item.expense_amount == '':
            continue
        temp_exp_amount = int(item.expense_amount)
        # if key not in dictonary so first occurance of the dept
        if item.dept_name not in expense_dict:
            expense_dict[item.dept_name] = [temp_exp_amount]
        else:
            expense_dict[item.dept_name].append(temp_exp_amount)
    return expense_dict


def dispaly_expenses(expense_dict):
    for department, expenses in expense_dict.items():
        total_expense = sum(expenses)
        print(f"Department: {department} spent: ${total_expense:,.2f}")


# Main execution
file_path = "city-of-seattle-2012-expenditures-dollars.csv"
expense_list = read_file(file_path)
expense_dict = get_expense_dict(expense_list)
dispaly_expenses(expense_dict)
