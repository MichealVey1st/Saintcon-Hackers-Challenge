from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(host='**.**.***.***', port=516)
client.connect()

client.write_coil(0x2040, True, 1)

client.close()
