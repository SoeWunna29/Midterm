def is_plndrm(n):
    word = str(n)
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_plndrm(word[1:-1])


print(is_plndrm(45654))
print(is_plndrm(42))
print(is_plndrm(2019))
print(is_plndrm(10101))
