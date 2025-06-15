import pywhatkit as kit

# Recipient's phone number (include country code, e.g., +91 for India)
phone_number = "+918167756291"

# Message to be sent
message = "Hello! This is an automated message sent using Python."

# Send the message instantly (without delay)
kit.sendwhatmsg_instantly(phone_number, message, wait_time=30)  # wait_time in seconds

print("Message sent successfully!")
