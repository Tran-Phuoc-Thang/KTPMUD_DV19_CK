
# câu 1
# a. Kiểm tra một mảng cho trước gồm 4 phần tử có ít nhất 2 số nguyên tố. Chương trình sẽ trả về ‘True’
# Lấy dữ liệu
def check_prime_number(n):
    flag = True;
    if (n <2):
        flag = False
        return flag  
    for p in range(2, n):
        if n % p == 0:
            flag = False
            break
    return flag
def prime(arr):
    count = 0
    for i in arr:
        if check_prime_number(i):
            count = count + 1
    if count >= 2:
        return True
    return False