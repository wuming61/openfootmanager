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
import pytest
from ofm.core.football.player import PlayerTeam, Player, PlayerSimulation, Positions
from ofm.core.football.formation import Formation, FormationError
from .test_player import  get_player_team


def test_invalid_formation():
    with pytest.raises(FormationError):
        Formation("4-4-3")


def test_add_gk_to_formation():
    formation = Formation("4-4-2")
    player, _, __ = get_player_team()
    formation.add_player(0, player)
    assert formation.gk.player == player
    assert formation.gk.current_position == Positions.GK


def test_add_df_to_formation():
    formation = Formation("4-4-2")
    for i in range(4):
        player, _, __ = get_player_team()
        formation.add_player(i + 1, player)
        assert formation.df[i].player == player
        assert formation.df[i].current_position == Positions.DF


def test_add_mf_to_formation():
    formation = Formation("4-4-2")
    for i in range(4):
        player, _, __ = get_player_team()
        formation.add_player(i + 5, player)
        assert formation.mf[i].player == player
        assert formation.mf[i].current_position == Positions.MF


def test_add_fw_to_formation():
    formation = Formation("4-4-2")
    for i in range(2):
        player, _, __ = get_player_team()
        formation.add_player(i + 9, player)
        assert formation.fw[i].player == player
        assert formation.fw[i].current_position == Positions.FW