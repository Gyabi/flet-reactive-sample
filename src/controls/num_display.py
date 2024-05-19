import flet as ft

class NumDisplay(ft.Row):
    def __init__(self):
        super().__init__()
        # 各種コントロールのインスタンスを作成
        self.txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
        self.button_minus = ft.IconButton(ft.icons.REMOVE, on_click=self.minus_click)
        self.button_plus = ft.IconButton(ft.icons.ADD, on_click=self.plus_click)
        
        # コントロールを親クラスのcontrolsリストに追加
        self.controls = [
            self.button_minus,
            self.txt_number,
            self.button_plus,
        ]
        self.alignment = ft.MainAxisAlignment.CENTER

    def minus_click(self, e):
        # デクリメント
        self.txt_number.value = str(int(self.txt_number.value) - 1) 
        # 表示されている数値を更新
        self.txt_number.update()
        
    def plus_click(self, e):
        # インクリメント 
        self.txt_number.value = str(int(self.txt_number.value) + 1)
        # 表示されている数値を更新
        self.txt_number.update() 