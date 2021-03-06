import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('loveSandwiches')


def get_sales_data():
    """
    get sales data from the user
    Run a while loop to collect a valid string of data from user
    via the terminal, a string of 6 numbers separated by commas.
    Loop will request data until valid data above is input,

    """

    while True:
        print('Please enter sales data from the last market.')
        print('Data should be six numbers, seperated by commas.')
        print('Example: 10, 20, 30, 40, 50, 60\n')

        data_str = input('Enter your data here:\n')
        
        sales_data = data_str.split(',')

        if validate_data(sales_data):
            print('Data is valid!')
            break
    
    return sales_data


def validate_data(values):
    """
    Inside the try, conversta all string values to integers
    Raises a ValueError if strings cannot be converted to integers
    or if there is not exactly six figures input.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 valued required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

"""
def update_surplus_worksheet(data):
    """
    update surpluss worksheet add new row with the list data provided
    """
    print('Updating surplus worksheet... \n')
    surplus_worksheet = SHEET.worksheet('SURPLUS')
    surplus_worksheet.append_row(data)
    print('Surplus worksheet updated successfully. \n')

        
def update_sales_worksheet(data):
    """
    update sales worksheet add new row with the list data provided
    """
    print('Updating sales worksheet... \n')
    sales_worksheet = SHEET.worksheet('SALES')
    sales_worksheet.append_row(data)
    print('Sales worksheet updated successfully. \n')

    """


def update_worksheet(data, worksheet):
    """
    receives a list of integers to be inserted into a worksheet
    update the relevant worksheet with the data provided
    """
    print(f'Updating {worksheet} worksheet...\n')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated successfully.\n')




def calculate_surplus_data(sales_row):
    """
    compare sales with stock + is waste - is sandwiches made that day
    """
    print('Calculating surplus data... \n')
    stock = SHEET.worksheet('STOCK').get_all_values()
    stock_row = stock[-1]


    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)


    return surplus_data 



def main():
    """
    run all program functions
    """

    data = get_sales_data()
    sales_data = [int(num) for num in data]
    update_worksheet(sales_data, 'SALES')
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data, 'SURPLUS')


print("Welcome to Love Salad Sanwiches Data Automation")
main()
