"""
CP1404 Seminar 8
"""
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class ShoppingApp(App):
    """Shopping app class."""

    def __init__(self, **kwargs):
        """Construct main kivy app."""
        super().__init__(**kwargs)
        Window.size = (800, 600)
        self.title = "Shopping App"

    def build(self):
        """Build main kivy app."""
        Window.size = (800, 600)
        self.title = "Shopping App"



    def create_widgets(self):
        """Create widgets from ***."""
