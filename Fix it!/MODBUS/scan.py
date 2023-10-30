import time
import datetime
from pymodbus.client import ModbusTcpClient

#512, 513, 514, 515, 	

for ports in [512, 513, 514, 515, 516]:
	client = ModbusTcpClient(host='**.**.***.***', port=ports)
	print("scanning port: "+ str(ports))
	client.connect()
	for i in range(1,2045):
		now = datetime.datetime.now()
		client.write_coil(i, True, slave=1)  
		print("turning " + str(i) + " on     "+str(now))
		#time.sleep(2)
		#client.write_coil(i, False, slave=1)
		#print("turning " + str(i) + " off   "+ str(now))
	#for i in range(2040, 2050):
		#now = datetime.datetime.now()
		#client.write_coil(i, True, slave=1)  
		#print("turning " + str(i) + " on     "+str(now))
		#time.sleep(2)
		#client.write_coil(i, False, slave=1)
		#print("turning " + str(i) + " off   "+ str(now))
	client.close()
	print('closing connection on port: ' + str(ports))
