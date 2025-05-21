import pywhatkit
import csv
import time

with open('./contact_list.csv', newline='') as csvfile:
    contacts = csv.reader(csvfile)
    next(contacts)
    for contact in contacts:
        number = ''.join(contact)
        pywhatkit.sendwhatmsg_instantly(number, 'Hello World', 15, True, 4)
        time.sleep(15)
        
        



