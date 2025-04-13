# Retro_Pong_Go!🏓

## Repository
<https://github.com/DannaBanuelos/Retro_Pong_Go.git >

## Retro Pong Go! A virtual Ping Pong game that puts 2 players against each other. Based on the famous Pong from Atari, this game creates an interactive board where points are counted and the level rises until there's a WINNER!

![image](https://github.com/user-attachments/assets/8482c08f-4efc-43f5-9cf9-52a7544682ca)

## Features
- Interactive Virtual Board 
	- Generates a virtual Board using Python `pygame` 
- Interactive Audio Input
	- Game plays sound when interacting with its environment using `pyaudio`/ `sounddevice` 
- Level Up
	- Game level up 1 level each time a player wins a match with `pygame`
- Point Counter
	- Each player must win 5 points to win a match, and each player must win 2 matches to win the GAME!


## Challenges
- Getting the program to level up depending on the players results
- Develop an interactive audio output.
- Working with shape and typo visuals in constant movement


## Outcomes
Ideal Outcome:
- A simple yet fun mental skill game where speed is key, and it encourages socialization as a multiplayer game.

Minimal Viable Outcome:
- A game capable of developing different outcomes and graphic visuals depending on score counting 


## Milestones
- Week 1
1.	Basic coding, output prints out the game board correctly, and can be open and closed
2.	The program prints the  paddles, ball, point counter starting in 0, and the level the game Is at. 
 
- Week 2
1.	Make the ball able to move left to right, up and down through the board.
2.	Paddles move up and down and can hit the ball, making it go the opposite way.
3.	A point is counted for player 1 or 2 depending on which wall the ball hits.
4.	Add different colors and designs for paddles, balls, and points/level typo.

- Week 3 (Final)
1.	When a player gets to 5 points, the match ends and prints out the result in the center of the game window (3s)
2.	The game follows to a new level. If a players hits 5 points in 2 consecutive levels, the player wins; else, a third level is added, and the first player to get 5 points wins the game.
3.	Adding sound to the game when the ball interacts with the paddle and when a point is added
4.	The game prints the results and gives the option to quit or restart the game.
