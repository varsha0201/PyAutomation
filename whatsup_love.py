from twilio.rest import Client 
 
account_sid = 'AC7ba0faf60d1948ec20e68c9472d151cf' 
auth_token = 'd9b7e847906a5bc5cfe43ba80c7e7938' 
client = Client(account_sid, auth_token) 

def send_love():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Everything happen for reason, Enjoy your life!!',      
                                to='whatsapp:+919423301341' 
                            ) 
    
    print(message.sid)