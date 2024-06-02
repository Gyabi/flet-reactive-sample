import subprocess
import os
import asyncio
from utils.state.state import State

def subprocess_args(include_stdout=True):
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

async def run_ping(ip, message:State[str]) -> str:
    command = ['ping', '-n', '1', ip]
    try:
        output = subprocess.run(command, **subprocess_args(True), text=True, encoding='cp932')
        message.set("ping success")
        await asyncio.sleep(1)
        message.set("sleep success")
        
        return output.stdout
    except subprocess.CalledProcessError as e:
        return f"Ping failed: {e.output}"