import datetime
import socket
from flask import Flask

now = datetime.datetime.now()                                                                                                                      
                                                                                                                                                       
f= open("/mnt/hello_log.txt","a+")                                                                                                                 
f.write ("%r,%r\n" % (socket.gethostname(), now.strftime("%Y-%m-%d %H:%M:%S")))                                                                    
f.close()  

application = Flask(__name__)

@application.route("/")
def hello():
  with open("/mnt/hello_log.txt") as f:
    contents = f.read()
    
  f.close()
  
  return contents

if __name__ == "__main__":
    application.run()
