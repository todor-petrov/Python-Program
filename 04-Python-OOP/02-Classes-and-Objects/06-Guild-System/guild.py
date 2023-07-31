from player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, pl: Player):
        if pl in self.players:
            return f'Player {pl.name} is already in the guild.'
        if pl.guild != 'Unaffiliated' and pl.guild != self.name:
            return f'Player {pl.name} is in another guild.'
        pl.guild = self.name
        self.players.append(pl)
        return f'Welcome player {pl.name} to the guild {self.name}'

    def kick_player(self, player_name):
        for pl in self.players:
            if pl.name == player_name:
                pl.guild = 'Unaffiliated'
                self.players.remove(pl)
                return f'Player {player_name} has been removed from the guild.'
        return f'Player {player_name} is not in the guild.'

    def guild_info(self):
        info = [f'Guild: {self.name}']
        for p in self.players:
            info.append(p.player_info())
        nl = '\n'
        return f'{nl.join(info)}'
