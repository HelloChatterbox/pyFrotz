from pyfrotz import Frotz

# load your game file
data = '/home/user/PycharmProjects/infocom-games-skill/planetfall.z5'
game = Frotz(data)


# use it inside code
game_intro = game.get_intro()
room, description = game.do_command("look")
game.save()  # optionally pass filename, default='save.qzl'
game.restore()  # optionally pass filename, default='save.qzl'


# or play in the cli
game = Frotz(data)
game.play_loop()

