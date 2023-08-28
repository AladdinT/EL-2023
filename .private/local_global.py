global_var = 10

def modify_global():
    print(global_var.to_bytes(length=8, byteorder='big'))
    print(global_var.conjugate() )
    print(global_var)

def modify_local():
    local_var = 30
    print("Inside the function:", local_var)

modify_global()
print("After modifying global_var:", global_var)

modify_local()
# Uncommenting the next line will result in an error
# print("Outside the function:", local_var)
