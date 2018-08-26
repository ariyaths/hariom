
# coding: utf-8

# In[6]:


class TicTacToe:
  SIZE = 3
  PLAYERS = 2
  EMPTY = ' '
  horizontal_lines = '___|___|___'
  vertical_lines = '   |   | '
  bar = ' | '

  def __init__(self, size=SIZE):
    self._grid = [[TicTacToe.EMPTY for col in range(size)]
                  for row in range(size)]
    self._current_player = 0
    self._moves = 0

  @property
  def is_over(self):
    """Returns True if the game is over"""
    return self._moves == TicTacToe.SIZE * TicTacToe.SIZE or self.check_winner(
    ) is not None

  @property
  def current_player(self):
    """Returns the current player number"""
    return self._current_player

  def check_winner(self):
    """Returns the player number if there is a winner, otherwise returns None"""
    # check rows
    for row in self._grid:
      if len(set(row)) == 1 and row[0] != TicTacToe.EMPTY:
        return self._marker_to_player(row[0])

    # check columns
    for col_index in range(TicTacToe.SIZE):
      col = [
          self._grid[row_index][col_index]
          for row_index in range(TicTacToe.SIZE)
      ]
      if len(set(col)) == 1 and col[0] != TicTacToe.EMPTY:
        return self._marker_to_player(col[0])

    # check diagonals
    pos_diagonal = [
        self._grid[~index][index] for index in range(TicTacToe.SIZE)
    ]
    if len(set(pos_diagonal)) == 1 and pos_diagonal[0] != TicTacToe.EMPTY:
      return self._marker_to_player(self._grid[-TicTacToe.SIZE][0])

    neg_diagonal = [
        self._grid[index][index] for index in range(TicTacToe.SIZE)
    ]
    if len(set(neg_diagonal)) == 1 and neg_diagonal[0] != TicTacToe.EMPTY:
      return self._marker_to_player(self._grid[0][0])

    # return None if no winner

  def process_turn(self, position):
    """Processes turn and returns whether processing was successful"""
    row, col = position

    # check bounds
    if not (0 <= row < TicTacToe.SIZE and 0 <= col < TicTacToe.SIZE):
      return False

    # check if valid placement
    if self._grid[row][col] != TicTacToe.EMPTY:
      return False

    self._grid[row][col] = self._player_to_marker(self._current_player)

    self._current_player = (self._current_player + 1) % TicTacToe.PLAYERS
    self._moves += 1
    return True

  def _player_to_marker(self, player_number):
    """Converts player number into the string representation of the player"""
    if player_number == 0:
      return 'X'
    else:
      return 'O'

  def _marker_to_player(self, marker_string):
    """Converts marker string into the player number"""
    if marker_string == 'X':
      return 0
    else:
      return 1

  def __str__(self):
    lines = []

    # automate drawing
    for i, row in enumerate(self._grid):
      lines.append(TicTacToe.EMPTY + (TicTacToe.bar).join(row))
      if i < TicTacToe.SIZE - 1:
        lines.append(TicTacToe.horizontal_lines)
    lines.append(TicTacToe.vertical_lines)

    return '\n'.join(lines)


from time import sleep
SLEEP_TIME = 3

if __name__ == '__main__':
  game = TicTacToe()
  print( 'Player 1 will be "X"\nPlayer 2 will be "O"\nBe Ready! ;)')
  sleep(SLEEP_TIME)

  while not game.is_over:
    print( str(game))

    # continue until position is properly parsed
    correct_format = False
    while not correct_format:
      position = input(
          'Player {}: Please provide the desired row and column (space '
          'separated)\n'.format(game.current_player + 1))
      try:
        correct_format = game.process_turn(tuple(map(int, position.split())))
      except:
        correct_format = False
      if not correct_format:
        print( "Invalid query: '{}'".format(position))

  print( str(game))

  # display winner
  winner = game.check_winner()
  if winner is None:
    print( 'Wow! It is a Draw! ! ! :|')
  else:
    print( 'Yipee! Player {} Has Won! ! ! :)'.format(winner + 1))

