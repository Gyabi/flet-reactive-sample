import flet as ft
from dataclasses import dataclass
from typing import List

@dataclass
class NavigationData:
    """
    ナビゲーションのデータクラス
    
    Attributes
    ----------
    title : str
        ナビゲーションのタイトル
    icon : ft.Icon
        ナビゲーションのアイコン
    page : ft.Control
        ナビゲーションが選択された際に表示するページ
    """
    title: str
    icon: ft.Icon
    control: ft.Control
    

class NavigationView(ft.Column):
    """ナビゲーションメニューを表示するコントロール

    Args:
        ft (_type_): _description_
    """
    def __init__(self, navigation_datas:List[NavigationData] = [], headers:List[ft.Control] = []) -> None:
        super().__init__()
        self.navigation_datas = navigation_datas
        self.headers = headers
        
        # ハンバーガーボタン
        self.humburger = ft.IconButton(
            icon=ft.icons.MENU_SHARP,
            on_click=self.open_drawer,
        )
              
        # ヘッダー  
        self.header = ft.Row(
            controls=[
                self.humburger,
                *self.headers
            ],
            alignment=ft.MainAxisAlignment.START,
        )
        
        # mainの表示エリア
        self.main_area = ft.Column(
            controls=[self.navigation_datas[0].control if len(self.navigation_datas) > 0 else None],
        )
        
        # navigationメニューを作成
        self.navigation_controls: List[ft.Control] = [
            ft.NavigationDrawerDestination(
                icon=content.icon,
                label=content.title,
            ) for i, content in enumerate(self.navigation_datas)
        ]
        
        # ドロワーの定義
        self.drawer = ft.NavigationDrawer(
            controls=self.navigation_controls,
            on_change=self.on_click_navigation_drawer_item,
        )
        
        # ft.Columnの要素を設定
        self.expand=True
        self.controls = [
                self.header,
                self.main_area
            ]
        
    def did_mount(self) -> None:
        """コンポーネントがマウントされた際に呼び出されるコールバック
        """
        self.page.drawer = self.drawer
        self.page.update()
        super().did_mount()
        
    def open_drawer(self, e:ft.ControlEvent) -> None:
        """ドロワー有効化

        Args:
            e (ft.ControlEvent): イベント
        """
        self.drawer.open = True
        self.drawer.update()

    def on_click_navigation_drawer_item(self, e:ft.ControlEvent) -> None:
        """ナビゲーションメニューがクリックされた際の処理

        Args:
            e (ft.ControlEvent): イベント
        """
        index = int(e.data)
        if len(self.navigation_datas) <= index:
            return
        
        self.page.drawer = False
        self.main_area.controls = [self.navigation_datas[index].control]
        self.main_area.update()
