#Using Twilio to send sms messages

#Twiliio is a external package (it is not in the standard library of python)

#'twilio' is a module or filename, that has a file in it called 'rest',
# which has a class called 'TwilioRestClient'
# 'client' is an instance created using the class 'TwilioRestClient'
# See the implementation of Twilio in Github


from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4f5219c6d3c198ec3e64827017c5c602"
auth_token  = "{{4aa88befb12fb77985a98b1cb33b4da9}}"
client = TwilioRestClient(account_sid, auth_token)  #'client' is an instance
 
message = client.messages.create(
    body="Jennifer oh Jennifer",
    to="+34609965614",    # Replace with your phone number
    from_ ="+34518890128") # Replace with your Twilio number
print message.sid
