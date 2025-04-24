# Implement a program that converts a given number of minutes into hours and minutes

minutes = int(input("Enter the total minutes: "))

hours = minutes // 60
remained_minutes = minutes % 60

print(f"{minutes} minutes is equal to:")
print(f"Hours   : {hours}")
print(f"Minutes : {remained_minutes}")
