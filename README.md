# QA-testsite
A python project based on Selenium package that runs QA test scripts on a test site.

Contents:
spam.py:
A python file based on Selenium package that sends randomly generated values to 'Name', 'Email', 'Phone', 'Subject' and 'Message' fields and clicks on submit.
This runs a total of 25 times for spam test purpose.

testCases.py:
A python file based on Selenium package that sends datas that is defined inside the program which loops the provided data and inserts it into the corresponding 
field of the test site. The script check if any error message appears and compares if the error occured was expected or not expected and provides the out accordingly.
