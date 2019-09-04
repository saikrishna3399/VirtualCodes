# Written By Sai Krishna
# Email : saikrishna.pendurthi1996@gmail.com

from pyVim.connect import SmartConnect, Disconnect
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

print("Cert Type:")

#To check  the Cert Type of VC
try:
    c = SmartConnect(host="192.168.0.51", user="Administrator@vsphere.local", pwd="VMware123!")
    print('Valid Certificate')
except:
    c = SmartConnect(host="192.168.0.51", user="Administrator@vsphere.local", pwd="VMware123!", sslContext=s)
    print('Invalid or Untrusted Certificate')

#To Check Time On VC
print("Time On VC :")

print(c.CurrentTime())
print("*" * 36)

#Code for Extension List


print("The List Of Extensions")
extension = c.content.extensionManager.extensionList
j = 1
for i in extension:
    print("{} :  {}".format(j, i.key))
    j += 1

print("*"*36)

Disconnect(c)