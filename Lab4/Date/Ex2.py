import datetime

current_date = datetime.datetime.now()
yesterday = current_date - datetime.timedelta(days=1)
tomorrow = current_date + datetime.timedelta(days=1)
print("Yesterday: ", yesterday.strftime("%Y-%m-%d"))
print("Today: ", current_date.strftime("%Y-%m-%d"))
print("Tomorrow: ", tomorrow.strftime("%Y-$m-%d"))

