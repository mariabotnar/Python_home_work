is_year_leap = input('Введите год: ')
year = int(is_year_leap)
print(year)

def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

leap_year = is_year_leap(year)
print(f"Год {year}:{leap_year}")