from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', 8080))
s.listen(1)
while True:
    print s.accept()[1]