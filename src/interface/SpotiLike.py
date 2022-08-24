import asyncio

from api.database import Database
from api.main import SpotiLikeAPI

from textual.app import App
from textual.widgets import Header, Footer, Placeholder


from .widgets import CMD, PlaylistView, MainView
from .commands import command_list


class SpotiLike(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.db = Database()

        # self.api = SpotiLikeAPI()
        # self.api.run()

    async def on_load(self):

        await self.bind("b", "view.toggle('sidebar')", "Show/Hide playlists")
        await self.bind("/", "focus_command_area()", "Focus Command Area.")
        await self.bind("q", "quit", "Quit")

    async def action_focus_command_area(self):

        await self.command_area.focus()

    async def on_mount(self):
        # await self.view.dock(Footer(), edge="bottom")
        # await self.view.dock(
        #     Header(tall=False, style="dark_goldenrod on black"), edge="top"
        # )

        self.command_area = CMD()
        self.playlists_view = PlaylistView(db=self.db)
        self.status = Placeholder()  # TODO Status
        self.main_view = MainView()  # TODO # DOING

        await self.view.dock(self.status, size=25, edge="right")
        await self.view.dock(self.playlists_view, size=25, edge="left", name="sidebar")
        await self.view.dock(self.command_area, edge="bottom", size=3)

        await self.view.dock(self.main_view, edge="top")
