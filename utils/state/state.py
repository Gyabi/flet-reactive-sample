from typing import TypeVar, Generic, Callable

# ジェネリック用
T = TypeVar('T')

"""データの状態遷移をフック可能とするためのデータラッパークラス
"""
class State(Generic[T]):
    def __init__(self, value:T) -> None:
        """constructor

        Args:
            value (T): 初期値
        """
        self._value = value
        self._observers: list[Callable] = []
        
    def get(self) -> T:
        """getter

        Returns:
            T: 現在の値
        """
        return self._value
    
    def set(self, value:T) -> None:
        """setter

        Args:
            value (T): 設定する値
        """
        self._value = value
        self._notify()
        
    def observe(self, observer:Callable) -> None:
        """監視関数を登録する

        Args:
            observer (Callable): 監視関数
        """
        self._observers.append(observer)
    
    def _notify(self) -> None:
        """監視関数を呼び出す
        """
        for observer in self._observers:
            observer(self._value)
    
    def unobserve(self, observer:Callable) -> None:
        """監視関数を解除する

        Args:
            observer (Callable): 解除する監視関数
        """
        self._observers.remove(observer)
