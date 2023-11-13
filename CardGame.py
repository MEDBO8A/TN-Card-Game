import random as np
np.seed(619)

class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit

class Deck:
    def __init__(self):
        self.cards=[]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for i in range(57):
            rank=np.choice(ranks)
            suit=np.choice(suits)
            card=Card(rank=rank,suit=suit)
            self.cards.append(card)

    def getDeck(self):
        for d in self.cards:
            print(d.rank + " " + d.suit)

    def shuffle(self):
        np.shuffle(self.cards)
    
    def draw(self):
        if self.cards:
            return self.cards.pop(0)
        print("There is no cards")
        return None
    
class Game:
    def __init__(self,gameName):
        self.gameName=gameName

    def rank_to_value(self, rank):
        rank_values = {'A': 1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
        return rank_values.get(rank) 

class SaharaAce(Game):
    def __init__(self):
        super().__init__("Sahara Ace")
    def play(self,deck):
        card=deck.draw()
        if card.rank=="A":
            return 10
        return 0

class TunisianTwins(Game):
    def __init__(self):
        super().__init__("Tunisian Twins")
    def play(self,deck):
        card1=deck.draw()
        card2=deck.draw()
        if card1.rank==card2.rank or card1.suit==card2.suit :
            return 50
        return 0

class MedinaBiggie(Game):
    def __init__(self):
        super().__init__("Medina Biggie")
    def play(self,deck):
        card1=deck.draw()
        card2=deck.draw()
        if self.rank_to_value(card2.rank)>self.rank_to_value(card1.rank):
            return 2
        return 0
class DesertHearts(Game):
    def __init__(self):
        super().__init__("Desert Hearts")
    def play(self,deck):
        card1=deck.draw()
        card2=deck.draw()
        card3=deck.draw()
        amount=0
        if card1.suit=="Hearts":
            amount+=self.rank_to_value(card1.rank)
        if card2.suit=="Hearts":
            amount+=self.rank_to_value(card2.rank)
        if card3.suit=="Hearts":
            amount+=self.rank_to_value(card3.rank)
        return amount

class OasisRunny(Game):
    def __init__(self):
        super().__init__("Oasis Runny")
    def play(self,deck):
        cards=[]
        for i in range(5):
            cards.append(deck.draw())
        ranksValue=[]
        for card in cards:
            ranksValue.append(self.rank_to_value(card.rank))
        ranksValue.sort()
        
        for i in range(3):
            if ranksValue[i+2]-ranksValue[i+1]-ranksValue[i] == 0:
                return 5
        return 0

class ElHaiaCard(Game):
    def __init__(self):
        super().__init__("Student Game")
    def play(self,deck):
        cards=[]
        for i in range(3):
            cards.append(deck.draw())
        ranksValue=[]
        for card in cards:
            ranksValue.append(self.rank_to_value(card.rank))
        
        if 7 in ranksValue and sum(ranksValue)==10 :
            return 100
        return 0


def monte_carlo():
    games = [SaharaAce(), TunisianTwins(), MedinaBiggie(), DesertHearts(), OasisRunny(), ElHaiaCard()]
    
    print("+-------------------+-------------------------+-------------------------------+---------------------------------+")
    print("| Game              | Probability of Winning  | Expected Winnings per Play    | Total Money Earned              |")
    print("+-------------------+-------------------------+-------------------------------+---------------------------------+")

    for game in games:
        wins = 0
        total_winnings = 0
        
        for _ in range(100000):
            deck = Deck()
            deck.shuffle()
            winnings = game.play(deck)
            if winnings>0:
                wins+=1
            total_winnings += winnings

        probability_of_winning = (wins / 100000)*100
        expected_winnings_per_play = total_winnings / 100000

        print(f"| {game.gameName.ljust(17)} | {probability_of_winning:2.1f}%                   | {expected_winnings_per_play:.2f}  Tunisian dinars         | {total_winnings:.2f} Tunisian dinars        |")

    print("+-------------------+-------------------------+-------------------------------+---------------------------------+")

monte_carlo()