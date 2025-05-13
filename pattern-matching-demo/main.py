import re
def main():
    print("Hello from pattern-matching-demo!")
    msg_phone1 = ' My phone no is 1234567891 and 9876543211'
    ''' Below regex is to match for phonenumbers with 9 digits'''
    pattern = r'\d{10}'
    match = re.findall(pattern, msg_phone1)
    print(match)
    msg_phone2 = ' My phone no is (123)-456-7891 and 987654321'

    ''' Below regex is to match for phonenumbers with 9 digits'''
    pattern_2 = r'\(\d{3}\)-\d{3}-\d{4}'
    match2 = re.findall(pattern_2,msg_phone2)
    print(match2)


if __name__ == "__main__":
    main()
