# Pass_saver
A python script for saving password.
The saved password is not encrypted.

## What can Pass_Saver Do?
---
- Save password:
    - Can generate password to save which it automatically copies to the clipboard.
    - Can also use user-given password instead of auto-generated
- Check saved password: Check your saved password by typing the website of the password to search for. Its a pattern matching thing.
- List available accounts: This lists all the accounts that has been saved.
- Search an account: Search for a particular account.
- Update an accont: Used to update an accout.

## Installation Steps
---
Follow these steps to install this program.
Pre-requisites:
Python3

Installation:
1. Run `python3 -m pip install venv`
2. Run `python3 venv venv`
3. change directory into venv/Scripts `cd venv\Scripts`
4. Run `activate.bat` on Windows OS and `./activate` on a Unix OS
5. Run `python -m pip install -r requirements.txt`
6. Run `python main.py`

This script can take save a password, suggest a password and also return a password and copy it to the clipboard.