"""
CP1404 Seminar 8
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from shopping_console import load_products
from product import Product


class ShoppingApp(App):
    """Shopping app class."""

    def __init__(self, **kwargs):
        """Construct main kivy app."""
        super().__init__(**kwargs)
        products = load_products("products.json")

    def build(self):
        """Build main kivy app."""
        Window.size = (800, 600)
        self.title = "Shopping App"
        self.root = Builder.load_file("shopping_app.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create widgets from ***."""
        for product in products:
            button = Button(text=product)
            button.product = product


    def press_entry(self, instance):
        """Handle what happens when product button is pressed."""
        product = instance.product
        cart_price += product.price



ProductsApp().run()