def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Nhập vào một chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược: ", dao_nguoc_chuoi(input_string))