import flet as ft
from logic.ping.ping_logic import run_ping
from utils.state.state import State
from view.common.text import CustomTextField
import asyncio

class PingButton(ft.ElevatedButton):
    def __init__(self) -> None:
        self.ip = "172.16.64.1"
        super().__init__(text="Ping", on_click=self.ping)
        
    async def ping(self, e: ft.event) -> None:
        dialog_str: State[str] = State("実行中")
        
        ping_task = asyncio.create_task(run_ping(self.ip, dialog_str))
        
        dialog_task = asyncio.create_task(self.progress_dialog(dialog_str, ping_task))
        
        results = await asyncio.gather(ping_task, dialog_task)
        
        print(results)
        

    async def progress_dialog(self, dialog_str:State[str], wait_task: asyncio.Task) -> None:
        # Dialogの表示
        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("ping"),
            content=ft.Column([
                ft.ProgressRing(),
                CustomTextField(dialog_str, width=200, height=100),
            ])
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        
        # wait_taskが完了するまで画面を更新処理を無限ループ
        while not wait_task.done():
            await asyncio.sleep(0.1)
        
        # 完了したらDialogを閉じる
        self.page.dialog.open = False
        self.page.update()
