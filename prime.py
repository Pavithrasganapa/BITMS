'''def find_primes(numbers):
    primes=[]
    for number in numbers:
        if number>1:
            is_prime=True
            for i in range(2,number):
                if number % i==0:
                    is_prime=False
                    break
            if is_prime:
                primes.append(number)
    return primes
my_numbers=[2004,1996,17,85]
my_primes=find_primes(my_numbers)
print(my_primes)'''
def primes():
    prime=[]
    leap=[]
    n=int(input('enter list'))
    for i in range(2,n+2):
        ele=int(input('enetr element'))
        prime.append(ele)
        i<=n/2
        if ele % i == 0:
            print('its not prime')
        else:
            print('its prime')
    print(prime)
    for i in range(0,n):
        ele=int(input('enetr element'))
        leap.append(ele)
        if ele % 4 == 0:
            print('its leap')
        else:
            print('its not leap')
    print(leap)
primes()
