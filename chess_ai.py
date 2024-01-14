try:
    import chess
    import random
    
    def evaluate_board(board):
        # Simple evaluation function based on piece values
        piece_values = {
            chess.PAWN: 1,
            chess.KNIGHT: 3,
            chess.BISHOP: 3,
            chess.ROOK: 5,
            chess.QUEEN: 9,
            chess.KING: 100
        }
    
        evaluation = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece is not None:
                value = piece_values.get(piece.piece_type, 0)
                evaluation += value if piece.color == chess.WHITE else -value
    
        return evaluation
    
    def minimax(board, depth, maximizing_player):
        if depth == 0 or board.is_game_over():
            return evaluate_board(board)
    
        legal_moves = list(board.legal_moves)
    
        if maximizing_player:
            max_eval = float('-inf')
            for move in legal_moves:
                board.push(move)
                eval = minimax(board, depth - 1, False)
                max_eval = max(max_eval, eval)
                board.pop()
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                board.push(move)
                eval = minimax(board, depth - 1, True)
                min_eval = min(min_eval, eval)
                board.pop()
            return min_eval
    
    def get_best_move(board, depth):
        legal_moves = list(board.legal_moves)
        best_move = None
        best_eval = float('-inf')
    
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)
            board.pop()
    
            if eval > best_eval:
                best_eval = eval
                best_move = move
    
        return best_move
    
    def play_game():
        board = chess.Board()
    
        while not board.is_game_over():
            if board.turn == chess.WHITE:
                move = get_best_move(board, depth=2)
            else:
                # Random move for black (opponent)
                move = random.choice(list(board.legal_moves))
    
            board.push(move)
            print(board)
    
        print("Game Over")
        print("Result:", board.result())
    
    if __name__ == "__main__":
        play_game()

except Exception as e:
    print(e)
    input("")
