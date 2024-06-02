import flet as ft
from utils.state.state import State
from view.common.text import CustomTextField
from logic.num_display.num_display_logic import NumDisplayLogic

class NumDisplay(ft.Row):
    """インクリメント、デクリメントの機能を持つコントロール
    """
    def __init__(self) -> None:
        super().__init__()
        # 表示するデータの初期化
        self.text = State("0")
        # 計算ロジッククラスをインスタンス化
        self.logic = NumDisplayLogic(self.text)
        
        # 各種コントロールのインスタンスを作成
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
        self.logic.decrement()
        
    def plus_click(self, e) -> None:
        # インクリメント 
        self.logic.increment()