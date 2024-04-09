# start_dt = datetime.date(2019, 2, 1)
# end_dt = datetime.date(2019, 3, 1)
# time_between_dates = end_dt - start_dt
# days_between_dates = time_between_dates.days
# random_number_of_days = random.randrange(days_between_dates)
# random_date = start_dt + datetime.timedelta(days=random_number_of_days)

# start_dt = datetime.date(2024, 1, 1)

import random
import datetime as dt



def get_random_date():
	start_dt = dt.date(2024, 1, 1)
	random_date = start_dt + dt.timedelta(days=random.randrange(90))
	random_date += dt.timedelta(hours=random.randrange(24), minutes=random.randrange(60))
	return random_date.isoformat().replace("T", " ")

def generate_order(reseller_id, count, start_id = 1):
	s = ""
	for i in range(start_id, start_id + count + 1):
		random_datetime = get_random_date()
		s += f"({i}, {reseller_id}, '{random_datetime}'),\n"
	return s