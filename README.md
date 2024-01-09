# Space Shooter Combat Game in Python

This is a space shooter combat game developed using Python and Pygame library. The game involves a spaceship battling against enemy spaceships. The objective of the game is to eliminate as many enemy spaceships as possible while preventing them from reaching the bottom of the screen.

## Prerequisites

To run this game, you will need:

- Python 3 or later
- Pygame library

## Installation

To install Pygame, run the following command in your terminal:


pip install pygame


## Game Overview

The game consists of the following key components:

- *Spaceship:* Controlled by the player, the spaceship can move left and right and shoot bullets.
- *Enemy Spaceships:* Multiple enemy spaceships appear on the screen and move towards the bottom.
- *Bullets:* The spaceship can shoot bullets to destroy enemy spaceships.
- *Score:* The player earns points for each enemy spaceship destroyed.

## Code Explanation

### Importing Libraries

python
import pygame
import random
import math
from pygame import mixer


These lines import the necessary libraries for the game. Pygame is used for game development, random for generating random numbers, math for mathematical calculations, and mixer for playing sounds.

### Initializing Pygame

python
mixer.init()
pygame.init()


These lines initialize Pygame and the mixer module for playing sounds.

### Setting Up the Game Window

python
screenWidth, screenHeight = 800, 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Space Shooter Combat")


These lines set up the game window with a resolution of 800x600 pixels and set the window title to "Space Shooter Combat".

### Loading Images

```python
icon = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\SpaceShooterCombatIcon.webp")
pygame.display.set_icon(icon)

backGround = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\SpaceShooterBg.jpg")
backGround = pygame.transform.scale(backGround, (screenWidth, screenHeight))

spaceShipImage = pygame.image.load("D:\\Python Projects\\Projects\\Space Shooter Combat\\Images\\spaceShip.png")
spaceShipImage
