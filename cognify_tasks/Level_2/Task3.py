def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return "Weak password: must be at least 8 characters long"

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check each character in the password
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    # Final strength evaluation
    if has_upper and has_lower and has_digit and has_special:
        return "Strong password"
    else:
        return "Moderate password: include uppercase, lowercase, digits, and special characters"

# Take input from the user
password = input("Enter your password: ")

# Display password strength
print(check_password_strength(password))
