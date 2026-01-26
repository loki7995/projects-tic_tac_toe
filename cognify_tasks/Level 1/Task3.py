print("Email Validator-(check wether given email is valid or not)")
print("--------------------------------------------------------")

def is_valid_email(email):
    # Check for spaces
    if " " in email:
        return False

    # Check for exactly one '@'
    if email.count("@") != 1:
        return False

    local_part, domain_part = email.split("@")

    # Check local and domain parts are not empty
    if not local_part or not domain_part:
        return False

    # Domain must contain at least one dot
    if "." not in domain_part:
        return False

    # Dot should not be at the start or end of domain
    if domain_part.startswith(".") or domain_part.endswith("."):
        return False

    return True


# -------- MAIN PROGRAM --------
email = input("Enter an email address: ")

if is_valid_email(email):
    print("Yes, the given email is valid")
else:
    print("No, the given email is invalid")

#OUTPUT
'''Email Validator-(check wether given email is valid or not)
--------------------------------------------------------
Enter an email address: loki@gmail.com
Yes, the given email is valid'''    