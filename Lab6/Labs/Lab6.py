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

    # until a mod b(remainder) equals 0
    # b1 = a1 * q1 + r1
    # a1 = r1 * q2 + r2
    # r1 = r2 * q3 + r3

    while (b % a) > 0:
      r = b % a
      b = a
      a = r
    
    return a  #previous number when r becomes 0 is the largest number


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
