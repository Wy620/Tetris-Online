import pygame
import sys
from Board import ROW, COL, SIZE, SCORE_FEILD, Board
from Tetri import Tetrimino, Game_Board
from Tetrimino_list import T, J, L, S, O, I, Z
from P2P import Peer

FPS = 30
GAME_ON = True
pygame.init()

window_width = (COL * SIZE) * 2 + (SCORE_FEILD * SIZE) * 2
window_height = ROW * SIZE
Main_Window = pygame.display.set_mode((window_width, window_height))


my_tetrimino = Tetrimino()
clock = pygame.time.Clock()

Online_Game_Board = Board()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if not GAME_ON:
                    GAME_ON = True
                    Game_Board.Restart()
            if event.key == pygame.K_a and (my_tetrimino.Index_left(my_tetrimino.tetrimino,
                                                                    my_tetrimino.rotation) + my_tetrimino.position) > 0 and not my_tetrimino.Coliide_left(
                    my_tetrimino.tetrimino, my_tetrimino.rotation):
                my_tetrimino.position -= 1
            if event.key == pygame.K_d and (my_tetrimino.Index_right(my_tetrimino.tetrimino,
                                                                     my_tetrimino.rotation) + my_tetrimino.position) < COL - 1 and not my_tetrimino.Coliide_right(
                    my_tetrimino.tetrimino, my_tetrimino.rotation):
                my_tetrimino.position += 1
            if event.key == pygame.K_SPACE:

                # S transform
                if my_tetrimino.tetrimino == S and my_tetrimino.rotation == 1 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == COL - 1:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == S and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == COL - 1:
                    my_tetrimino.rotation = my_tetrimino.rotation
                # Z transform
                elif my_tetrimino.tetrimino == Z and my_tetrimino.rotation == 1 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == COL - 1:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == Z and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == COL - 1:
                    my_tetrimino.rotation = my_tetrimino.rotation
                # LINE transform
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 1 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position >= COL - 2:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 1 and my_tetrimino.Index_left(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position >= COL - 2:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == I and my_tetrimino.rotation == 3 and my_tetrimino.Index_left(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                # J transform
                elif my_tetrimino.tetrimino == J and my_tetrimino.rotation == 0 and my_tetrimino.Index_left(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == J and my_tetrimino.rotation == 2 and my_tetrimino.Index_left(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                # L transform
                elif my_tetrimino.tetrimino == L and my_tetrimino.rotation == 2 and my_tetrimino.Index_left(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == L and my_tetrimino.rotation == 0 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == COL - 1:
                    my_tetrimino.rotation = my_tetrimino.rotation
                # T transform
                elif my_tetrimino.tetrimino == T and my_tetrimino.rotation == 1 and my_tetrimino.Index_left(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == 0:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.tetrimino == T and my_tetrimino.rotation == 3 and my_tetrimino.Index_right(
                        my_tetrimino.tetrimino, my_tetrimino.rotation) + my_tetrimino.position == COL - 1:
                    my_tetrimino.rotation = my_tetrimino.rotation
                elif my_tetrimino.Coliide_rotation(my_tetrimino.tetrimino, my_tetrimino.rotation):
                    my_tetrimino.rotation = my_tetrimino.rotation
                else:
                    my_tetrimino.rotation += 1

                if my_tetrimino.rotation > 3:
                    my_tetrimino.rotation = 0

    if GAME_ON:
        #local
        Main_Window.fill("#ffffff")
        Game_Board.Update(Main_Window)
        my_tetrimino.update(Main_Window, my_tetrimino.tetrimino, 'blue', my_tetrimino.rotation)
        local_state = {"board": Game_Board.board, "score": Game_Board.score, "tetrimino": my_tetrimino.tetrimino}
        #peer.send_data(local_state)

        #online
        #remote_state = peer.receive_data()
        #Online_Game_Board.board = remote_state.get("board")
        #Online_Game_Board.score = remote_state.get("score")

        pygame.display.update()
        if Game_Board.Game_Over() or Online_Game_Board.Game_Over():
            GAME_ON = False