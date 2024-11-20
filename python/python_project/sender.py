import socket 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_address = "127.0.0.1"  # 127.0.0.1 localhost 
port_no = 2525
target_address = (ip_address,port_no)

quiet = False
while not quiet:
    DATA_TYPE = """what do you want to send,
                press 1. for message
                press 2. for text file  """
    send_data_code = int(input(DATA_TYPE))
    if send_data_code == 1:

        message = input("plz write your message : ")
        encrypted_message = message.encode('ascii')  # encryption 
        s.sendto(encrypted_message,target_address)
        print("successfully sent the message!")

        checkmark  = input("Do you want to quiet it press Y/N :  ") # 
        if checkmark.lower() == "y" :
            quiet = True 
        else:
            pass  
    elif send_data_code == 2:
        path = input("plz enter the path of the file : ")
        with open(path,'r') as file:
            file_content = file.read()
            encrypted_file_content = file_content.encode('ascii')
            s.sendto(encrypted_file_content,target_address)
 
    else:
        pass 
# whatsapp(encryption, decryption) 

  