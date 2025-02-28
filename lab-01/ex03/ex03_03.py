def tao_tuple_tu_list(n):
    return tuple(n)

input_list = input("Nhập vào một danh sách các số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ list: ", my_tuple)