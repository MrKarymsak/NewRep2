from datetime import datetime


def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


year = 1991
month = 12
day = 20

name = "Olzhas"
date_of_birth = datetime(year, month, day)
age = calculate_age(date_of_birth)
ocupation = "Appliance tech and QA Engineering student"
intro = f"Hello! My name is {name}. I'm {age} years old. I'm an {ocupation}"

print(intro)