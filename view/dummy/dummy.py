import flet as ft
from view.dummy.ping_button import PingButton

class Dummy(ft.Column):
    def __init__(self) -> None:
        self.text_ = ft.Text("Dummy")
        self.ping_button = PingButton()
            
        super().__init__([self.text_, self.ping_button])