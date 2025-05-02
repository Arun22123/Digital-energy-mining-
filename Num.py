import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Prompt the user for a phone number with a clear message
user_input = input("Enter a phone number with country code (e.g., +917004755346): ")

try:
    # Parse the phone number
    phone = phonenumbers.parse(user_input)

    # Validate the phone number
    if not phonenumbers.is_valid_number(phone):
        print("The phone number is not valid. Please try again.")
    else:
        # Get timezone, carrier, and region information
        phone_timezone = timezone.time_zones_for_number(phone)
        phone_carrier = carrier.name_for_number(phone, "en")
        phone_region = geocoder.description_for_number(phone, "en")

        # Print the details
        print(f"Phone Number: {phone}")
        print(f"Timezone(s): {phone_timezone}")
        print(f"Carrier: {phone_carrier}")
        print(f"Region: {phone_region}")

except phonenumbers.NumberParseException as e:
    print(f"Error parsing the phone number: {e}")
