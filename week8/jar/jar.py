class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    # Methodes -----------------------------------------

    def deposit(self, n):
        if n > 0 and self.size + n <= self.capacity :
            self.size = self.size + n
        else:
            raise ValueError

    def withdraw(self, n):
        if n > 0 and self.size >= n:
            self.size = self.size - n
        else:
            raise ValueError

    # Getters -----------------------------------------


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



    # Setters -----------------------------------------

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity


    @size.setter
    def size(self, size):
        self._size = size



def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    print(jar)


if __name__ == "__main__":
    main()
