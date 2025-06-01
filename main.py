import pywhatkit
import csv
import time

with open('./contact_list.csv', newline='') as csvfile:
    contacts = csv.reader(csvfile)
    next(contacts)
    for contact in contacts:
        number = ''.join(contact)
        pywhatkit.sendwhatmsg_instantly(number, 'Bom dia!! Já ouviu falar da Coffe Day? ' \
        'Aqui temos café de qualidade e lanches para alegrar sua tarde.', 15, True, 4)
        time.sleep(10)
    
        
        



