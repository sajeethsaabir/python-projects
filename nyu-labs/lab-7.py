print("Please enter the day the call began")
day = input("Mon/Tue/Wed/Thu/Fri/Sat/Sun: ").lower()

print("Enter the time the call started")
time = int(input("24h format, hhmm: "))

print("Enter the call duration")
dur = int(input("In minutes: "))

if day in ['mon', 'tue', 'wed', 'thu', 'fri']:
    if (time <= 2400 and time > 1800) or (time < 800 and time >= 0):
        bill = dur * 0.25
        print("The cost for the call is ", bill, "$", sep="")
    elif (time >= 800 and time <= 1800):
        bill = dur * 0.40
        print("The cost for the call is ", bill, "$", sep="")

else:
    bill = dur * 0.15
    print("The cost for the call is ", bill, "$", sep="")
