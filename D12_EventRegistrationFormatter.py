from datetime import datetime

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
event_name = input("Enter event name: ").strip()
year = input("Enter event year: ").strip()
month = input("Enter event month: ").strip()
day = input("Enter event day: ").strip()

full_name = f"{first_name} {last_name}".title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_event = event_name.title()

if month.isdigit():
    date_obj = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
else:
    date_obj = datetime.strptime(f"{year}-{month.title()}-{day}", "%Y-%B-%d")

formatted_date = f"{date_obj.strftime('%B')} {date_obj.day}, {date_obj.year}"

print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Event:", formatted_event)
print("Event Date:", formatted_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("\nRegistration record created successfully.")
