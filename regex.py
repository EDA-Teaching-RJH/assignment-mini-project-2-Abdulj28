import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)



def extract_domain(email):
    match = re.search(r'@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$', email)
    if match:
        return match.group(1)
    return None




def main():


    user_email = input("Please enter your email address: ")
    match = validate_email(user_email)


    if match:
        print(f"{user_email} is a valid email address.")
        domain = extract_domain(user_email)


        if domain:
            print(f"The domain of the email address is: {domain}")
        else:
            print("Failed to extract domain.")


    else:
        print(f"{user_email} is not a valid email address.")



if __name__ == "__main__":
    main()