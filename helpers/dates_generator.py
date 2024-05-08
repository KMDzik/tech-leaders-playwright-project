from datetime import datetime, timedelta

today = datetime.now().date()

departure_date = today + timedelta(days=7)
departure_day = departure_date.day
departure_month = departure_date.month
departure_year = departure_date.year

return_date = departure_date + timedelta(days=14)
return_day = return_date.day
