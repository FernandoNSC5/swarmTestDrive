import socket

class sender():

    def __init__(self):
        # Localhost
        self.ip     = "poc"
        self.port   = 3000
        self.buffer = 128
        self.run()
    
    def run(self):
        print("[INFO] Starting sender server")
        # Crete TCP connection
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            soc.connect((self.ip, self.port))
        except Exception as e:
            print(f"Error connecting to receiver: {e.__doc__}")
            soc.close()
            return
        
        for i in range(10):
            try:
                soc.send(str(i).encode())
            except Exception as e:
                print(f"Error sending data: {e}")
                soc.close()
                return
s = sender()