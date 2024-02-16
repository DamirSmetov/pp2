import datetime

x = datetime.datetime(2024, 5, 12, 13, 45, 30)
y = datetime.datetime(2024, 5, 12, 14, 45, 38 )
diff = x-y
print(abs(diff.total_seconds()))
