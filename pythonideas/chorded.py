""" Sketch code for a chording keyboard prototype: part 2 """
 
from __future__ import print_function
from tkinter import *
import sys
 
root = Tk()
debug = False
 
# shortcuts:
#'aa'=>0, 'bb'->1 etc?
# char space space -> char . space Cap
 
#rules: don't care about down-order, do care about 1st keyup
 
from chordfile import CHARMAPS, KEYMAP
     
class Chords(object):
    def __init__(self, keymap, charmaps):
        self.keymap = keymap
        self.charmaps = charmaps
        self.chars = ''
        self.down = []
        self.enabled = False
        self.mode = '/LOWER'
     
    def keypress(self, event):
        down = event.char
        if down not in self.keymap:
            return
        if down not in self.down:
            self.down.append(down)
            self.enabled = True
            if debug:
                print("pressed", down, self.down)
 
    def keyrelease(self, event):
        up = event.char
        if up not in self.keymap:
            return
        if debug:
            print("release", up, self.down)
        if self.enabled:
            code = self.keys_to_code(self.down, up)
            char = self.charmaps[self.mode].get(code, None)
            if char is None: # try a lowercase conversion
                if self.mode.startswith('/SHIFT'):
                    char = self.charmaps['/LOWER'].get(code, None).upper()
            if char is None: # it doesn't exist - debug print
                print('\n', self.mode, ':', code, '\n')
            else:
                if char.startswith('/'): # change mode
                    self.mode = char
                else:
                    print(char,end='')
                    if self.mode == '/SHIFT': # return to lowercase on next
                        self.mode = '/LOWER'
                         
            self.enabled = False
        self.down.remove(up)
         
    def keys_to_code(self, downkeys, upkey):
        #print(downkeys, upkey)
        downkeys = [KEYMAP[k] for k in downkeys]
        upkey = KEYMAP[upkey]
        sortdown = sorted(downkeys)
        code = ''
        #print('sorted:', sortdown)
        for k in sortdown:
            if k == upkey:
                code += '(%s)' % k
            else:
                code += k
        return code
if __name__ == '__main__':
    c = Chords(KEYMAP, CHARMAPS)
    if len(sys.argv) > 1:
        if sys.argv[1] == 'd': # debug mode
            debug = True
        elif sys.argv[1] == 't': # training mode
            lower = dict((v, k) for k, v in CHARMAPS['/LOWER'].items())
            loweralpha = sorted(lower.keys())[14:]
            for ch in loweralpha[:6]:
                print(ch, lower[ch])
 
    frame = Frame(root, width=100, height=100)
    frame.bind("<KeyPress>", c.keypress)
    frame.bind("<KeyRelease>", c.keyrelease)
    frame.pack()
    frame.focus_set()
    root.mainloop()
