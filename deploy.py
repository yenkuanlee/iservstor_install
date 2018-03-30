import sys
import os
DomainName = sys.argv[1]
MnodeIP = sys.argv[2]
DnodeIP = sys.argv[3]

os.system("sed -i 's/DATA_NODE_IP=/DATA_NODE_IP="+DnodeIP+"/g' iservstor.rc")
os.system("sed -i 's/MANAGEMENT_NODE_IP=/MANAGEMENT_NODE_IP="+MnodeIP+"/g' iservstor.rc")
os.system("sed -i 's/ISERVSTOR_DOMAIN_NAME=/ISERVSTOR_DOMAIN_NAME="+DomainName+"/g' iservstor.rc")
os.chdir("iServStorPKG")
os.system("./deploy install")
