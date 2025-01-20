## @package swordfight

import pyray as pr
import entity_manager.entity_manager as em

myManager = em.Entity_manager

pr.set_target_fps(60)
pr.init_window(800,450, 'swordfight')
while not pr.window_should_close():
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.end_drawing()
pr.close_window()

