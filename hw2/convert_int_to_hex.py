# user_number = 65535
user_number = int(input("Enter the number you want to convert: "))

hex_number_string = f'{user_number:#x}'  # "0xffff"

print(hex_number_string, hex(user_number))  # "0xffff" "0xffff"

