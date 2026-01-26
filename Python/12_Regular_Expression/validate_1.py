# Regex:

email = input("Enter your email: ").strip();

username, domain = email.split("@");

if username and domain.endswith(".edu"):
    print("Valid email");
else:
    print("Invalid email");