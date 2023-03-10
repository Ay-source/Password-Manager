import sys
import string
import time
import random
import pyperclip


def save_password(password,account_description, account_name):
    '''
    This takes two input and append each of them in a new in a txt file
    '''
    with open("pass_not_encrypted.txt", "a") as f:
        f.write(account_name.lower() + "\n")
        f.write(account_description + "\n")
        f.write(password + "\n\n")
    f.close()
    return True

def check_password(account_name):
    '''
    This takes one input and returns a list of similar account names and passwords  from a txt file
    '''
    lst = []
    with open("pass_not_encrypted.txt") as f:
            x = f.readlines()
    f.close()
    for i in x:
        lst.append(i.strip('\n').lower())
    account, passes = checked_password_string(lst)
    account_pass = pass_sorter(account_name, account, passes)
    for i in account_pass:
        print("Account_name: " + i + "\n" + "Password: " + account_pass[i])
    return None

def checked_password_string(lst):
    """
    This takes a list a returns a split version of it.
    """
    account = []
    passes = []
    for i in lst:
        if lst.index(i) % 2 == 0:
            account.append(i)
        else:
            passes.append(i)
    return account, passes

def pass_sorter(account_name, account, passes):
    """
    This adds each values in the lists account name and password as keys and values respectively to a dictionary
    """
    account_pass = dict()
    for i in account:
        if account_name in i:
            account_pass[i] = passes[account.index(account_name)]
    return account_pass

def list_passwords():
    pass

def search_accounts():
    pass

def copy_and_paste_values(password):
    try:
        pyperclip.copy(password)
        return True
    except:
        return False

def suggest_password():
    select1 = ''.join(random.choices(list('!?*&^%$#'), k=2))
    select2 = ''.join(random.choices(list(string.ascii_lowercase), k=6))
    select4 = ''.join(random.choices(list(string.ascii_uppercase), k=2))
    select3 = str(random.randint(0, 9)) + str(random.randint(0, 9))
    final_pass = select2 + select3 + select1 + select4
    sample = list(map(str,final_pass))
    password = ''
    while len(sample) > 0:
        password += sample.pop(random.randint(0, len(sample)-1))
    return password

def update_password():
    pass


if __name__ == "__main__":
    swapping = True
    while swapping:
        action = input("What will you like to do? save_password(s) / check saved password(c) / List available accounts(l) \
search account(q) / Update account(u): ").lower()
        if action in ['s', 'c', 'l', 'q', 'u']:
            swapping = False
    if action in ['s', 'c', 'q', 'u']:
        account_name = input("Name of account/website: ")

    if action == 's':
        account_description = input("Add a desciption(Optional): ")
        password_input = input("Autogenerate password(a) / Input password(i)").lower()
        if password_input == 'i':
            password = input("Type in the password you want to save: ")
        else:
            password = suggest_password()
        save = save_password(password, account_description, account_name)
        keep = input("Do you wish to copy the password? Y/N: ").lower()
        if keep == 'y':
            keep_valid = copy_and_paste_values(password)
        if keep_valid:
            print("Passsword copied to clipboard")
            time.sleep(2)
        if save:
            print("Password_saved")
            sys.exit(0)
        print("An error occured.")

    elif action == 'c':
        check_password(account_name)
    elif action == "l":
        list_passwords()
    elif action == 'q':
        search_accounts(account_name)
    else:
        update_password(account_name)
    