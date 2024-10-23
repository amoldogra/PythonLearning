
l = [1,2,55,85,44,66,25,18]
def divisible5(n):
    if n%5==0:
        return True
    return False

lst = filter(divisible5, l)
print(list(lst))