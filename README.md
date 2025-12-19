# Chess Engine with Pygame GUI♟️

Interactive chess game built in Python featuring a fully functional AI opponent using minimax search with alpha–beta pruning. Human (White) plays against an AI (Black) with a simple, responsive graphical interface.

---

## ✨Features

- Human vs AI chess with full legal move generation  
- AI using minimax search with alpha–beta pruning (fixed depth)  
- Material-based evaluation function with basic game-end handling  
- Pygame-based 2D board and piece rendering  
- Mouse-based move selection and automatic pawn promotion to queen  
- Centered game-over messages for checkmate and draw

---

## 🛠️Technologies Used

- Python  
- [Pygame](https://www.pygame.org/) (GUI, rendering, input)  
- [python-chess](https://python-chess.readthedocs.io/) (board logic, legal moves)  
- Minimax search  
- Alpha–beta pruning

---

## Project Structure


- `chess_gui.py`: Handles the main game loop, drawing the board and pieces, processing mouse clicks, and calling the AI for moves.  
- `chess_backend.py`: Implements the alpha–beta search and a simple evaluation function based on material.  

---

## 📦 Dependencies

This project requires:

- Python 3.x  
- pygame  
- python-chess  

Install the dependencies using:

- pip install pygame
- pip install python-chess

## 🚀 How to Run

1. **Clone this repository:**
2. **Install dependencies:**
 
3. **Check that the piece images exist:**

- Ensure the `peices/` folder is present in the project root.  
- It should contain files like: `wp.png`, `wn.png`, `wb.png`, `wr.png`, `wq.png`, `wk.png`, `bp.png`, `bn.png`, `bb.png`, `br.png`, `bq.png`, `bk.png`.

4. **Run the game:**
 - python chess_gui.py
---

## How to Play

- You play as **White**, the AI plays as **Black**.
- Click on a white piece to select it, then click on a target square to attempt a move.
- Legal moves and game state are enforced by `python-chess` (illegal moves are ignored).
- Pawns that reach the last rank are automatically promoted to a queen for simplicity.
- When the game ends:
  - Checkmate: A centered message indicates whether White or Black has won.
  - Draw: A centered “Game over: Draw.” message appears.

---

## AI Details

The AI is designed as a classic turn-based game engine:

- **Search algorithm:**  
  Minimax search with alpha–beta pruning over the move tree, exploring a fixed depth each time the AI moves.

- **Evaluation function:**  
  Material-based evaluation that sums piece values (pawn, knight, bishop, rook, queen) and applies large positive/negative scores for checkmate and zero for stalemate/draw-like conditions.

- **Difficulty:**  
  Difficulty is controlled primarily by search depth (e.g., depth 3). Increasing depth makes the AI stronger but slower.

---

## Possible Improvements

Some ideas for future enhancements:

- Add visual highlighting of selected piece and legal moves.
- Add multiple difficulty levels (varying search depth).
- Use more advanced evaluation (piece-square tables, king safety, pawn structure).
- Implement move history, undo functionality, and a restart button.
- Add sound effects, a menu screen, and time controls.

---

## License

This project is intended for learning and personal use. You are welcome to fork the repository and modify the code. If you use this project or significant parts of it in your own work, a brief credit or link back to this repository in your README is appreciated.





