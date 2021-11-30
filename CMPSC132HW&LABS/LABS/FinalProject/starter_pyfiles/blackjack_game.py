from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        
        self.player_list = [] #make player list
        
        self.dealer = Dealer() #make dealer
        
        for i in player_names: #create players add to list
            
            j = Player(i, self.dealer)
            self.player_list.append(j)

        return None

    def play_rounds(self, num_rounds=1):
        """
        >>> import random; random.seed(1)
        >>> game = BlackjackGame(["Lawrence","Melissa"])
        >>> print(game.play_rounds(2))
        Round 1
        Dealer: [10, 9] 0/0/0
        Lawrence: [10, 6, 3] 0/1/0
        Melissa: [8, 8] 0/0/1
        Round 2
        Dealer: [10, 10] 0/0/0
        Lawrence: [10, 3] 0/1/1
        Melissa: [9, 10] 0/0/2
        """
        
        output = ""
        
        for i in range(num_rounds): #repeat for rounds
            
            j = 0 #cards
            
            self.dealer.shuffle_deck() #new deck
            self.dealer.hand = [] #empty hand
            
            for k in self.player_list: #players
                
                player = k #fresh hand
                player.hand = []
            
            while j < 2: #players have less than two cards
                
                for l in self.player_list: #get players to 2 cards default
                    
                    self.dealer.signal_hit(l)
                    
                self.dealer.signal_hit(self.dealer) #dealer gets after player
                
                j += 1
            
            for k in self.player_list: #players playround 
                player = k
                player.play_round()
            self.dealer.play_round() #dealer play round
            
            output += "Round " + str(i+1) + "\n" + str(self.dealer) + "\n" #string format
            for k in self.player_list:
                player = k
                if (player.card_sum > self.dealer.card_sum and player.card_sum <= 21) or self.dealer.card_sum > 21: #if player higher hand than dealer and hand <= 21 or dealer bust
                    player.record_win()
                elif (player.card_sum < self.dealer.card_sum and self.dealer.card_sum <= 21) or player.card_sum > 21:#if player hand lower than dealer and hand <= 21 or player bust
                    player.record_loss()
                elif player.card_sum == self.dealer.card_sum and player.card_sum <= 21: #if dealer and player equal hand and hand <= 21
                    player.record_tie()
                output += str(k) + "\n"
            
        return output[0:len(output)-1] #remove empty space

    def reset_game(self):
        """
        >>> game = BlackjackGame(["Lawrence", "Melissa"])
        >>> _ = game.play_rounds()
        >>> game.reset_game()
        >>> game.player_list[0]
        Lawrence: [] 0/0/0
        >>> game.player_list[1]
        Melissa: [] 0/0/0
        """
        for i in self.player_list: #reset stats and hand for each player
            
            i.reset_stats()
            i.discard_hand()
            
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()