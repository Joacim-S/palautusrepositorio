import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

        
class PlayerReader:
    def __init__(self, url):
        self.url = url
        
    def get_players(self):
        response = requests.get(self.url).json()
        
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
            
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nation):
        players = self.reader.get_players()
        players.sort(key= lambda player: player.goals + player.assists, reverse=True)
        
        players_filtered = []
        
        for player in filter(lambda player: player.nation == 'FIN', players):
            players_filtered.append(player)
            
        return players_filtered
        
        
if __name__ == '__main__':
    main()