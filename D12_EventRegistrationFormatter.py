first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
event_name = input("Enter event name: ")
year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

full_name = first_name + " " + last_name
event_date = month + "/" + day + "/" + year

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", full_name)
print("Section:", section)
print("Event:", event_name)
print("Event Date:", event_date)
print("Language Used: Python")
print("String Feature Used: None")
print("Date/Time Feature Used: None")
print("\nRegistration record created successfully.")