#!/usr/bin/env python
## @package swordfight

# imports
import pyray as pr
import entity_manager.entity_manager as em
import entity_manager.shapes as shapes
from players import Player
from weapons import Sword
from obstacles import Obstacle
from globals import *

# constants
STAGE_REC = shapes.Rectangle(100,300,600,50)
P1BINDINGS = {
    'up': pr.KEY_W,
    'down': pr.KEY_S,
    'left':pr.KEY_A,
    'right':pr.KEY_D }
P2BINDINGS = {
    'up': pr.KEY_UP,
    'down': pr.KEY_DOWN,
    'left':pr.KEY_LEFT,
    'right':pr.KEY_RIGHT }



# initialization
player1 = Player(shapes.Point(200,200), pr.RED, P1BINDINGS, RIGHT)
player2 = Player(shapes.Point(500,200), pr.BLUE, P2BINDINGS, LEFT)
sword1 = Sword(shapes.Point(200,200), LEFT)
player1.weapon = sword1
stage = Obstacle(pr.DARKGRAY, STAGE_REC)

players = [player1, player2]
swords = [sword1]
obstacles = [stage]

manager = em.Entity_manager()
manager.add_entity( player1.entity, 'player1')
manager.add_entity( player2.entity, 'player2')
manager.add_entity( stage.entity, 'stage')

# loop
pr.set_target_fps(60)
pr.init_window(800,450, 'swordfight')
while not pr.window_should_close():
    #update
    go = True # toggle for frame-by-frame
    if go:
        for player in players:
            player.update(manager.check_collisions)
        for sword in swords:
            sword.update()
    if pr.is_key_pressed(pr.KEY_SPACE):
        go = True
    #draw
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    for obstacle in obstacles:
        obstacle.draw()
    for player in players:
        player.draw()
    for sword in swords:
        sword.draw()
    pr.draw_text(str(len(manager.overlaps)), 20,0,20, pr.BLACK)
    for i in range(len(players)):
        pr.draw_text(f"{i}:{players[i].position.x},{players[i].position.y}", 20,20*i + 20, 20,pr.BLACK)
    pr.end_drawing()
pr.close_window()

