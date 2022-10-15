from ..widgets import MainView
import pyfiglet


# TODO: Create Methods for all commands
# TODO: Arguments are based on method positional args
# TODO: Create command description based on doc strings
# TODO: parse_args method must check argument validation and number of args inputted by checking against command methods (Use inspect)


class CommandParser:
    def __init__(self):
        self.command_list = [
            "help",
            "download",
            "autosave",
            "export_track_list",
            "logout",
            "reset_database",
            "autobackup",
            "home",
        ]

    def error(self, code: int, cmd: str):
        base = f"""
[red][bold]{pyfiglet.figlet_format("ERROR", font="cosmic")}[/bold][/red]\n\n\n\n\n        
"""

        if code == 1:
            message = f" [purple]Error code {code}[/purple]\n\n[b]No command named [yellow]{cmd}[/yellow] found![/b] Perhaps you did a typo.\n\n Return to home instruction page by typing `home` or use `help` to see a list of commands."

        return self.view.update(base + message)

    def parse_args(self, cmd: str):
        args = list(filter(None, cmd.split(" ")))
        return args

    async def command(self, cmd: str, main_view: MainView):
        self.view = main_view
        parsed = self.parse_args(cmd.lower())
        if parsed[0] not in self.command_list:
            return await self.error(code=1, cmd=cmd)

        await getattr(self, parsed[0])(parsed)
