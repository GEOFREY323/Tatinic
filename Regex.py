import re
Geofrey=r"^(UBa|UBA)\d{2}[a-z]{1,2}\d{2,4}$"
if re.fullmatch(Geofrey,"UBA24E6366"):
    print("content valid")
else:
    print("invalid")    