# Create a class Product with a property price.
# The property should have a getter and a setter.
# The setter should ensure that the price is not negative.
class Product:
    def __init__(self, price) -> None:
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")

        self._price = value


# Create an instance of Product
product = Product(50)
print(product.price)  # Output: 50

# Change the price
product.price = 100
print(product.price)  # Output: 100

# Try to set a negative price (should raise an error)
try:
    product.price = -10
except ValueError as e:
    print(e)  # Output: Price cannot be negative
