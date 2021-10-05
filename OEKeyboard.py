import tkinter as tk
import tkinter.font as font
from pandas.io.clipboard import copy

class OE_Keyboard:
    def __init__(self, master):
        tk.Label(master, text = "Old English Special Characters").grid(row = 0, columnspan = 6)    
        tk.Label(master, text = "Consonants").grid(row = 1, columnspan = 6) 
        def press(key):
            copy(key)
        myfont = font.Font(size = 20)
            
    
    
        U_thorn = tk.Button(master, text = u'\u00DE',width = 3,height = 1, command = lambda: press(u'\u00DE'))
        U_thorn.grid(row = 2, column = 0)
        U_thorn['font'] = myfont
        
        L_thorn = tk.Button(master, text = u'\u00FE',width = 3,height = 1, command = lambda: press(u'\u00FE'))
        L_thorn.grid(row = 2, column = 1)
        L_thorn['font'] = myfont
        
        U_eth = tk.Button(master, text = u'\u00D0',width = 3,height = 1, command = lambda: press(u'\u00D0'))
        U_eth.grid(row = 2, column = 2)
        U_eth['font'] = myfont
        
        L_eth = tk.Button(master, text = u'\u00F0',width = 3,height = 1, command = lambda: press(u'\u00F0'))
        L_eth.grid(row = 2, column = 3)
        L_eth['font'] = myfont
        
        U_wynn = tk.Button(master, text = u'\u01F7',width = 3,height = 1, command = lambda: press(u'\u01F7'))
        U_wynn.grid(row = 2, column = 4)
        U_wynn['font'] = myfont
        
        L_wynn = tk.Button(master, text = u'\u01BF',width = 3,height = 1, command = lambda: press(u'\u01BF'))
        L_wynn.grid(row = 2, column = 5)
        L_wynn['font'] = myfont
        
        ####
            
        U_Gdot = tk.Button(master, text = u'\u0120',width = 3,height = 1, command = lambda: press(u'\u0120'))
        U_Gdot.grid(row = 3, column = 0)
        U_Gdot['font'] = myfont
        
        L_Gdot = tk.Button(master, text = u'\u0121',width = 3,height = 1, command = lambda: press(u'\u0121'))
        L_Gdot.grid(row = 3, column = 1)
        L_Gdot['font'] = myfont
        
        U_Cdot = tk.Button(master, text = u'\u010A',width = 3,height = 1, command = lambda: press(u'\u010A'))
        U_Cdot.grid(row = 3, column = 2)
        U_Cdot['font'] = myfont
        
        L_Cdot = tk.Button(master, text = u'\u010B',width = 3,height = 1, command = lambda: press(u'\u010B'))
        L_Cdot.grid(row = 3, column = 3)
        L_Cdot['font'] = myfont
        ####
        
        tk.Label(master, text = "Vowels").grid(row = 4, columnspan = 6) 
        
        
        U_ash = tk.Button(master, text = u'\u00C6',width = 3,height = 1, command = lambda: press(u'\u00C6'))
        U_ash.grid(row = 5, column = 0)
        U_ash['font'] = myfont
        
        L_ash = tk.Button(master, text = u'\u00E6',width = 3,height = 1, command = lambda: press(u'\u00E6'))
        L_ash.grid(row = 5, column = 1)        
        L_ash['font'] = myfont
        
        U_ashmacron = tk.Button(master, text = u'\u01E2',width = 3,height = 1, command = lambda: press(u'\u01E2'))
        U_ashmacron.grid(row = 5, column = 2)
        U_ashmacron['font'] = myfont
        
        L_ashmacron = tk.Button(master, text = u'\u01E3',width = 3,height = 1, command = lambda: press(u'\u01E3'))
        L_ashmacron.grid(row = 5, column = 3)
        L_ashmacron['font'] = myfont
        
        U_Amacron = tk.Button(master, text = u'\u0100',width = 3,height = 1, command = lambda: press(u'\u0100'))
        U_Amacron.grid(row = 5, column = 4)
        U_Amacron['font'] = myfont
        
        L_Amacron = tk.Button(master, text = u'\u0101',width = 3,height = 1, command = lambda: press(u'\u0101'))
        L_Amacron.grid(row = 5, column = 5)
        L_Amacron['font'] = myfont
        ####
        
        U_imacron = tk.Button(master, text = u'\u012A',width = 3,height = 1, command = lambda: press(u'\u012A'))
        U_imacron.grid(row = 6, column = 2)
        U_imacron['font'] = myfont
        
        L_imacron = tk.Button(master, text = u'\u012B',width = 3,height = 1, command = lambda: press(u'\u012B'))
        L_imacron.grid(row = 6, column = 3)
        L_imacron['font'] = myfont
        
        U_Emacron = tk.Button(master, text = u'\u0112',width = 3,height = 1, command = lambda: press(u'\u0112'))
        U_Emacron.grid(row = 6, column = 0)
        U_Emacron['font'] = myfont
        
        L_Emacron = tk.Button(master, text = u'\u0113',width = 3,height = 1, command = lambda: press(u'\u0113'))
        L_Emacron.grid(row = 6, column = 1)
        L_Emacron['font'] = myfont
        
        U_Omacron = tk.Button(master, text = u'\u014C',width = 3,height = 1, command = lambda: press(u'\u014C'))
        U_Omacron.grid(row = 6, column = 4)
        U_Omacron['font'] = myfont
        
        L_Omacron = tk.Button(master, text = u'\u014D',width = 3,height = 1, command = lambda: press(u'\u014D'))
        L_Omacron.grid(row = 6, column = 5)
        L_Omacron['font'] = myfont
        ####

        
        U_umacron = tk.Button(master, text = u'\u016A',width = 3,height = 1, command = lambda: press(u'\u016A'))
        U_umacron.grid(row = 7, column = 0)
        U_umacron['font'] = myfont
        
        L_umacron = tk.Button(master, text = u'\u016B',width = 3,height = 1, command = lambda: press(u'\u016B'))
        L_umacron.grid(row = 7, column = 1)
        L_umacron['font'] = myfont
        
        U_Ymacron = tk.Button(master, text = u'\u0232',width = 3,height = 1, command = lambda: press(u'\u0232'))
        U_Ymacron.grid(row = 7, column = 2)
        U_Ymacron['font'] = myfont
        
        L_Ymacron = tk.Button(master, text = u'\u0233',width = 3,height = 1, command = lambda: press(u'\u0233'))
        L_Ymacron.grid(row = 7, column = 3)
        L_Ymacron['font'] = myfont
        ####
    
    
root = tk.Tk()
my_gui = OE_Keyboard(root)
root.mainloop()   