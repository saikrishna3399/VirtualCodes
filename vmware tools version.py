# Written By Sai Krishna
# Email : saikrishna.pendurthi1996@gmail.com

from pyVim.connect import SmartConnect, Disconnect
import ssl
from pyVmomi import vim

s =  ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE

print("Cert Type:")
try:
    c = SmartConnect(host="192.168.0.51", user="Administrator@vsphere.local", pwd="VMware123!")
    print('Valid Certificate')
except:
    c = SmartConnect(host="192.168.0.51", user="Administrator@vsphere.local", pwd="VMware123!", sslContext=s)
    print('Invalid or Untrusted Certificate')
print("Time On VC :")

print(c.CurrentTime())
print("*"*36)

content = c.RetrieveContent()

container = content.rootFolder
item = [vim.VirtualMachine]

recursive = True

containerView = content.viewManager.CreateContainerView(container, item, recursive)

vms = containerView.view
# for vm in vms:
#     if vm.summary is not None:
#         try:
#             info = vm.summary
#             print("VM is {} and its Summary is {}".format(vm, info))
#             print("*"*56)
#         except:
#             print("None")

for vm in vms:
    if vm.summary.guest is not None:
        try:
            info = vm.summary.guest
            print("VM is {} and its Guest summary \n{}".format(vm, info))
            print("*"*56)
        except:
            print("None")

Disconnect(c)

