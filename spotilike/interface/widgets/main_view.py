from textual.widgets import ScrollView

from rich.text import Text

import pyfiglet


class MainView(ScrollView):
    def __init__(self, *args, **kwargs):
        super().__init__(contents=self.welcome_text(), *args, **kwargs)

    def welcome_text(self) -> str:
        logo = pyfiglet.figlet_format("SpotiLike <3", font="big")

        text = f"""
        
                                
[green1][b]{logo}[/b][/green1]

 Hey! Welcome to [sea_green2]SpotiLike[/sea_green2]. I'm not that good with colors obviously
        
        [cyan1]To start off, click one of your [cyan]playlists[/cyan] in the left hand side[/cyan1].
        
            > [dark_slate_gray3]Once clicked, you will be able to edit the value inside each playlist.[/dark_slate_gray3]
            
            > [dark_slate_gray3]These values are clearly hotkeys.[/dark_slate_gray3]
            
            > [dark_slate_gray3]You just need to type out the hotkey by using '+' as the separator[/dark_slate_gray3]
                [italic]Here are a few examples:[/italic]
            
                >> [light_cyan1]Invoke save by pressing 'ctrl' and 'l' together[/light_cyan1] 
                            -> [green_yellow]ctrl + l[/green_yellow]
                >> [light_cyan1]Invoke save by pressing 'ctrl' and 'shift' and 'a' and 'b' together[/light_cyan1]
                            -> [green_yellow]ctrl + shift + a + b[/green_yellow]
                >> [light_cyan1]Invoke save by media key - 'media volume up` and 'media volume down' together[/light_cyan1]
                            -> [green_yellow]media_volume_down + media_volume_up[/green_yellow]
                >> [light_cyan1]Invoke save with one letter[/light_cyan1] 
                            -> [green_yellow]f[/green_yellow]
                >> [light_cyan1]I don't want to invoke a playlist with any key[/light_cyan1]
                            -> [green_yellow]Just leave it blank or 'none'[/green_yellow]

        
        [cyan1]What commands can I use[/cyan1]
        
            > [dark_slate_gray3]To see a list of available commands, type [bright_yellow]help[/bright_yellow] in the command area and hit enter[/dark_slate_gray3]
            
            :warning: Not implemented.
"""

        return Text.from_markup(text)
