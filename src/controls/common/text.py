import flet as ft
from state.state import State

class CustomTextField(ft.TextField):
    """カスタムテキストフィールド
    """
    def __init__(self, value_state:State[str], **kwargs) -> None:
        """constructor

        Args:
            value_state (State[str]): テキストフィールドの値を管理するState
        """
        super().__init__(value=value_state.get(), **kwargs)
        self.value_state = value_state
        
    def value_observer(self, value:str) -> None:
        """value_stateの値が変更された際に呼び出されるコールバック

        Args:
            value (str): value_stateの値
        """
        self.value = value
        self.update()
        
    def did_mount(self) -> None:
        """コンポーネントがマウントされた際に呼び出されるコールバック
        """
        self.value_state.observe(self.value_observer)
        self.value_observer(self.value_state.get())
        super().did_mount()
    
    def will_unmount(self) -> None:
        """コンポーネントがアンマウントされる際に呼び出されるコールバック
        """
        self.value_state.unobserve(self.value_observer)
        super().will_unmount()
