
### Create class Game ###
class Game:
   def __init__(self, game_state, commands, location):
      self.game_state = game_state
      self.commands = commands
      self.location = location

   def __str__(self):
      return self.game_state

### Player commands ###
commands = {
   'explore': "I'm exploring the room.",
}

### Create game object from class Game ###
game = Game('running', commands, 'home')

### Start game ###
def game_start():
   print(f'Game is {game}.')
   play_location()

### Play location ###
def play_location():
   print(f'You are at: {game.location}')
   parser = input('What do you want to do?')
   if parser in game.commands.keys():
      print(game.commands[parser])
      play_location()
   else:
      print("I do not know what to do.")
      play_location()

game_start()