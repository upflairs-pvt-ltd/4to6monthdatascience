import socket 
s = socket.socket(socket.AF_INET  , socket.SOCK_DGRAM)
ip =  "127.0.0.1"   #"192.168.88.13"
port_no = 2525 
target_ip = (ip,port_no)  # full address 

condition = True 
while condition:
    message = input("plz write your message : ") 
    message_encrypt = message.encode("ascii") 
    s.sendto(message_encrypt,target_ip)
    print("your messeage is sent..")

    permission = input("do you want to quiet the program press Y/N :")
    if permission.lower()  == "y":
        condition = False 











