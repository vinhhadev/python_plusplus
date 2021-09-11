from datetime import date
year_born = int(input('Nhập năm sinh của bạn: '))
today = date.today()
this_year = today.year
year_old = this_year - year_born
print(f'Tuổi của bạn: {year_old}')