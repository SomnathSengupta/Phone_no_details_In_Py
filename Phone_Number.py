import phonenumbers
from phonenumbers import timezone, geocoder, carrier
number = input("Enter any phone no starting with +__ : ")
phone = phonenumbers.parse(number) #Country Code and National Number
time = timezone.time_zones_for_number(phone) #Time Zone
car = carrier.name_for_number(phone, "en") # Simcard name
reg = geocoder.description_for_number(phone, "en") # Country Name
print(phone)
print(time)
print(car)
print(reg)

'''
Enter any phone no starting with +__ : +919382101341
Country Code: 91 National Number: 9382101341
('Asia/Calcutta',)
Reliance Jio
India

'''