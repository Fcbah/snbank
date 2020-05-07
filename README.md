# SNBANK

This is an app to Illustrate the Banking Filesystem in Python. Designed as part of start.ng task 4

## Features

The features of this app are:

+ Bank Staff Authentication and Login
+ Staffs can create bank accounts for Customers
+ Stores Customers Account details in an internal filesystem database
+ Bank staff can check and view stored account details of customer accounts
+ Display of validation errors to staff users
+ create session for logged in staffs. So they don't need to login again and again
+ Destroys every session on logout to avoid security breaches.

## Deployment Instructions

To deploy

1. First you need to have a recent version of python (i.e. python 3.x) installed on your machine. Visit [Python Official Website](https://www.python.org)

2. Ensure that your environment variables are properly set

3. Run the [bankingApp.py](bankingApp.py) with a terminal command as below

```bash
$ cd <PATH TO DIRECTORY>
$ python3 bankingApp.py
```

## File Arrangement

+ [bankingApp.py](bankingApp.py) is the main App file
+ [initialize.py](bankingApp.py) This is the script to reinitialize the content of the database folder
+ [clearground.py](clearground.py) This is a private script I use to clear the contents of customer.txt and sessions file and reinitialize them.
+ [db](db/) This is the folder that will host my database of
  + Customer records
  + Staff records
  + Session File
