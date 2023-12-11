class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass
    
    def test(self, player):
        return True
    
class Not:
    def __init__(self, matcher):
        self._matcher = matcher
        
    def test(self, player):
        return not self._matcher.test(player)
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
        
    def test(self, player):
        return Not(HasAtLeast(self._value, self._attr)).test(player)
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False
    
class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_object = matcher
        
    def build(self):
        return self._matcher_object

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matcher_object))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._matcher_object))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._matcher_object))
    
    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))
