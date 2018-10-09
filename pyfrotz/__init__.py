import time
import subprocess
from os.path import exists, dirname, join


class Frotz(object):
    def __init__(self, game_data,
                 interpreter=join(dirname(dirname(__file__)), 'frotz/dfrotz'),
                 save_file='save.qzl',
                 prompt_symbol=">",
                 reformat_spacing=True):
        self.data = game_data
        self.interpreter = interpreter
        self.save_file = save_file
        self.prompt_symbol = prompt_symbol
        self.reformat_spacing = reformat_spacing
        self._get_frotz()

    def _get_frotz(self):

        self.frotz = subprocess.Popen([self.interpreter, self.data],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        time.sleep(0.1)  # Allow to load

        # Load default savegame
        if exists(self.save_file):
            print('Loading saved game')
            self.restore(self.save_file)

    def save(self, filename=None):
        """
            Save game state.
        """
        filename = filename or self.save_file
        self.do_command('save')
        time.sleep(0.5)
        self._clear_until_prompt(':')
        self.do_command(filename)  # Accept default savegame
        time.sleep(0.5)
        # Check if game returns Ok or query to overwrite
        while True:
            char = self.frotz.stdout.read(1)
            time.sleep(0.01)
            if char == b'.':  # Ok. (everything is done)
                break  # The save is complete
            if char == b'?':  # Indicates an overwrite query
                self.do_command('y')  # reply yes

        time.sleep(0.5)
        self._clear_until_prompt()

    def restore(self, filename=None):
        """
            Restore saved game.
        """
        filename = filename or self.save_file
        self.do_command('restore')
        time.sleep(0.5)
        self._clear_until_prompt(':')
        self.do_command(filename)  # Accept default savegame
        time.sleep(0.5)
        self._clear_until_prompt()

    def _clear_until_prompt(self, prompt=None):
        """ Clear all received characters until the standard prompt. """
        # Clear all data with title etcetera
        prompt = prompt or self.prompt_symbol
        char = self.frotz.stdout.read(1).decode()
        while char != prompt:
            time.sleep(0.001)
            char = self.frotz.stdout.read(1).decode()

    def do_command(self, action):
        """ Write a command to the interpreter. """
        self.frotz.stdin.write(action.encode() + b'\n')
        self.frotz.stdin.flush()
        return self._frotz_read()

    def _frotz_read(self, parse_room=True):
        """
            Read from frotz interpreter process.
            Returns tuple with Room name and description.
        """
        # Read room info
        output = ""
        output += self.frotz.stdout.read(1).decode()
        if not len(output):
            return ""
        while output[-1] != '>':
            output += self.frotz.stdout.read(1).decode()
        lines = [l for l in output[:-1].split("\n") if l.strip() and "Score: " not in l]
        if parse_room:
            room = lines[0]
            lines = lines[1:]
        # reformat text by . instead of \n
        if self.reformat_spacing:
            lines = " ".join(lines).replace(".", ".\n")
        else:
            lines = "\n".join(lines)
        # Return description removing the prompt
        if parse_room:
            return room, lines
        return lines

    def get_intro(self, custom_parser=None):

        if custom_parser is not None:
            intro = custom_parser(self)
        else:
            output = ""
            saw_serial = False
            while not saw_serial:
                output += self.frotz.stdout.read(1).decode()
                while str(output)[-1] != '\n':
                    output += self.frotz.stdout.read(1).decode()
                if "serial number" in output.lower():
                    saw_serial = True

            intro = self._frotz_read(parse_room=False) + "\n"
        # lets remove the first "look"
        room, descript = self.do_command("look")
        return intro.replace(descript, "").replace(room, "").strip()

    def play_loop(self):
        print(self.get_intro())
        try:
            while not self.game_ended():
                room, descript = self.do_command(input(">>"))
                print(room)
                print(descript)
        except KeyboardInterrupt:
            pass

    def game_ended(self):
        poll = self.frotz.poll()
        if poll is None:
            return False
        else:
            return True
