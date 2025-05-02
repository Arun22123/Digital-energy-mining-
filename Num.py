from time import time
from number import number
import phonenumbers 
from phonenumbers import timezone,geocoder,carrier
number =input("917004755346: ")
phone =phonenumbers.parse(number)
time =timezone.time_zone_for_number(phone)
car =carrier.name_for_number(phone, "en")
reg =geocoder.descriptions_for_number(phone, "en")

print(phone)
print(time)
print(car)
print(reg)
