if __name__ == "__main__":
    import doctest
    doctest.testmod()

def smallestDivisor(n):
    """
    return the smallest divisor of a given integer
    
    >>> smallestDivisor(2)
    2

    >>> smallestDivisor(5)
    5

    >>> smallestDivisor(180)
    2

    >>> smallestDivisor(81)
    3

    >>> smallestDivisor(-4)
    Traceback (most recent call last):
        ...
    ValueError: n must be a positive integer
    >>> smallestDivisor("3")
    Traceback (most recent call last):
        ...
    TypeError: n must be from type integer
    """
    #make sure n is a positive integer

    if not type(n)==int:
        raise TypeError("n must be from type integer")
    if not n>=0:
        raise ValueError("n must be a positive integer")
    
    if (n%2==0): return 2
    i = 3
    #the smallest divisor of an integer n is
    #smaller than squareroot(n)
    while(i*i<=n):
        if(n%i==0):
            return i
        i = i + 2
    return n

def factorize (n):
    """
    return an array with the factors of a given number

    >>> factorize(15)
    [3, 5]

    >>> factorize(121)
    [11, 11]

    >>> factorize(40)
    [2, 2, 2, 5]
    """
    #initialize divisor with a guaranted divosor of n
    a = n
    b = smallestDivisor(n)
    factors = []
    while(a>1):
        if (a%b==0):
            factors.append(b)
            a = a / b
        else:
            b = b + 1    
    return factors

def nthprime(n):
    """
    return the nth-prime

    >>> nthprime(1)
    2

    >>> nthprime(20)
    71

    >>> nthprime("String")
    Traceback (most recent call last):
    ...
    TypeError: n must be type of integer

    >>> nthprime(-2)
    Traceback (most recent call last):
    ...
    ValueError: n must be >1
    """
    if not type(n)==int:
        raise TypeError("n must be type of integer")
    if n<1:
        raise ValueError("n must be >1")
    if n == 1: return 2
    if n == 2: return 3

    primes = {2,3}
    
    #start at the lowest uneven prime
    i = 3

    #repeat this block until we get the desired nth prime
    while(len(primes)!=n):
        #factorize the current number, add all its factors to the prime set
        factors = factorize(i)
        for x in factors:
            primes.add(x)
        #increase 2 to go the next uneven number
        i = i + 2 
    #convert the set into a sorted list
    result = sorted(list(primes))
    return result[n-1]              
def main():
    print(nthprime(10001))

main()
