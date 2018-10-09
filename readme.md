# PyFrotz

minimal python wrapper around [Frotz](https://gitlab.com/DavidGriffith/frotz)

get some classic games to try it out [here](https://if.illuminion.de/infocom.html)


# install

first you need to install frotz, i included a script for that

    bash requirements.sh
    
or you can install it yourself

    git clone https://gitlab.com/DavidGriffith/frotz
    cd frotz
    make dumb
    cd ..
    
then install the python package from pip

    pip install pyfrotz
 

# usage

    from pyfrotz import Frotz
    
    # load your game file
    data = '/home/user/PycharmProjects/infocom-games-skill/planetfall.z5'
    game = Frotz(data)  # optionally pass frotz path, default='./frotz/dfrotz'
    
    
    # use it inside code
    game_intro = game.get_intro()
    room, description = game.do_command("look")
    game.save()  # optionally pass filename, default='save.qzl'
    game.restore()  # optionally pass filename, default='save.qzl'
    
    
    # or play in the cli
    game = Frotz(data)
    game.play_loop()

