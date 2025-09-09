from tkinter import *
import tkinter.font as tkFont
import random
import math

class TreasureHunt:

    def __init__(self, master):
        app = Frame(master, bg="yellow")
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(1, weight=1)
        app.grid_columnconfigure(0, weight=1)
        app.pack(fill="both", expand=True)
        # instructions and fonts
        self.mono_font = tkFont.Font(family="Courier",size=24,weight="bold")
        self.instructions = "Find the hidden treasure!\n\nUse the arrow keys to select where to look, then press Enter to check. \
        There is a 50/50 chance you will be told the distance from the treasure. Keep hunting until you find it. Good luck!"
        # create instructions widget
        self.info = Text(app, wrap=WORD, padx=10, pady=10,width=15,bd=0, height=19, bg="yellow")
        self.info.insert(1.0,self.instructions)
        self.info.grid(row=0,column=0,sticky=N+E+S+W)
        # create island widget
        self.island = Text(app, bg="cyan", padx=40, pady=40, font=self.mono_font,width=15, height=9, wrap=NONE,bd=0)
        self.island.insert(1.0, "ready")
        self.island.grid(row=0,column=1, stick=N+E+S+W, rowspan=3)
        # restart button
        self.restart_b = Button(app, text="Restart", bg="red", command=self.begin)  
        self.restart_b.grid(row=2, column=0, pady=20)
        # score labels and fields
        self.score_lbl = Label(app, text="Guesses: 0", bg="yellow")
        self.score_lbl.grid(row=1, column=0)

        # set keydown handler
        root.bind("<Key>", self.key_pressed)
        # best score variable
        self.best_score = 0
        # begin game
        self.begin()
        #print self.treasure_pos

    def begin(self):
        # game state variables
        root.after_cancel(self.tick)
        self.matrix = [["#" for col in range(8)] for row in range(8)]
        self.current_pos = [0,0]
        self.treasure_pos = [random.randrange(8), random.randrange(8)]
        #self.treasure_pos = [0,0]
        #print self.treasure_pos
        self.blink = False
        self.guesses = 0
        self.end_tick = False
        self.tick()

    def display_grid(self):
        '''Displays current visual game state'''
        self.island.delete(1.0, END) 
        m_str = ""
        for row in range(len(self.matrix)):
            m_str += (" ".join(self.matrix[row]) + "\n")
        self.island.insert(1.0, m_str)

    def process_guess(self):
        self.guesses += 1
        self.score_lbl.config(text="Guesses: " + str(self.guesses))
        if not (self.current_pos[0] == self.treasure_pos[0] and self.current_pos[1] == self.treasure_pos[1]):
            #print "NOT HERE"
            dist = int(round(math.sqrt((self.current_pos[0] - self.treasure_pos[0]) ** 2 + (self.current_pos[1] - self.treasure_pos[1]) ** 2)))
            self.matrix[self.current_pos[0]][self.current_pos[1]] = str(dist)
            self.display_grid()
        else:
            self.end_tick = True

    def finish(self):
        self.matrix[self.treasure_pos[0]][self.treasure_pos[1]] = "$"
        self.display_grid()
        self.island.insert(END, "Gold!")

    def tick(self):
        '''timer for blinking cursor'''
        if self.blink == False:
            self.matrix[self.current_pos[0]][self.current_pos[1]] = "#"
        elif self.blink == True:
            self.matrix[self.current_pos[0]][self.current_pos[1]] = " "
        self.blink = not self.blink
        self.display_grid()
        if not self.end_tick:
            root.after(200, self.tick)
        else:
            self.finish()

    def key_pressed(self, event):
        if event.keysym == "Right" and self.current_pos[1] < 7:
            self.current_pos[1] += 1
        elif event.keysym == "Left" and self.current_pos[1] > 0:
            self.current_pos[1] -= 1
        elif event.keysym == "Up" and self.current_pos[0] > 0:
            self.current_pos[0] -= 1
        elif event.keysym == "Down" and self.current_pos[0] < 7:
            self.current_pos[0] += 1
        elif event.keysym == "Return":
            self.process_guess()
        self.display_grid()
        self.matrix = [["#" for col in range(8)] for row in range(8)] # is here the best place for this?


root = Tk()
game = TreasureHunt(root)
root.mainloop()
