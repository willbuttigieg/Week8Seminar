"""
Cp1404 Seminar 8
Product app
"""

class Product:
    """Product class for storing details about a product."""

    def __init__(self, name, price):
        """Initialise a product."""
        self.name = name
        self.price = price


    def __repr__(self):
        """String representation of a product."""
        return f"{self.name}, ${self.price}"