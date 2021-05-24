import hashlib
import time

data0 = input("string input: ")
target=int(0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF)
x=1
begin = time.time()
while(1):
    data=data0+str(x)
    m = hashlib.sha256(data.encode('utf-8'))
    if int(m.hexdigest(),16)<target:
        time.sleep(1)
        break
    x+=1
end = time.time()
print("The magic number is "+str(x))
print(f"The time taken to get this nonce value is {end - begin} sec")
