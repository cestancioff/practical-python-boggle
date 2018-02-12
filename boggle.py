def make_grid(width, height):
    """
   create a grid that will hpld all the tiles for a boggle game
    """

    return{(row, col): ' ' for row in range (height)
        for col in range (width)
    }
        