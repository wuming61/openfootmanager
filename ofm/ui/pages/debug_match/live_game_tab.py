#      Openfoot Manager - A free and open source soccer management simulation
#      Copyright (C) 2020-2023  Pedrenrique G. Guimarães
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview


class LiveGameTab(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.columns = [
            {"text": "Minutes", "stretch": True},
            {"text": "Commentary", "stretch": True},
        ]

        self.default_rows = [
            ("0.00", "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
        ]

        self.output = Tableview(
            self,
            coldata=self.columns,
            rowdata=self.default_rows,
            searchable=False,
            autofit=True,
            paginated=False,
            pagesize=1000,
            height=15,
        )
        self.output.grid(row=0, column=0, sticky=EW)

    def update_table(self, data):
        self.output.insert_row(data)

    def reset_table(self, data):
        self.output.destroy()
        self.output = Tableview(
            self,
            coldata=self.columns,
            rowdata=self.default_rows,
            searchable=False,
            autofit=True,
            paginated=False,
            pagesize=1000,
            height=11,
        )
        self.output.grid(row=0, column=0, sticky=EW)
