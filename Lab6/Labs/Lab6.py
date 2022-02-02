""" Primes, GCD, LCM """
import math

# sample answer from today's lession
def is_prime(n):
    """ Check if n is prime """
    if n<=1:
      return False
    
    for i in range(2,int(math.sqrt(n)) + 1):
      if n % i == 0:
        return False

    return True

#https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm from a course slide
def gcd(a, b):
    """ GCD of a and b """
    # remainder
    r = 0

    # until a mod b equals 0
    while (a % b) > 0:
      r = a % b
      a = b
      b = r    
    
    return b 


def lcm(a, b):
    """ LCM of a and b """
    return (a * b) / gcd(a,b)

# sample answer from today's lesson
def generate_primes(n):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """

    prime_list = []

    for i in range(2,n + 1):
      if is_prime(i):
        prime_list.append(i)

    return prime_list
