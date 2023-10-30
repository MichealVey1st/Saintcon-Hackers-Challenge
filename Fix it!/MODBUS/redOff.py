from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(host='**.**.***.***', port=514)
client.connect()

client.write_coil(0x00, False, 1)

client.close()
