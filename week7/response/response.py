import validators

def main():
    email = input("What's your email address? ").strip()
    if validate(email):
        print("Valid")
    else:
        print("Invalid")

def validate(email):
    return bool(validators.email(email))

if __name__ == "__main__":
    main()
