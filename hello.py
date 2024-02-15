import datetime

print("Good")
if datetime.datetime.now().strftime("%H:%M:%S") == "00:00:00":
    print("Midnight!")
else:
    print("Daytime!")