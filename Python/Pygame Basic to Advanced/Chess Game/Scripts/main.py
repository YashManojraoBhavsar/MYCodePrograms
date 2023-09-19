""" Main User Interface Script for Chess Game in Python """
import sys
import pygame

import chess_backend as chess
import game_constants as const


class GameUI:
    """Main Handler Class for Chess Game."""

    @classmethod
    def welcome_screen(cls):
        """
        The function displays a welcome screen in a Pygame window and waits for the user to
        press the Enter key to start the game  or close to end it.

        :param cls: The parameter "cls" in the function "welcome_screen" is typically used as a
        convention to refer to the class itself.
        """
        while True:
            pygame.display.update()
            const.clock.tick(const.FPS_VALUE)
            const.game_Window.fill(const.blue)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        cls.game_loop()

    @classmethod
    def end_screen(cls):
        """
        The function `end_screen` displays a blue screen and waits for the user to press the Enter
        key to start the game loop or close to end it.

        :param cls: The parameter "cls" in the function "end_screen" is typically used as a
        convention to refer to the class itself.
        """
        while True:
            pygame.display.update()
            const.clock.tick(const.FPS_VALUE)
            const.game_Window.fill(const.blue)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        cls.game_loop()

    @classmethod
    def game_loop(cls):
        """
        The function `game_loop` is a loop that handles the main game logic and events, including
        updating the display, handling mouse and keyboard events, and checking for game over
        conditions.

        :param cls: The parameter "cls" is a reference to the class that the method belongs to.
        It is used to access the class's attributes and methods within the method
        """

        game_over = False
        selected_pos = (-1, -1)
        chess_board = chess.ChessGame()

        while not game_over:
            const.clock.tick(const.FPS_VALUE)
            pygame.display.flip()
            selected_pos, game_over = chess_board.play(selected_pos)
            # pygame.display.update()  # Updating Display.

                # box_pos = (-1, -1)


            # game_board.draw_dot((5, 5))

            for event in pygame.event.get():  # Getting The Event In Pygame.
                if (
                    event.type == pygame.QUIT
                ):  # Checking If The Close Button Is Pressed.
                    pygame.quit()  # Quitting The Game...
                    sys.exit()  # Exiting All Functions...

                # Checking If Any Mouse Button Is Pressed.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Checking If The Left Mouse Button Is Pressed.
                    if event.button == pygame.BUTTON_LEFT:
                        selected_pos = (-1, -1)
                        # game_board.show_board()
                        selected_pos = pygame.mouse.get_pos()
                if event.type == pygame.KEYDOWN:  # Checking If Any Key Is Pressed.
                    # Checking If Enter(Return) Key Is Pressed.
                    if event.key == pygame.K_RETURN:
                        pass

        if game_over:  # Checking If The Game Is Over.
            cls.end_screen()  # Calling Ending Screen...


if __name__ == "__main__":
    GameUI.game_loop()  # Calling Welcome Screen...