def binary_representation(num):
    if num < 0:
        mystr = bin(num)
    else:
        mystr = bin(num)[2:].zfill(8)  # Convert to binary and remove '0b' prefix, then zero-fill to 8 bits
    return mystr
    

a = 28 
b = 10 

print("-"*30)
print(f"{a} --binary-> {binary_representation(a)}")
print(f"{b} --binary-> {binary_representation(b)}")

result_and = a & b
print("-"*30)
print(f"Bitwise AND : {binary_representation(result_and)}")
print(f"{a} & {b} = {result_and}")

result_or = a | b
print("-"*30)
print(f"Bitwise OR  : {binary_representation(result_or)} ")

result_xor = a ^ b
print("-"*30)
print(f"Bitwise XOR : {binary_representation(result_xor)} ")

result_comp = ~a
print("*"*30)
print(f"{a} --binary->   ~{binary_representation(a)} ")
print(f"one's complement: {binary_representation(result_comp)}")
print(f"two's complement: {(result_comp + 1)}")

result_left_shift = a << 2
print("-"*30)
print(f"{a} --binary-> {binary_representation(a)} << 2")
print(f"Left Shift  : {binary_representation(result_left_shift)}")

result_right_shift = a >> 2
print("-"*30)
print(f"{a} --binary-> {binary_representation(a)} >> 2")
print(f"Right Shift : {binary_representation(result_right_shift)}")
