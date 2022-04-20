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
from uuid import UUID
from dataclasses import dataclass
from .player import PlayerSimulation
from .formation import Formation


@dataclass
class Team:
    team_id: UUID
    name: str
    roster: list
    stadium: str
    is_players_team: bool

    def get_roster_in_player_simulator_objects(self) -> list[PlayerSimulation]:
        return [PlayerSimulation(player, player.get_current_skill()) for player in self.roster]


@dataclass
class TeamSimulation:
    team: Team
    players: list[PlayerSimulation]
    bench: list[PlayerSimulation]
    formation: Formation
    in_possession: bool = False
    score: int = 0

    def substitute_player(self, player1: PlayerSimulation, player2: PlayerSimulation):
        pass

    def remove_player(self, player: PlayerSimulation):
        """
        Remove player if it got injured, or received a red card.
        :param player:
        :return:
        """
        self.players.remove(player)


@dataclass
class TeamStats:
    shots: int = 0
    fouls: int = 0
    goals: int = 0
    own_goals: int = 0
    penalties: int = 0
    injuries: int = 0
    yellow_cards: int = 0
    red_cards: int = 0
    avg_rating: float = 0.0
    possession: float = 0.0
