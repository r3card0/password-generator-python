# import libraries
import random
from description import description # description of the program
from len_character import set_len_character # choose the max number of characteres in password
from char_lists import get_character_lists

# get password
def get_password():
    max_num = set_len_character(12)
    password = []

    for i in range(max_num):
        char_random = random.choice(get_character_lists())
        password.append(char_random)
    
    # convert list to string
    password_str = ''.join(password)
    return password_str 

# entry point

def run():
    print(description())
    print('Your new password is: ',get_password())


if __name__ == "__main__":
    run()