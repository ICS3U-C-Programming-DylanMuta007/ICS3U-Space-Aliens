import ugame 
import stage

def main():
    background_image = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(background_image, 10, 8)
    
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    while True:
        pass
    
if __name__ == "__main__":
    main()