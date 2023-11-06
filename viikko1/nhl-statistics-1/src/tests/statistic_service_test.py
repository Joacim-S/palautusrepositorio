import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
        
    def test_search_palauttaa_oikean_pelaajan(self):
        result = self.stats.search('Kurri')
        
        self.assertAlmostEqual(result.name, 'Kurri')
        
    def test_haku_palauttaa_none_kun_pelaajaa_ei_löydy(self):
        result = self.stats.search('Mummi')
        
        self.assertAlmostEqual(result, None)
        
    def test_team_palauttaa_oikean_listan(self):
        result = self.stats.team('EDM')
        expected = ('Semenko', 'Kurri', 'Gretzky')

        for i, player in enumerate(result):
            self.assertAlmostEqual(player.name, expected[i])
            
    def test_top_palauttaa_oikeat_pelaajat(self):
        result = self.stats.top(2)
        expected = ('Gretzky', 'Lemieux', 'Yzerman')

        for i, player in enumerate(result):
            self.assertAlmostEqual(player.name, expected[i])
            
    def test_top_goals_toimii(self):
        result = self.stats.top(0, SortBy.GOALS)
        self.assertEqual(result[0].name, 'Lemieux')
        
    def test_top_assists_toimii(self):
        result = self.stats.top(0, SortBy.ASSISTS)
        self.assertEqual(result[0].name, 'Gretzky')
        
    def test_top_points_toimii(self):
        result = self.stats.top(0, SortBy.POINTS)
        self.assertEqual(result[0].name, 'Gretzky')