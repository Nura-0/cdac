#ACADEMIC EMAIL VALIDATOR
import re

def validate_academic_email(email):
    pattern = r"^([a-z0-9._]+)@([a-z0-9.-]+).(edu|res.in)$"
    match = re.search(pattern, email)
    if match:
        return True
    else:
        return False

print(validate_academic_email("arunchengaloor15@edu.in"))