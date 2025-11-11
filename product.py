"""
Cp1404 Seminar 8
Product class
"""


class Product:
    """Product class for storing details about a product."""

    def __init__(self, name, price):
        """Initialise a product."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return a product instance as a string"""
        return f"{self.name}, ${self.price}"

    def __repr__(self):
        """Return developer-frienly string representation of product instance."""
        return f"{vars(self)}"
