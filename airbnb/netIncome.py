import json

json_String= '''
{
    "code": 0,
    "msg": "success",
    "data": [
        {
            "id": 342,
            "userid": 435,
            "housenum": "TO5V1097",
            "checkintime": "2024-04-02",
            "checkinnum": "TO5V1097-Apr-2024",
            "mgfee": 221.02,
            "useincome": 1176.05,
            "uptime": "2024-05-31",
            "sender": "Administrator",
            "paystate": "2",
            "airbnb": 1397.07,
            "booking": 0.00,
            "expedia": 0.00,
            "vrbo": 0.00
        },
        {
            "id": 362,
            "userid": 435,
            "housenum": "TO5V1097",
            "checkintime": "2024-05-02",
            "checkinnum": "TO5V1097-May-2024",
            "mgfee": 946.77,
            "useincome": 5037.89,
            "uptime": "2024-06-30",
            "sender": "Administrator",
            "paystate": "2",
            "airbnb": 5984.66,
            "booking": 0.00,
            "expedia": 0.00,
            "vrbo": 0.00
        },
        {
            "id": 387,
            "userid": 435,
            "housenum": "TO5V1097",
            "checkintime": "2024-06-02",
            "checkinnum": "TO5V1097-Jun-2024",
            "mgfee": 965.43,
            "useincome": 5137.16,
            "uptime": "2024-07-31",
            "sender": "Administrator",
            "paystate": "2",
            "airbnb": 6102.59,
            "booking": 0.00,
            "expedia": 0.00,
            "vrbo": 0.00
        },
        {
            "id": 404,
            "userid": 435,
            "housenum": "TO5V1097",
            "checkintime": "2024-07-02",
            "checkinnum": "TO5V1097-Jul-2024",
            "mgfee": 1343.83,
            "useincome": 7150.66,
            "uptime": "2024-08-30",
            "sender": "Administrator",
            "paystate": "2",
            "airbnb": 8494.49,
            "booking": 0.00,
            "expedia": 0.00,
            "vrbo": 0.00
        },
        {
            "id": 427,
            "userid": 435,
            "housenum": "TO5V1097",
            "checkintime": "2024-08-02",
            "checkinnum": "TO5V1097-Aug-2024",
            "mgfee": 1468.30,
            "useincome": 7812.95,
            "uptime": "2024-09-30",
            "sender": "Administrator",
            "paystate": "2",
            "airbnb": 9281.25,
            "booking": 0.00,
            "expedia": 0.00,
            "vrbo": 0.00
        }
    ],
    "count": 0
}'''

parsed_json = json.loads(json_String)
data = parsed_json.get("data", [])

all_months = []
net_months = []

for month in data:
    month_str = month["checkintime"].split("-")[1]
    airbnb = float(month["airbnb"])
    useincome = float( month["useincome"])
    mgfee = float(month["mgfee"])
    # airbnb - mgfee = useincome
    all_months.append((month_str, month["airbnb"],  month["mgfee"]))
    net_months.append((month_str, useincome))

print(f"month, airbnb, mgfee: {all_months}")

print(f"month, useincome: {net_months}")

print(f"total useincome: {round(sum(x[1] for x in net_months),2)}")

