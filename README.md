# Tic_Tac_Toe

A tic-tac-toe game done in Python. This project started as a simple command line game created for Angela Yu's 100 Days of Code course of Udemy, but after completing that quickly I wanted to expand it a bit to get more practice.

The project uses Pygame for graphics. There is a two player mode and a single player mode that has 'easy' and 'hard' modes. The easy mode is a simple random move generator and the hard mode uses a mini-max algorithm to play perfect moves. There is a small flaw in the 'hard' mode that results in the computer playing suboptimal moves if the player plays poorly, but in that case the computer should still win. 

Ths program also has a testing script that I used to run 500 games to confirm that the mini-max algorithm was working properly. Test modes 0 and 1 had X and O use the mini-max algorithm with slight randomization, which should result in a draw for each game. This held true after 198 games between the modes, whcih gives me confidence that the alogorithm is working. Unfortunately, my computer apparently didn't like runnning the script very much and the program would crash frequently. I originally intended to run thousands of tests but the constant crashing made that impracticable.

There are definitely many things that I could improve upon with this project to better follow programming best practices, and I am going to be more mindful on my next project
