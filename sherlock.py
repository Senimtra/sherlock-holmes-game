
### Create class Game ###
class Game:
   def __init__(self, game_state, location):
      self.game_state = game_state
      self.location = location
   def __str__(self):
      return self.game_state

### Player commands ###
commands = {
   'explore': "I'm exploring the room."
}

### Game locations ###
locations = {
   'home_living_room': {
      'description': "This is Sherlock Holmes' living room.",
      'ways': ['bedroom', 'kitchen', 'bathroom', 'staircase'],
      'items': ['desk', 'chair', 'sofa', 'violine']
   },
   'home_bedroom': {
      'description': "This is Sherlock Holmes' bedroom.",
      'ways': ['living room', 'bathroom'],
      'items': ['bed', 'wardrobe', 'chest', 'safe']     
   },
   'home_bathroom': {
      'description': "This is Sherlock Holmes' bathroom.",
      'ways': ['bedroom'],
      'items': ['toilet', 'bathtub', 'medicine cabinet']     
   },
   'home_kitchen': {
      'description': "This is Sherlock Holmes' kitchen.",
      'ways': ['living room'],
      'items': ['kitchen table', 'stove', 'cupboard', 'food rack']      
   }
}

### Game items ###
items = {
   'violine': {
      'description': 'Your violine.'
   }
}

### Create game object from class Game ###
game = Game('running', 'home_living_room')

### Start game ###
def game_start():
   print('You are at 221b Baker Street, London, 1888.')
   play_location()

### Play location ###
def play_location():
   location = locations[game.location]
   print(location['description'])
   print(f"You recognize: {', '.join(location['items'])}.")
   print(f"You could go to: {', '.join(location['ways'])}.")
   parser = input('What do you want to do? ')
   if parser in commands.keys():
      print(commands[parser])
      play_location()
   else:
      print("I do not know what to do.")
      play_location()

game_start()