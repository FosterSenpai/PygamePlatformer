# Foster Rae
# 02/09/2024
# Entry point

from classes.screen_manager import ScreenManager
from classes.game_manager import GameManager

game_manager = GameManager()
screen_manager = ScreenManager(game_manager)
screen_manager.run()

    