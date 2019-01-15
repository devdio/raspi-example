import bluetooth

bd_addr = '50:77:05:74:FC:8E'
port = 1
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect(bd_addr, port)
data = ''
while 1:
	try:
		data += sock.recv(1024)
		data_end=data.find('\n')
		if data_end != -1:
			rec = data[:data_end]
			print(data)
			data = data[data_end+1:]
	except KeyboardInterrupt:
		break
sock.close()				