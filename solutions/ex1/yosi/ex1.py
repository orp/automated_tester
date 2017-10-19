def circle_area(r):
    "returns the area of a circle with radius r. Assumes pi = 3.14"
    return r **2 * 3.1

def fizzbuzz(n):
    """return the sum of all numbers between 1 and n (inclusive)
    but skips all values that are multiple of 5 or 7, unless they are multiples of
    both 5 and 7, in which case they are included times 2 (so 35 adds 70)"""
    sum = 1
    i = 1
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            sum += i * 2
        elif i % 5 == 0 or i % 7 == 0:
            pass
        else:
            sum += i
        i += 1
    return sum

def count_in_str(pattern, str):
    """counts the number of times the pattern appears in the string
    for example:
        count_in_str("a", "abcaabc") returns 3
        count_in_str("ab", "abcaabc") return 2"""
    c = 0
    sp = len(pattern)
    while len(str) >= sp:
        slice = str[:sp]
        if pattern == slice:
            c += 1
        str = str[1:]
    return c

def flip_ends(str):
    "this function exchanges the first and last character of a string"
    if (len(str) <= 1):
        return str
    else:
        return str[-1] + str[1:-1] + str[0]

def is_prime(x):
    "this function return True iif x is prime"
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i ** 2 <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def sum_primes(n):
    "this function computes the sum of all primes up to N, not including N"
    sum = 0
    i = 2
    while i < n:
        if is_prime(i):
            sum += i
        i += 1
    return sum
        
#start tests
def test_circle_area():
    assert(circle_area(1) == 3.14)
    assert(circle_area(0) == 0)
    assert(circle_area(10) == 314)

def test_fizzbuzz():
    assert(fizzbuzz(1) == 1)
    assert(fizzbuzz(8) == 1 + 2 + 3 + 4 + 6 + 8) #5 and 7 are skipped
    assert(fizzbuzz(35) == 490)

def test_count_in_str():
    assert(count_in_str("a", "abcaabc") == 3)
    assert(count_in_str("ab", "abcaabc") == 2)
    assert(count_in_str("abx", "abx") == 1)
    assert(count_in_str("abx", "ab") == 0)

def test_flip_ends():
    assert(flip_ends("") == "")
    assert(flip_ends("a") == "a")
    assert(flip_ends("ab") == "ba")
    assert(flip_ends("abc") == "cba")

def test_is_prime():
    assert(is_prime(1) == False)
    assert(is_prime(2) == True)
    assert(is_prime(3) == True)
    assert(is_prime(5) == True)
    assert(is_prime(9) == False)
    assert(is_prime(14) == False)
    assert(is_prime(17) == True)

def test_sum_primes():
    assert(sum_primes(5) == 5)
    assert(sum_primes(10) == 17)
    
if __name__ == "__main__":
    test_circle_area()
    test_fizzbuzz()
    test_count_in_str()
    test_flip_ends()
    test_is_prime()
    test_sum_primes()