# VMware vSphere Python SDK, pyvmomi
# Simple script to get vCenter server product details
# Written By Sai Krishna
# Email : saikrishna.pendurthi1996@gmail.com


from pyVim.connect import SmartConnect, Disconnect
import ssl

s = ssl.SSLContext(ssl.PROTOCOL_SSLv23)  # For VC 6.5/6.0 s=ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

si = SmartConnect(host=input("Enter IP or FQDN of ESXi or VCSA : "), user=input("Enter User :  "),
                  pwd=input("Enter The Password : "), sslContext=s)
aboutInfo = si.content.about

print("Time On VC :")

print(si.CurrentTime())
print("*"*36)

print("Product Name:", aboutInfo.fullName)
print("Product Build:", aboutInfo.build)
print("Product Unique Id:", aboutInfo.instanceUuid)
print("Product Version:", aboutInfo.version)
print("Product Base OS:", aboutInfo.osType)
print("Product vendor:", aboutInfo.vendor)

Disconnect(si)