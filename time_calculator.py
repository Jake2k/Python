def add_time(start_time,added_time,day=""):
    day = day.capitalize()
    start_time = process_start_time(start_time)
    added_time, days = process_added_time(added_time)
    process_final_time(start_time, added_time, days,day)

def process_start_time(start_time):
    meridiem = ""
    if "PM" in start_time:
        meridiem = "PM"
    start_time = start_time.replace(":",".")
    start_time = start_time.replace("AM","")
    start_time = start_time.replace("PM","")
    if meridiem == "PM":
        start_time = float(start_time) + 12
    return start_time

def process_added_time(added_time):
    days = 0
    added_time = added_time.replace(":",".")
    added_time = added_time.strip()
    if float(added_time) > 24.00:
        days, added_time = divmod(float(added_time),24)
    return added_time, days

def process_final_time(start_time, added_time,days,day):
    more_days = 0
    final_time = float(start_time) + float(added_time)
    if float(final_time) > 24.00:
        more_days, final_time = divmod(float(final_time),24)
    if final_time > 12.59:
        final_time = final_time - 12
        meridiem = "PM"
    else:
        meridiem = "AM"     
    if str(final_time)[2]== "6":
        final_time = final_time + 0.4
        if meridiem == "PM" and final_time > 11.59:
            more_days += 1
            meridiem = "AM"
        elif meridiem == "AM" and final_time > 11.59:
            meridiem = "PM"
    if str(final_time)[3]== "6":
        final_time = final_time + 0.4
        if meridiem == "AM" and final_time > 11.59:
            meridiem = "PM"
        elif meridiem == "PM" and final_time > 11.59:
            more_days += 1
            meridiem = "AM"
    final_days = days + more_days
    final_days = int(final_days)
    if final_days == 0:
        print ("%.2f" % final_time, meridiem, day)
    if final_days == 1:
        print ("%.2f" % final_time, meridiem, "(next day)")
    if day != "" and final_days > 1:
        day = calculate_day(day,final_days)
        print ("%.2f" % final_time, meridiem, day, (f"({final_days} days later)"))
    if final_days > 2:
        print ("%.2f" % final_time, meridiem, day,(f"({final_days} days later)"))

def calculate_day(day,final_days):
    day_to_num = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday":3,
        "Thursday":4,
        "Friday":5,
        "Saturday":6,
        "Sunday":7
        }
    num_to_day = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
        }    
    day_value = day_to_num.get(day)
    day_value = final_days + day_value
    if day_value > 7:
        day_value = day_value % 7
    day = num_to_day.get(day_value)
    return day



##add_time("3:00 PM", "3:10")
#### Returns: 6:10 PM
##add_time("11:30 AM", "2:32", "Monday")
#### Returns: 2:02 PM, Monday
##add_time("11:43 AM", "00:20")
#### Returns: 12:03 PM
##add_time("10:10 PM", "3:30")
#### Returns: 1:40 AM (next day)
##add_time("11:43 PM", "24:20", "tueSday")
#### Returns: 12:03 AM, Thursday (2 days later)
##add_time("6:30 PM", "205:12")
#### Returns: 7:42 AM (9 days later)
