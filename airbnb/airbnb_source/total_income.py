import json
import os
from datetime import datetime

file_names = ['2024-04', '2024-05', '2024-06', '2024-07', '2024-08']
# file_names = ['2024-04', '2024-05', '2024-06', '2024-07', '2024-08', '2024-09']
month_income = {}
for file_name in file_names:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)
    with open(file_path, 'r') as file:
        booking_data = json.load(file)

    booking_data = booking_data['data']['patek']['getAdditionalReservationData']['reservationResources']

    total_income = 0
    for booking in booking_data:
        total_income += (float(booking['hostPayoutFormatted'].replace('$', '').replace(',', '')) - 94) # cleaning fee

    print(f"Total income for {file_name}: ${total_income:.2f}")
    month_income[file_name] = round(total_income, 2)

print(month_income)
total_income = sum(month_income.values())
net_income = total_income * (1 - 0.14 * 1.13)
print(f"net income: ${net_income:.2f}")
