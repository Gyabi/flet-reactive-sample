import flet as ft
from view.num_display.num_display import NumDisplay
from view.navigation.navigation_rail import NavigationView, NavigationData
from view.dummy.dummy import Dummy

def main(page: ft.Page):
    page.title = "sample app"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {
        "Roboto Mono": "RobotoMono-VariableFont_wght.ttf",
    }
    
    # NumDisplayをインスタンス化
    num_display = NumDisplay()
    
    # ダミーをインスタンス化
    dummy = Dummy()
    
    # ナビゲーションメニューをインスタンス化
    nav = NavigationView(
        navigation_datas = [
            NavigationData(
                title="NumDisplay",
                icon=ft.icons.ADD,
                control=num_display,
            ),
            NavigationData(
                title="Dummy",
                icon=ft.icons.ADD,
                control=dummy,
            ),
        ],
    )
    
    page.add(nav)
            
ft.app(main)