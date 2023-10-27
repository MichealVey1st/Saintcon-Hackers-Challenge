from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(host='10.30.246.117', port=514)
client.connect()

client.write_coil(0x00, True, 1)

client.close()
