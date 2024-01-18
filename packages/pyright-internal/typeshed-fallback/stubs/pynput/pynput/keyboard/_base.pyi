import contextlib
import enum
import sys
from collections.abc import Callable, Iterable, Iterator
from typing import Any, ClassVar
from typing_extensions import Self

from pynput._util import AbstractListener

class KeyCode:
    _PLATFORM_EXTENSIONS: ClassVar[Iterable[str]]  # undocumented
    vk: int | None
    char: str | None
    is_dead: bool | None
    combining: str | None
    def __init__(self, vk: str | None = None, char: str | None = None, is_dead: bool = False, **kwargs: str) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def join(self, key: Self) -> Self: ...
    @classmethod
    def from_vk(cls, vk: int, **kwargs: Any) -> Self: ...
    @classmethod
    def from_char(cls, char: str, **kwargs: Any) -> Self: ...
    @classmethod
    def from_dead(cls, char: str, **kwargs: Any) -> Self: ...

class Key(enum.Enum):
    alt = ...
    alt_l = ...
    alt_r = ...
    alt_gr = ...
    backspace = ...
    caps_lock = ...
    cmd = ...
    cmd_l = ...
    cmd_r = ...
    ctrl = ...
    ctrl_l = ...
    ctrl_r = ...
    delete = ...
    down = ...
    end = ...
    enter = ...
    esc = ...
    f1 = ...
    f2 = ...
    f3 = ...
    f4 = ...
    f5 = ...
    f6 = ...
    f7 = ...
    f8 = ...
    f9 = ...
    f10 = ...
    f11 = ...
    f12 = ...
    f13 = ...
    f14 = ...
    f15 = ...
    f16 = ...
    f17 = ...
    f18 = ...
    f19 = ...
    f20 = ...
    if sys.platform == "win32":
        f21 = ...
        f22 = ...
        f23 = ...
        f24 = ...
    home = ...
    left = ...
    page_down = ...
    page_up = ...
    right = ...
    shift = ...
    shift_l = ...
    shift_r = ...
    space = ...
    tab = ...
    up = ...
    media_play_pause = ...
    media_volume_mute = ...
    media_volume_down = ...
    media_volume_up = ...
    media_previous = ...
    media_next = ...
    insert = ...
    menu = ...
    num_lock = ...
    pause = ...
    print_screen = ...
    scroll_lock = ...

class Controller:
    _KeyCode: ClassVar[type[KeyCode]]  # undocumented
    _Key: ClassVar[type[Key]]  # undocumented

    if sys.platform == "linux":
        CTRL_MASK: ClassVar[int]
        SHIFT_MASK: ClassVar[int]

    class InvalidKeyException(Exception): ...
    class InvalidCharacterException(Exception): ...

    def __init__(self) -> None: ...
    def press(self, key: str | Key | KeyCode) -> None: ...
    def release(self, key: str | Key | KeyCode) -> None: ...
    def tap(self, key: str | Key | KeyCode) -> None: ...
    def touch(self, key: str | Key | KeyCode, is_press: bool) -> None: ...
    @contextlib.contextmanager
    def pressed(self, *args: str | Key | KeyCode) -> Iterator[None]: ...
    def type(self, string: str) -> None: ...
    @property
    def modifiers(self) -> contextlib.AbstractContextManager[Iterator[set[Key]]]: ...
    @property
    def alt_pressed(self) -> bool: ...
    @property
    def alt_gr_pressed(self) -> bool: ...
    @property
    def ctrl_pressed(self) -> bool: ...
    @property
    def shift_pressed(self) -> bool: ...

class Listener(AbstractListener):
    def __init__(
        self,
        on_press: Callable[[Key | KeyCode | None], None] | None = None,
        on_release: Callable[[Key | KeyCode | None], None] | None = None,
        suppress: bool = False,
        **kwargs: Any,
    ) -> None: ...
    def canonical(self, key: Key | KeyCode) -> Key | KeyCode: ...
