#      Openfoot Manager - A free and open source soccer management game
#      Copyright (C) 2020-2022  Pedrenrique G. Guimarães
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
import random
import json
import logging

from ofm.core.api.game.team import Team
from ofm.core.api.game.player import Player
from ofm.core.api.game.match import Match
from ofm.core.api.game.match_live import MatchLive
from ofm.core.api.file_management import find_file
from ofm.core.api.generators.player_gen import PlayerParser


class Game:
    def __init__(self):
        self.players = None
        self.teams = []
        self.match = None
        self.match_live = None
        logging.basicConfig()
        self.logger = logging.getLogger(__file__)

    def run(self):
        player_parser = PlayerParser()


if __name__ == '__main__':
    game = Game()
    game.run()
