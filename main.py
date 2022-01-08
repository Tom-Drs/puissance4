import os

from game import Puissance4


def main():
    game = Puissance4()
    ended = False
    current_player = 1
    while not ended:
        game.print_grid()
        request_put = input(
            f"Joueur {current_player} : dans quelle colonne voulez"
            f" vous posez un pion ? (premiere colonne -> 0)")
        move = game.put_pawn(request_put, current_player)
        while move == -1:
            game.print_grid()
            print("Erreur, veuillez indiquer une colonne valide")
            request_put = input(
                f"Joueur {current_player} : dans quelle colonne voulez"
                f" vous posez un pion ? (premiere colonne -> 0)")
            move = game.put_pawn(request_put, current_player)
        ended = move
        current_player = switch_player(current_player)
    game.print_grid()
    current_player = switch_player(current_player)
    print(f"Victoire du joueur {current_player}")


def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1


if __name__ == "__main__":
    main()
