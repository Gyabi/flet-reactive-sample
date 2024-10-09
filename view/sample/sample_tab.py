import flet as ft



class SampleTab(ft.Column):
    def __init__(self):
        buttons = ft.Column([
                ft.Row([ft.CupertinoFilledButton("aaaaaa", expand=True)]),
                ft.Row([ft.CupertinoFilledButton("bbb", expand=True)]),
                ft.Row([ft.CupertinoFilledButton("cccccccc", expand=True)]),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.CENTER)
        button_area = ft.Container(buttons, bgcolor=ft.colors.BLUE_ACCENT,expand=3,padding=20)
        
        texts = ft.Column([
            ft.Text("dskjfasl"),
            ft.Text("dskjfasl"),
            ft.Text("dskjfasl"),
            ft.Text("dskjfasl"),
        ],expand=True, alignment=ft.MainAxisAlignment.CENTER)
        buttons2 = ft.Column([
            ft.Row([ft.CupertinoFilledButton("aaaaaa", expand=True)]),
            ft.Row([ft.CupertinoFilledButton("bbb", expand=True)]),       
        ],expand=True, alignment=ft.MainAxisAlignment.CENTER)
        
        r = ft.Row([
            texts,
            buttons2
        ],expand=True)
        text_area = ft.Container(r,bgcolor=ft.colors.AMBER, expand=5, padding=40)
        
        first = ft.Row([
                        button_area,
                        text_area
                    ],
                       expand=2,
                       alignment=ft.MainAxisAlignment.CENTER,
                       spacing=30
                )
        
        second = ft.Row([
            ft.Container(
                ft.Column([
                    ft.Text("sample"),
                    ], alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=ft.colors.DEEP_PURPLE_ACCENT,
                expand=True
            )
        ], expand=3, alignment=ft.MainAxisAlignment.CENTER)
        
        super().__init__(controls=[first, second], expand=True)