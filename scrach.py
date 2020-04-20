import tictactoe as t

for _idx in range(5):
    b = t.gen_rand_board()
    action = t.minimax(b)
    print("\nPlayer: ", t.player(b))
    print("\nAccion: ", action, "\n")
    if not action is None:
        move = t.result(b, action)

    t.pp(b)
    print("\n==>\n ")
    t.pp(move)

    print("+++++++++++++++")
