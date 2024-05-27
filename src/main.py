import flet as ft
from controls.num_display import NumDisplay
from controls.navigation.navigation_drawer import NavigationView, NavigationData

def main(page: ft.Page):
    page.title = "sample app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    # NumDisplayをインスタンス化
    num_display = NumDisplay()
    
    # ダミー画面をインスタンス化
    dummy_page = ft.Column(
        controls=[ft.Text("Dummy page")]
    )
    
    # 画面の定義
    nav = NavigationView(
        navigation_datas=[
            NavigationData(
                title="Counter",
                icon=ft.icons.ADD,
                control=num_display,
            ),
            NavigationData(
                title="Dummy",
                icon=ft.icons.ADD,
                control=dummy_page,
            ),
        ],
        headers=[ft.Text("sample app")],
    )
    
    # ページに追加
    page.add(nav)

ft.app(target=main)