import re
from pattern_match_util import get_phone_no,get_email_id,get_order_no
def main():
    print("Hello from pattern-matching-demo!")
    msg_phone1 = ' My phone no is 1234567891 and 9876543211'
    msg_phone2 = ' My phone no is (123)-456-7891 and 9876543211'
    msg_email = ' My email id is sachin.bharathy@gmail.com'
    msg_order_no = ' My order no is 123456789'
    print(get_phone_no(msg_phone1))
    print(get_phone_no(msg_phone2))
    print(get_email_id(msg_email))
    print(get_order_no(msg_order_no))

if __name__ == "__main__":
    main()
