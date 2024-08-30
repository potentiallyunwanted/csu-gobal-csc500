# Instructions
# Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight). 
# If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm). 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours) and 
# then ask for the number of hours to wait for the alarm. 
# Your program should output what the time will be on a 24-hour clock when the alarm goes off.

'''
Sudo code:
1. ask the time in hours
2. ask the number of hours to wait for the alarm
3. add the current time and the alarm time mod 24 to get the remainder which will always be the time
4. return the time in 12 hour format
5. if the time is greater than 12, subtract 12
6. if the time is 0, set it to 12
7. if the time is greater than 12, return the time with PM
8. else return the time with AM
'''

def to_12(time):
    after_12 = False
    if time > 12:
        time -= 12
        after_12 = True
    if time == 0:
        time = 12
    if after_12:
        return f"{time} o'clock PM"
    else:
        return f"{time} o'clock AM"

def main():
    current_time = int(input("Enter the current time (in hours): "))
    alarm_time = int(input("Enter the number of hours to wait for the alarm: "))
    alarm_time = (current_time + alarm_time) % 24
    alarm_time = to_12(alarm_time)
    print(f"The alarm will go off at {alarm_time} o'clock")
    
if __name__ == "__main__":
    main()