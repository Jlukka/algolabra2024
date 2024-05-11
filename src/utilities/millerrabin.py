from random import randint


class MillerRabin():
    def __init__(self, attempts):
        self.attempts = attempts

    def primalityTest(self, number):
        if number == 1:
            return False

        if number % 2 == 0:
            return False

        for i in range(0, self.attempts):
            if not self.__millerRabin(number):
                return False
        return True

    def __millerRabin(self, number):
        a = randint(2, number - 2)

        d, s = self.__findDandS(number)

        x = pow(a, d, number)
        for i in range(0, s):
            y = pow(x, 2, number)

            if y == 1 and x != 1 and x != number - 1:
                return False

            x = y
        if y != 1:
            return False
        return True

    def __findDandS(self, number):
        d = number - 1
        s = 0
        while (d % 2 == 0):
            d //= 2
            s += 1
        return d, s
