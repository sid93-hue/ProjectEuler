"""Problem 19"""

# Monday = 0, ...., Sunday = 6

def is_leap(year):
    if year % 400 == 0 : return True
    if year % 100 == 0: return False
    if year % 4 == 0 : return True
    else : return False 

def is_Sunday(day_of_week):
    if day_of_week == 6 : return True
    else : return False

def get_num_sundays_on_first(year):
    num_days = 0 
    num_sundays = 0
    for i in range(0, year - 1900):
        if is_leap(i):
            num_days += 366
        else :
            num_days += 365
    starting_day = num_days % 7
    
    # 1 January
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 February
    starting_day += 31
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 March
    if is_leap(year):
        starting_day += 29
    else :
        starting_day += 28
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 April
    starting_day += 31
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 May
    starting_day += 30
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 June
    starting_day += 31
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 July
    starting_day += 30
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 August
    starting_day += 31
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 September
    starting_day += 31
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 October
    starting_day += 30
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 November
    starting_day += 31
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    # 1 December
    starting_day += 30
    starting_day = starting_day % 7
    if is_Sunday(starting_day) : num_sundays += 1

    return num_sundays


year = 1965
print(f"number of sundays falling on 1 in {year} is {get_num_sundays_on_first(year)}")

answer = 0
for year in range(1901, 2001):
    answer += get_num_sundays_on_first(year)

print(f"answer = {answer}")