# Import socket module
import socket           
 
# Create a socket object
socket1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
 
# Define the port on which you want to connect
port = 12345   
# Defining the variables            
pitchyaw=0
roll=0
pitch=0
yaw=0
# Counter to avoid first few readings that have error
delayer=0
# connect to the server on local computer
socket1.connect(('192.168.137.1', port))
while True:
    recieved = socket1.recv(32768).decode()     ##### Put the recieved readings into variable
    if "." in recieved:                         ##### "." is a delimiter we put in the readings to identify first element,so if we have "." in reading it means there's no error.
        roll=list(recieved)                     ##### Roll is the first reading, we just remove the "," and "." and we have an integer reading
        del roll[-1]                            ##### Delete last index of reading ","
        del roll[-1]                            ##### Delete last index again "."
        roll = "".join(roll)
    else:
        pitchyaw = recieved                     ##### Put the recieved reading into variable if it doesn't contain "."
        pitch = pitchyaw.split(",")[0]          ##### The second and third reading are stuck to each other so this part splits them into two variables <=== Pitch
        yaw = pitchyaw.split(",")[1]            ##### <=== Yaw
    if len(roll)<6 and delayer>2000 :           ##### len(roll)<6 is to ensure that the reading has no error, because sometimes they get stuck into eachother so we disregard these readings. Delayer to wait a few seconds before taking readings to avoid error.
        print([roll,pitch,yaw])
    delayer+=1
 