class ScoreBoard:
    def __init__(self, player1, player2):
        self.points = {player1: 0, player2: 0}
        
    def won_point(self, player):
        self.points[player] += 1
    
    def generate_score(self, player1, player2):
        point_difference = self.get_difference(player1, player2)
        if point_difference == 0:
            return self.get_even_score(self.points[player1])
        
        leader = self.get_leader()
        if max(self.points.values()) >= 4:
            return self.get_late_game_score(point_difference, leader)
        
        player1_score = self.get_player_score(player1)
        player2_score = self.get_player_score(player2)
        
        return f"{player1_score}-{player2_score}"
    
    def get_late_game_score(self, difference, leader):
        if difference >= 2:
            return f"Win for {leader}"
        return f"Advantage {leader}"
    
    def get_difference(self, player1, player2):
        return abs(self.points[player1] - self.points[player2])
    
    def get_leader(self):
        return max(self.points, key=self.points.get)
    
    def get_even_score(self, points):
        if points >= 3:
            return "Deuce"
        scores = [
            "Love-All",
            "Fifteen-All",
            "Thirty-All",
        ]
        return scores[points]
    
    def get_player_score(self, player):
        scores = [
            "Love",
            "Fifteen",
            "Thirty",
            "Forty"
        ]
        return scores[self.points[player]]

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.scoreboard = ScoreBoard(player1, player2)

    def won_point(self, player):
        self.scoreboard.won_point(player)

    def get_score(self):
        return self.scoreboard.generate_score(self.player1, self.player2)

def get_difference(scores):
    return abs(p1_points - p2_points)
    
def get_even_score(points):
    if points >= 3:
        return "Deuce"
    scores = [
        "Love-All",
        "Fifteen-All",
        "Thirty-All",
    ]
    return scores[points]