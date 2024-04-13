class EuclideanAlgorithms:
    def GCD(self,a,b):
        """calculate the GCD of given two positive integers by using Euclidean Algorithm
           args:
           a : positive integer
           b : positive integer

           returns:
           GCD of given two positive integers
        """

        if b>a: # if a<b then swap them
            a,b=b,a

        else:
            while b != 0:
                temp = b
                b = a % b
                a = temp
            return a

if __name__ == '__main__':
    euclidean_alg=EuclideanAlgorithms()
    # input two numbers
    number1=int(input("enter first number:"))
    number2=int(input("enter second number:"))
    if number1 <=0 or number2 <=0: # check if the input number is positive number
        print("input numbers should be positive integers") # if not, then raise warning
    print(euclidean_alg.GCD(number1,number2))

