#import pyperclip

def save_password(password, account_name):
    '''
    This takes two input and append each of them in a new in a txt file
    '''
    with open("pass_not_encrypted.txt", "a") as f:
        f.write(account_name + "\n")
        f.write(password + "\n")
    f.close()
    return None

def check_password(account_name):
    '''
    This takes one input and returns a list of similar account names and passwords  from a txt file
    '''
    lst = []
    with open("pass_not_encrypted.txt") as f:
            x = f.readlines()
    f.close()
    for i in x:
        lst.append(i.strip('\n'))
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


if __name__ == "__main__":
    swapping = True
    while swapping:
        action = input("What will you like to do? (save_password(s)/check password(c)): ")
        if 's' in action or 'c' in action:
            swapping = False
    account_name = input("Enter the name of the account: ")
    if action.lower() == "s":
        password = input("Please type in the password you want to save: ")
        save_password(password, account_name)
        print("Password_saved")
    if action.lower() == "c":
        check_password(account_name)