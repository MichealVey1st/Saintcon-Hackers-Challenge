from pymodbus.client import ModbusTcpClient
import time

#green
#blue
#white

green_client = ModbusTcpClient(host='10.30.246.117', port=512)
green_client.connect()
green_client.write_coil(0x00, False, 1)
time.sleep(2)
green_client.write_coil(0x00, True, 1)
green_client.close()

blue_client_base = ModbusTcpClient(host='10.30.246.117', port=514)
blue_client_base.connect()
blue_client_base.write_coil(0x00, False, 1)
time.sleep(2)
blue_client_base.write_coil(0x00, True, 1)
blue_client_base.close()

white_client = ModbusTcpClient(host='10.30.246.117', port=516)
white_client.connect()
white_client.write_coil(0x2040, False, 1)
white_client.write_coil(0x2041, False, 1)
time.sleep(2)
white_client.write_coil(0x2041, True, 1)
result = white_client.read_coils(0x2041, slave=1)
print(result.bits[0])
white_client.close()

#for ports in [512, 513, 514, 515, 516]:
#	client = ModbusTcpClient(host='10.30.246.117', port=ports)
#	print("scanning port: "+ str(ports))
#	client.connect()
#	for i in range(20):
#		client.write_coil(i, True, slave=1)  
#		print("turning " + str(i) + " on")  
#		time.sleep(5)
#		client.write_coil(i, False, slave=1)
#		print("turning " + str(i) + " off")  
#	client.close()
#	print('closing connection on port: ' + str(ports))    
#512 00 green
#514 00 red & blue
#516 2041 white
