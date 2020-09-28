time=str(input("Please enter time in a 24 hour format hh:mm:ss:"))
hour=int(time[0]+time[1])
minutes=int(time[3]+time[4])
seconds=int(time[6]+time[7])

seconds=seconds+1
if seconds==60:
    seconds=00
    minutes=minutes+1
    if minutes==60:
        minutes=00
        hour=hour+1
        if hour==24:
            hour=0
print(hour,":", minutes, ":",seconds)
            
