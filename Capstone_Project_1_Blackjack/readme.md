# Blackjack Game

This is a single-player blackjack game where you compete against the computer.

## Objective of the Game

You attempt to beat the dealer (the computer) by getting a count as close to 21 as possible without going over 21.

- 2 through 10 cards count at face value, i.e. 2 counts as two, 9 counts as nine.
- Face cards (J, Q, K) count as 10.
- Ace can count as a 1 or an 11 depending on which value helps the hand the most.

**You beat the dealer:**

1. when you draw a hand value higher than the dealer’s hand value.
2. when the dealer draws a hand value that goes over 21.
3. when you draw a hand value of 21 on your first two cards when the dealer does not.

**You lose when:**

1. your hand value exceeds 21.
2. the dealer's hand has a greater value than yours at the end of the round.


If you want to play this game online, go to this [link](https://games.washingtonpost.com/games/blackjack/).

There are many resources online where you can learn more about the rules. One such resource is [this](https://bicyclecards.com/how-to-play/blackjack/).

---

## Our Blackjack House Rules 

- The deck is unlimited in size.
- There are no jokers.
- The Jack/Queen/King all count as 10.
- The Ace can count as 11 or 1.
- The following is a list that represents the deck of cards:
```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  ```
- The cards in the list have an equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.










