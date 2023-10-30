from pymodbus.client import ModbusTcpClient

client.connect()
client.write_coil(0x2041, True, 1)
client.close()
