#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :June 2025
# Space aliens in a pybadge

import ugame 
import stage
import constant

def game_scene():
    # This funtion is the main game

    # image banks for circuit python
    background_image = stage.Bank.from_bmp16("space_aliens_background.bmp")
    sprite_image = stage.Bank.from_bmp16("space_aliens.bmp")

    # Set the background to image 0 in the image bank 
    # set size to 10 X 8 tiles of 16 X 16
    background = stage.Grid(background_image, constant.SCREEN_GRID_X, constant.SCREEN_GRID_Y)
    
    # A sprite that will updated every frame
    ship = stage.Sprite(sprite_image, 5, 75, constant.SCREEN_Y - (2* constant.SPRITE_SIZE))


    game = stage.Stage(ugame.display, constant.FPS)
    game.layers = [ship] + [background]
    game.render_block()

    while True:
        # redraws the sprites
        game.render_sprites([ship])
        game.tick()
        
        # user input
        keys = ugame.buttons.get_pressed()
        
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constant.SCREEN_X - constant.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(constant.SCREEN_X - constant.SPRITE_SIZE, ship.y)

        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(0, ship.y)


        if keys & ugame.K_UP:
            pass
        if keys & ugame.K_DOWN:
            pass
    
if __name__ == "__main__":
    game_scene()