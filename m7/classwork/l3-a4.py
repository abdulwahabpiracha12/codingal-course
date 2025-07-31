import datetime
import calendar

# Get current time and manually adjust for Pakistan (UTC+5)
current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5)

print("Time now in Pakistan is:", current_time)
print("\n", calendar.calendar(2025))