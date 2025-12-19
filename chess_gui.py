import pygame
import chess
from chess_backend import get_best_move

pygame.init()

WIDTH, HEIGHT = 500, 500
SQ_SIZE = WIDTH // 8
FPS = 15

symbol_to_file = {
    'P': "wp.png",
    'N': "wn.png",
    'B': "wb.png",
    'R': "wr.png",
    'Q': "wq.png",
    'K': "wk.png",
    'p': "bp.png",
    'n': "bn.png",
    'b': "bb.png",
    'r': "br.png",
    'q': "bq.png",
    'k': "bk.png",
}

IMAGES = {}
for symbol, filename in symbol_to_file.items():
    IMAGES[symbol] = pygame.transform.scale(
        pygame.image.load(f"peices/{filename}"), (SQ_SIZE, SQ_SIZE)
    )

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

font = pygame.font.SysFont(None, 32)

def draw_board(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            pygame.draw.rect(
                screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE)
            )

def draw_pieces(screen, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            row = 7 - chess.square_rank(square)
            col = chess.square_file(square)
            screen.blit(
                IMAGES[piece.symbol()],
                pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE),
            )

def get_square_under_mouse(pos):
    x, y = pos
    col = x // SQ_SIZE
    row = y // SQ_SIZE
    return chess.square(col, 7 - row)

def draw_status(screen, text):
    if text:
        label = font.render(text, True, pygame.Color("black"))
        label_rect = label.get_rect(center=screen.get_rect().center)
        screen.blit(label, label_rect)


def main():
    clock = pygame.time.Clock()
    board = chess.Board()
    player_turn = True  # Human white, AI black
    selected_square = None
    status_text = ""
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and player_turn and not board.is_game_over():
                sq = get_square_under_mouse(pygame.mouse.get_pos())
                if selected_square is None:
                    if board.piece_at(sq) and board.turn == chess.WHITE:
                        selected_square = sq
                else:
                    # Handle promotion explicitly
                    move = chess.Move(selected_square, sq)
                    piece = board.piece_at(selected_square)
                    if (
                        piece and piece.piece_type == chess.PAWN and
                        (chess.square_rank(sq) == 0 or chess.square_rank(sq) == 7)
                    ):
                        # Always promote to Queen for simplicity
                        move = chess.Move(selected_square, sq, promotion=chess.QUEEN)

                    if move in board.legal_moves:
                        board.push(move)
                        player_turn = False
                        selected_square = None
                    else:
                        # Invalid move; deselect
                        selected_square = None

        # AI move + game-over checks
        if not player_turn and not board.is_game_over():
            move = get_best_move(board, 3)
            if move:
                board.push(move)
            player_turn = True

        if board.is_game_over():
            result = board.result()  # "1-0", "0-1", "1/2-1/2"
            if board.is_checkmate():
                if result == "1-0":
                    status_text = "Checkmate! White wins."
                elif result == "0-1":
                    status_text = "Checkmate! Black wins."
            else:
                status_text = "Game over: Draw."

        draw_board(screen)
        draw_pieces(screen, board)
        draw_status(screen, status_text)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
