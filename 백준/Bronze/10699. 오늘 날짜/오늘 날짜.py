from datetime import datetime
from datetime import timedelta

logdate = (datetime.today()) + timedelta(hours=9)
print(str(logdate).split()[0])