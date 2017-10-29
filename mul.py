def karatsuba(x,y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    m = max(len(str(x)), len(str(y)))
    m2 = m / 2

    a = x / (10 ** m2)
    b = x % (10 ** m2)
    c = y / (10 ** m2)
    d = y % (10 ** m2)

    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

    pro = ac * 10 ** (2 * m2) + (ad_plus_bc * 10 ** m2) + bd
    prod = ac * 10 ** m + (ad_plus_bc * 10 ** m2) + bd

    return pro
    #return prod 

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
#x = 5678
#y = 1234

print karatsuba(x,y)
