import mandrill
import socket

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


if is_connected():   #If there is internet connection, email IP address

    mandrill_client = mandrill.Mandrill('Mandrill API Key')

    try:
        message = {
         'bcc_address': 'to_email@example.com',
         'from_email': 'from_email@example.com',
         'from_name': 'Brandon Walsh',
         'to': [{'email': 'to_email@example.com',
                 'name': 'Recipient Name',
                 'type': 'to'}],
         'html': '<p>' +  socket.gethostbyname(socket.gethostname()) + '</p>',
         'subject': 'Subject here'
         };
         
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='', send_at='')

        print result

    except mandrill.Error, e:
        # Mandrill errors are thrown as exceptions
        print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
        raise
else:
    print 'Please make sure you have an internet connection established.  '

   