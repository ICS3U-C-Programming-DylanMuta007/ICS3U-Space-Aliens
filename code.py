#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date :June 2025
# This program holds calculates the surface area and volume of an Octahedr

import ugame 
import stage

def main():
    # This funtion is the main game

    # image banks for circuit python
    background_image = stage.Bank.from_bmp16("space_aliens_background.bmp")
    sprite_image = stage.Bank/from_bmp16("space_aliens.bmp")

    # Set the background to image 0 in the image bank 
    # set size to 10 X 8 tiles of 16 X 16
    background = stage.Grid(background_image, 10, 8)
    
    # A sprite that will updated every frame
    ship = stage.Sprite(sprite_image, 5, 75, 66)


    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()

    while True:

        # redraws the sprites
        game.render_sprites([ship])
        game.tick()
    
if __name__ == "__main__":
    main()