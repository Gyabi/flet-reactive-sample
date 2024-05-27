import flet as ft
from state.state import State
from controls.common.text import CustomTextField

class NumDisplay(ft.Row):
    """インクリメント、デクリメントの機能を持つコントロール
    """
    def __init__(self) -> None:
        super().__init__()
        # 各種コントロールのインスタンスを作成
        self.text = State("0")
        self.txt_number = CustomTextField(value_state=self.text, text_align=ft.TextAlign.RIGHT, width=100, read_only=True)
        self.button_minus = ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click)
        self.button_plus = ft.IconButton(ft.icons.ADD, on_click=self.plus_click)
        # コントロールを親クラスのcontrolsリストに追加
        self.controls = [
            self.button_minus,
            self.txt_number,
            self.button_plus,
        ]
        self.alignment = ft.MainAxisAlignment.CENTER

    def minus_click(self, e) -> None: 
        # デクリメント
        self.text.set(str(int(self.text.get()) - 1))
        
    def plus_click(self, e) -> None:
        # インクリメント 
        self.text.set(str(int(self.text.get()) + 1))