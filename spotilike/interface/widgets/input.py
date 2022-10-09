from textual_inputs import TextInput
from textual.reactive import Reactive

from ...api.utils.format_hotkey import unformat


class CMD(TextInput):
    def __init__(self):
        super().__init__()
        self.name = "cmd"
        self.title = "Command Area"
        self.placeholder = "Enter command [see help for more]"
        self.style = "bright_yellow"
        self.border_style = "cyan"
        self.on_change_handler_name = "handle_cmd"


class PlaylistInput(TextInput):
    mouse_over = Reactive(False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("playlist_id")
        self.title = kwargs.get("playlist_name")

        if not kwargs.get("hotkey"):
            self.placeholder = "No hotkey"
        else:
            self.value = unformat(kwargs.get("hotkey"))

        self.border_style = "cyan"
        self.on_change_handler_name = "handle_text_input"

    def on_enter(self):
        self.mouse_over = True

    def on_leave(self):
        self.mouse_over = False

    def render(self):
        panel = super().render()
        panel.style = "on yellow3" if self.mouse_over else "cyan"

        return panel
