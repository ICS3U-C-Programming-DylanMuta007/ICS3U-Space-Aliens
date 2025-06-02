import ugame 
import stage

def main():
    background_image = stage.Bank.from_bmp16("space_aliens_background.bmp")
    sprite_image = stage.Bank/from_bmp16("space_aliens.bmp")

    background = stage.Grid(background_image, 10, 8)
    
    ship = stage.Sprite(sprite_image, 5, 75, 66)

    game = stage.Stage(ugame.display, 60)
    game.layers = [ship] + [background]
    game.render_block()

    while True:
        game.render_sprites([ship])
        game.tick
    
if __name__ == "__main__":
    main()