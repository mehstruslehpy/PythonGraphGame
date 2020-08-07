# Game start:
	- A random graph is generated at the start of the game.
	- Player 1 is red player 2 is blue, each player has characters placed randomly in the graph at the start of the game.

# During a players turn:
	- A player can choose to move one of their own characters or do nothing.
	- Moving a character to a like colored vertex does nothing.
	- Moving a character to a green vertex zeroes the source node and accumulates the sum of the points into the destination node
	- Moving a character to an opponents node subtracts the nodes points from each other and places the difference at that node (the absolute value of the difference), the character with the higher amount of points stays in play at that node

# The game ends when:
	- Only one player has characters left in play, the player with remaining characters wins.
	- If no players have characters left in play the game is a draw.
