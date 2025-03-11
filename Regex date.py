import re
Gam=r"^[0-9]+/+[0-9]+/+[0-9]"
if re.fullmatch(Gam,"01/03/2024"):
    print("content valid")
else:
    print("invalid")    