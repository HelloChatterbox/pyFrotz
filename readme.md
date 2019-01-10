# PyFrotz
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

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

