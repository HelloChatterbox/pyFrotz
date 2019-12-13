from pyfrotz import Frotz

# load your game file
data = '/home/user/infocom_games/planetfall.z5'
game = Frotz(data)


# use it inside code
#game_intro = game.get_intro()
#room, description = game.do_command("look")


# or play in the cli
game = Frotz(data)
game.play_loop()

