from Tkinter import Frame , Label , CENTER
import  LogicsFinal
import Constants as c

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()  #to create a grid
        self.master.title('2048') #name of the grid
        self.master.bind("<Key>",self.key_down)  #movement functions 
        self.commands ={c.KEY_UP:LogicsFinal.move_up , 
                        c.KEY_DOWN:LogicsFinal.move_down,
                        c.KEY_LEFT:LogicsFinal.move_left,
                        c.KEY_RIGHT:LogicsFinal.move_right
                        }
        self.grid_cells =[]    #create empty cells
        self.init_grid()       #create grids in the master grid
        self.init_matrix()      #change the matrix like adding '2' randomly at random place  
        self.update_grid_cells()  #change the UI

        self.mainloop()

#initializing grid
    def init_grid(self):
        #creating anpther frame inside Frame 
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,width =c.SIZE , height=c.SIZE)
        background.grid()

        #adding cells
        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                #creating another frame name cell inside background with color to be a color of a empty cell
                cell = Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                            width=c.SIZE/c.GRID_LEN ,
                            height = c.SIZE / c.GRID_LEN)
                #adding cells 
                cell.grid(row = i ,column=j ,padx = c.GRID_PADDING , 
                        pady = c.GRID_PADDING )
                
                #inside cell adding label grid which takes text
                t = Label(master=cell , text="" ,
                        bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                        justify=CENTER ,font=c.FONT , width =5 , height =2)

                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    #creates a internal matrix .using this internal matrix we will make changes in the UI
    def init_matrix(self):
        self.matrix =LogicsFinal.start_game()
        LogicsFinal.add_new_2(self.matrix)
        LogicsFinal.add_new_2(self.matrix)

    #update the grid based on the internal matrix named(matrix)
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="" , bg= c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number) , bg= c.BACKGROUND_COLOR_DICT[new_number],
                        fg =c.CELL_COLOR_DICT[new_number])
        #update_idletasks waits before taking the next step or next input till all the color of the grid is changed
        self.update_idletasks()

    #performs based on the event(key pressed) occurred
    def key_down(self,event):
        key = repr(event.char) 
        if key in self.commands:
            self.matrix , changed = self.commands[repr(event.char)](self.matrix)

            if changed:
                #if there is some change we will add 2 things
                #1.add '2' to the matrix
                #2.then update the matrix
                LogicsFinal.add_new_2(self.matrix)
                self.update_grid_cells()
                changed=False

                #now checks if the user has WON OR LOST OR THE GAME IS STILL IN PLAY
                if LogicsFinal.get_current_state(self.matrix)=='WON':
                    self.grid_cells[1][1].configure(
                        text="YOU" , bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="WIN!" , bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                
                if LogicsFinal.get_current_state(self.matrix)=='LOST':
                    self.grid_cells[1][1].configure(
                        text="YOU" , bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="LOSE!" , bg=c.BACKGROUND_COLOR_CELL_EMPTY)

gamegrid = Game2048()
                    

                    
                              




        
