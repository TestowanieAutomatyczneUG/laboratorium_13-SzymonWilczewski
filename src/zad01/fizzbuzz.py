class FizzBuzz:
    def game(self, num):
        if type(num) != int:
            return "Wrong type!"
        elif (num % 15) == 0:
            return "FizzBuzz"
        elif (num % 3) == 0:
            return "Fizz"
        elif (num % 5) == 0:
            return "Buzz"
        else:
            return num
