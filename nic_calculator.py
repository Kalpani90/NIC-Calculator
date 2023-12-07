import datetime

# Function for validating user input
def validate (nic: str)-> bool:
    nic_length = len(nic)
    if nic_length !=12 :
        return False
    else:
        nic_digit = nic.isdigit()
        return nic_digit
    
# Function for identifying born year
def get_born_year(nic:str)-> int:
    year = nic[0:4]
    return int(year)

# Get born date
def get_born_date(nic: str) -> datetime.date:
    born_day = int(nic[4:7])
    if born_day > 500:
        born_day = born_day - 500
    year = get_born_year(nic)
    jan_first = datetime.date(year,1,1)
    born_date = jan_first + datetime.timedelta(days= born_day -1)
    return born_date


           
