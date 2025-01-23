import socket 
s = socket.socket(socket.AF_INET  , socket.SOCK_DGRAM)
ip_address = "127.0.0.1"   #"192.168.88.13"
port_no = 2525 
address = (ip_address,port_no)

s.bind(address) 
print("Hey i am lestening....")
while True:
    data= s.recvfrom(100)
    message = data[0]
    decoded_message = message.decode('ascii')
    ip_address = data[1][0]
    print("Recieved Message : ",decoded_message)
    with open(ip_address+".txt",'a+') as file:
        file.write(decoded_message+"\n")



 