import hashlib
m = hashlib.sha512()
m.update("test to encode goes here".encode('ascii'))
print(m.hexdigest())