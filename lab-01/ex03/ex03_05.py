def dem_so_lan_xuat_hien(n):
    count_dict = {}
    for i in n:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()

so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử: ", so_lan_xuat_hien)