import flet as ft
from controls.num_display import NumDisplay

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    

    # NumDisplayをインスタンス化
    num_display = NumDisplay()
    # ページに追加
    page.add(num_display)

ft.app(target=main)