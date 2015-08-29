import mandrill
import socket
from sys import argv

REMOTE_SERVER = "www.google.com"

#checks if there is internet connection
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

def send_mail():
    mandrill_client = mandrill.Mandrill('Your Mandrill API key')

    try:
        message = {
         'bcc_address': 'email@example.com',
         'from_email': 'email@example.com',
         'from_name': 'Brandon Walsh',
         'to': [{'email': 'email@example.com',
                 'name': 'Recipient Name',
                 'type': 'to'}],
         'html': '<p>' +  socket.gethostbyname(socket.gethostname()) + '</p>',
         'subject': 'RPi IP'
         };
         
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='', send_at='')

        print result

    except mandrill.Error, e:
        # Mandrill errors are thrown as exceptions
        print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
        raise


if is_connected():   #If there is internet connection, email IP address to myself

    txt = open('ip.txt')
    current_ip = socket.gethostbyname(socket.gethostname())

    if txt.readline() == '': #if the txt file does not have an IP (is empty)
        txt = open('ip.txt', "w")
        txt.write(current_ip)
        txt.close()
    else:
        txt = open('ip.txt')
        file_ip = txt.readline()

        if file_ip != current_ip: #if last saved IP is different than current IP
            print 'Old IP Address:' + file_ip
            print 'Current IP Address' + current_ip

            txt = open('ip.txt', "w")
            txt.write(current_ip)
            txt.close()

            send_mail()


    
else:
    print 'Please make sure you have an internet connection established.'

   
