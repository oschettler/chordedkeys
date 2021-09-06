"""
Define mappings for key sequences (chords) to characters
Character frequency info (including non-alpha chars) from http://mtgap.bilfo.com/letter_frequency.html
"""
 
SHIFT = {
    '(0)12':'/SHIFTLOCK',
}
 
SHIFTLOCK = {
    '(0)12':'/LOWER',
}
 
NUMCHAR = {
    '(0)':'1', # onekey chords x 5
    '(1)':'2',
    '(2)':'3',
    '(3)':'4',
    '(4)':'5',
    '0(1)':'6', # twokey x 20
    '0(2)':'7',
    '0(3)':'8',
    '0(4)':'9',
    '(0)23':'/LOWER'
    }
     
LOWER = {
    '(0)':' ', # onekey chords x 5
    '(1)':'e',
    '(2)':'t',
    '(3)':'a',
    '(4)':'o',
    '0(1)':'i', # twokey x 20
    '0(2)':'n',
    '0(3)':'s',
    '0(4)':'r',
    '(0)1':'h',
    '1(2)':'l',
    '1(3)':'d',
    '1(4)':'c',
    '(0)2':'u',
    '(1)2':'m',
    '2(3)':'f',
    '2(4)':'g',
    '(0)3':'p',
    '(1)3':'y',
    '(2)3':'w',
    '3(4)':'\n', # RETURN
    '(0)4':'b',
    '(1)4':',',
    '(2)4':'.',
    '(3)4':'v',
    '01(2)':'k', # 3 key x 12 (straightforward)
    '01(3)':'-',
    '01(4)':"'",
    '0(1)2':'x',
    '02(3)':'j',
    '02(4)':'q',
    '0(1)3':':',
    '0(2)3':'z',
    '03(4)':'!',
    '0(1)4':'?',
    '0(2)4':'<GBP>',
    '0(3)4':'&',
    '(0)34':'\b', # 3 key (harder)
    #'(1)23':'/SHIFT', # doesn't work due to keyboard limits?
    '(0)12':'/SHIFT',
    '(0)23':'/NUMCHAR'
    }
 
     
CHARMAPS = {'/LOWER':LOWER, '/SHIFT':SHIFT, '/SHIFTLOCK':SHIFTLOCK, '/NUMCHAR':NUMCHAR}
KEYMAP = {' ':'0', 'r':'1', 'e':'2', 'w':'3', 'a':'4'}
