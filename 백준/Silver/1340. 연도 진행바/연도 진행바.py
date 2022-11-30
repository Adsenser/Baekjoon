# 함수 선언 파트

hour_minute = 60
day_minute = hour_minute*24

def yun_year_detect(year):
    if year % 4 ==0:
        if year%400 == 0:
            return True
            #윤년임
        elif year%100 == 0:
            return False
            #윤년 아님
        else:
            return True
            #윤년임

def yun_year_month(month):

    month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    global total_minute
    total_minute = 0
    for i in month_list:
        total_minute += i*day_minute
    global current_month_minute
    current_month_minute = 0
    for j in range(month_detect(month)-1):
        current_month_minute += (month_list[j])*day_minute

def non_yun_year_month(month):

    month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    global total_minute
    total_minute = 0
    for i in month_list:
        total_minute += i * day_minute
    global current_month_minute
    current_month_minute = 0
    for j in range(month_detect(month)-1):
        current_month_minute += (month_list[j]) * day_minute

def month_detect(input_month):
    if input_month == 'January':
        return 1
    elif input_month == 'February':
        return 2
    elif input_month == 'March':
        return 3
    elif input_month == 'April':
        return 4
    elif input_month == 'May':
        return 5
    elif input_month == 'June':
        return 6
    elif input_month == 'July':
        return 7
    elif input_month == 'August':
        return 8
    elif input_month == 'September':
        return 9
    elif input_month == 'October':
        return 10
    elif input_month == 'November':
        return 11
    elif input_month == 'December':
        return 12

def time_count(hour,minute):
    global current_time_minute
    current_time_minute = int((hour*hour_minute)+minute)

def day_count(day):
    global current_day_minute
    current_day_minute = int((day-1)*day_minute)

# 값 입력 파트

month, day, year, time = input().split()
if yun_year_detect(int(year)) == True:
    yun_year_month(month)
else:
    non_yun_year_month(month)

#입력받은 문자열에서 기호 제거
real_day = (day.split(','))[0]
real_hour = (time.split(':'))[0]
real_minute = (time.split(':'))[1]

# 나머지 함수에 삽입
time_count(int(real_hour),int(real_minute))
day_count(int(real_day))

#결과
result = (current_month_minute + current_time_minute + current_day_minute )*100 / total_minute
print(result)