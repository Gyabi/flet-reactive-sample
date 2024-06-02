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
    

class NavigationView(ft.Row):
    """ナビゲーションメニューを表示するコントロール

    Args:
        ft (_type_): _description_
    """
    def __init__(self, navigation_datas:List[NavigationData] = []) -> None:
        super().__init__()
        self.navigation_datas = navigation_datas
              
        
        # mainの表示エリア
        self.main_area = ft.Column(
            controls=[self.navigation_datas[0].control if len(self.navigation_datas) > 0 else None],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
        )
        
        # navigationメニューを作成
        self.navigation_rail_destinations: List[ft.NavigationRailDestination] = [
            ft.NavigationRailDestination(
                icon=nav_data.icon,
                label=nav_data.title,
            ) for nav_data in self.navigation_datas
        ]
        
        # ドロワーの定義
        self.navigation_rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=self.navigation_rail_destinations,
            on_change=self.on_click_navigation_rail_item,
        )
        
        # ft.Columnの要素を設定
        self.expand=True
        self.controls = [
                self.navigation_rail,
                ft.VerticalDivider(width=1),
                self.main_area,
            ]

    def on_click_navigation_rail_item(self, e:ft.ControlEvent) -> None:
        """ナビゲーションメニューがクリックされた際の処理

        Args:
            e (ft.ControlEvent): イベント
        """
        index = int(e.data)
        if len(self.navigation_datas) <= index:
            return
        
        self.main_area.controls = [self.navigation_datas[index].control]
        self.main_area.update()
