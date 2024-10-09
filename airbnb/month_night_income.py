import json
from datetime import datetime

# Read the JSON file
with open('airbnb/bookinghistory.json', 'r') as file:
    booking_data = json.load(file)

# Access the 'data' field
bookings = booking_data['data']

# Print some information about the bookings
print(f"Total number of bookings: {len(bookings)}")

total_income = sum(booking['income'] for booking in bookings)
print(f"\nTotal income from all bookings: ${total_income:.2f}")

month_info = {}
for booking in bookings:
    checkin_datetime = datetime.strptime(booking['checkin'], "%Y-%m-%d %H:%M:%S")
    year_month = checkin_datetime.strftime("%Y-%m")
    if year_month not in month_info:
        month_info[year_month] = []
    month_info[year_month].append({
        "days": int(booking['days']), 
        "income": float(booking['income']),
        "number_of_guests": int(booking['number_of_guests'])
    }) 
month_summary = {}# map of month to month summary(days, income, number_of_guests)
for month in month_info:
    if month not in month_summary:
        month_summary[month] = {
            "days": 0,
            "income": 0,
            "number_of_guests": 0
        }
    for day in month_info[month]:
        month_summary[month]["days"] += day["days"]
        month_summary[month]["income"] += day["income"]
        month_summary[month]["number_of_guests"] += day["number_of_guests"]


for key, inner_map in month_summary.items():
    inner_map['income'] = round(inner_map['income'], 2)
    inner_map['average_night_rate'] = round(inner_map['income'] / inner_map['days'], 2)
month_summary_list = list(month_summary.items())
month_summary_list.sort(key=lambda x: x[0])
for month in month_summary_list:
    print(f"{month[0]}: {month[1]}")

year_summary = {}
for month in month_summary:
    year = month.split('-')[0]
    if year not in year_summary:
        year_summary[year] = {
            "days": 0,
            "income": 0,
            "number_of_guests": 0
        }
    year_summary[year]["days"] += month_summary[month]["days"]
    year_summary[year]["income"] += month_summary[month]["income"]
    year_summary[year]["number_of_guests"] += month_summary[month]["number_of_guests"]

for key, inner_map in year_summary.items():
    inner_map['income'] = round(inner_map['income'], 2)
    inner_map['average_night_rate'] = round(inner_map['income'] / inner_map['days'], 2)
print(year_summary)