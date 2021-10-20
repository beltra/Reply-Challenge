import struct
import binascii
import math
leftrotate = lambda x, n: (x << n) | (x >> (32 - n))


class MGH():

	A, B, C, D = (0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476)

	r = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
		 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
		 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
		 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

	k = [int(math.floor(abs(math.sin(i + 1)) * (2 ** 32))) for i in range(64)]

	def __init__(self, message):
		self._is_bytes(message)
		length = (len(message) * 8) % (2**64)
		message += b'\x80\x80\x80\x80'
		zero_padding = b'\x00' * (((448 - (length + 32) % 512) % 512) // 8)
		message += zero_padding
		message += length.to_bytes(8, byteorder='little')

		assert len(message) % 64 == 0

		while len(message):
			self._chunk_handler(message[:64])
			message = message[64:]
	
	def _is_bytes(self, data):
		try:
			assert(isinstance(data,bytes))
		except:
			exit()

	def _chunk_divider(self, chunk, nr_words):
		chunk_divided = []
		size = len(chunk)//nr_words
		for i in range(0, nr_words):
			chunk_divided.append( int.from_bytes(chunk[i*size:(i+1)*size],byteorder="little"))
		return(chunk_divided)

	def _chunk_handler(self, chunk):
		w = self._chunk_divider(chunk, 16)

		a, b, c, d = self.A, self.B, self.C, self.D
		for i in range(64):
			if i < 16:
				f = (b & c) | ((~b) & d)
				g = i
			elif i < 32:
				f = (d & b) | ((~d) & c)
				g = (5 * i + 1) % 16
			elif i < 48:
				f = b ^ c ^ d
				g = (3 * i + 5) % 16
			else:
				f = c ^ (b | (~d))
				g = (7 * i) % 16

			x = b + leftrotate((a + f + self.k[i] + w[g]) & 0xffffffff, self.r[i])
			a, b, c, d = d, x & 0xffffffff, b, c

		self.A = (self.A + a) & 0xffffffff
		self.B = (self.B + b) & 0xffffffff
		self.C = (self.C + c) & 0xffffffff
		self.D = (self.D + d) & 0xffffffff

	def digest(self):
		return struct.pack('<IIII', self.A, self.B, self.C, self.D)

	def hexdigest(self):
		return binascii.hexlify(self.digest()).decode()

string = "6334723366756c5f306e33"
byte = bytes.fromhex(string) 
msg = MGH(byte)
print(msg.hexdigest())