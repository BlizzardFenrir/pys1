class Color:
    colormap = { 'black':   0, \
                 'red':     1, \
                 'green':   2, \
                 'yellow':  3, \
                 'blue':    4, \
                 'magenta': 5, \
                 'cyan':    6, \
                 'white':   7, \
                 'default': 9 }

    def __init__(self):
        self.flags = []

    def addForegroundColor(self, color):
        self.flags.append( str(30 + self.colormap[color]) )

    def addBackgroundColor(self, color):
        self.flags.append( str(40 + self.colormap[color]) )

    def resetFlags(self):
        self.flags.append( '0' ) # Unset all previous flags

    def setBold(self):
        self.flags.append( '1' ) # Bright intensity

    def unsetBold(self):
        self.flags.append( '22' ) # Regular intensity

    def __str__(self):
        if not self.flags:
            return '' # no flags have been set
        return '\033[' + ';'.join(self.flags) + 'm'

class Text:
    def __init__(self, text=None):
        if text is None:
            text = ''
        self.text = text;

    def append(self, text):
        self.text += text

    def __str__(self):
        return self.text;

class Prompt:
    def __init__(self):
        self.components = []

    def addText(self, text):
        if len(self.components) == 0 or type(self.components[-1]) is not Text:
            self.components.append( Text() )
        textnode = self.components[-1]

        textnode.append(text)

    def setColor(self, foreground=None, background=None, bold=None, reset=None):
        if len(self.components) == 0 or type(self.components[-1]) is not Color:
            self.components.append( Color() )
        colornode = self.components[-1]

        # set parameters
        if foreground != None:
            colornode.addForegroundColor(foreground)
        if background != None:
            colornode.addBackgroundColor(background)
        if bold != None:
            if bold == True:
                colornode.setBold()
            else:
                colornode.unsetBold()
        if reset == True:
            colornode.resetFlags()

    def setForegroundColor(self, color):
        self.setColor(foreground=color)

    def setBackgroundColor(self, color):
        self.setColor(background=color)

    def setBold(self):
        self.setColor(bold=True)

    def unsetBold(self):
        self.setColor(bold=False)

    def resetFlags(self):
        self.setColor(reset=True)

    def __str__(self):
        return ''.join( [str(x) for x in self.components] )

def main():
    p = Prompt()

    # First section
    p.setForegroundColor('black')
    p.setBackgroundColor('red')
    p.addText(' user:computer ')

    # Powerline splitter
    p.setForegroundColor('red')
    p.setBackgroundColor('cyan')
    p.addText( b'\xee\x82\xb0'.decode('utf-8') )

    # Second section
    p.setForegroundColor('black')
    p.addText(' ~/Cool/Projects ')

    # Powerline splitter
    p.resetFlags()
    p.setForegroundColor('cyan')
    p.addText( b'\xee\x82\xb0'.decode('utf-8') )

    # Second line
    p.resetFlags()
    p.addText( '\n' )

    # Triple dot prompt
    p.setForegroundColor('red')
    p.addText( b'\xe2\x80\xa2'.decode('utf-8') )
    p.setForegroundColor('magenta')
    p.addText( b'\xe2\x80\xa2'.decode('utf-8') )
    p.setForegroundColor('cyan')
    p.addText( b'\xe2\x80\xa2'.decode('utf-8') )

    # Final space and reset for terminal
    p.addText( ' ' )
    p.resetFlags()

    print(p)

if __name__ == '__main__':
    main()

