from primefactor import is_prime

def main():
    num= int(input("Enter an integer:"))
    if is_prime(num):
        print(num,"is prime")
    else:
        print(num, "not a prime")

main()
