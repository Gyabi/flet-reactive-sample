import flet as ft
import subprocess

import os

def subprocess_args(include_stdout=True):
    # The following is true only on Windows.
    if hasattr(subprocess, 'STARTUPINFO'):
        info = subprocess.STARTUPINFO()
        info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        env = os.environ
    else:
        info = None
        env = None
    
    if include_stdout:
        return {'stdout': subprocess.PIPE,
                'stdin': subprocess.PIPE,
                'stderr': subprocess.PIPE,
                'startupinfo': info,
                'env': env }
    else:
        return {'stdin': subprocess.PIPE,
                'stderr': subprocess.PIPE,
                'startupinfo': info,
                'env': env}
        
class PingRow(ft.Row):
    def __init__(self):
        super().__init__()
        self.ip_address_input = ft.TextField(label="IP Address", value="127.0.0.1")
        self.result_output = ft.Text(value="")
        self.ping_button = ft.ElevatedButton(text="Ping", on_click=self.ping)
        
        self.controls.extend([
            self.ip_address_input,
            self.ping_button,
            self.result_output
        ])

    def ping(self, e):
        ip = self.ip_address_input.value
        self.result_output.value = self.run_ping(ip)
        self.update()
        
    @staticmethod
    def run_ping(ip):
        command = ['ping', '-n', '1', ip]
        try:
            output = subprocess.run(command, **subprocess_args(True), text=True, encoding='cp932')
            return output.stdout
        except subprocess.CalledProcessError as e:
            return f"Ping failed: {e.output}"
