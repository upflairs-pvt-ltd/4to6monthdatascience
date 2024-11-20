### one way , two way build 
# sender ===> send,recieve  
# reciever == > recieve ,  send 
import socket 
import os 
# UDP ==> user datagram protocol
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address = "127.0.0.1"
port_no = 2525

complete_address = (ip_address,port_no)
s.bind(complete_address)
print("Hey i am listening ...... ")
os.makedirs('media',exist_ok=True)
current_working_dire_path = os.getcwd() # pwd 
data_folder_path = os.path.join(current_working_dire_path,"media")
while True:
    data = s.recvfrom(100)
    message = data[0]
    decoded_message = message.decode('ascii')
    ip_address = data[1][0]
    print(f"Ip address : {ip_address} \nmessage is : {decoded_message}")

    inbox_folder_path = os.path.join(data_folder_path,'inbox files')
    os.makedirs(inbox_folder_path,exist_ok=True) 

    filename = ip_address+".txt"
    file_path = os.path.join(inbox_folder_path,filename)

    with open(file_path,'a') as file:
        file.write(decoded_message+'\n') 


