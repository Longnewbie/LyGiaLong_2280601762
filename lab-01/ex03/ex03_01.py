def tinh_tong_so_chan(n):
    tong = 0
    for i in n:
        if i % 2 == 0:
            tong += i
    return tong

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong list: ", tong_chan)