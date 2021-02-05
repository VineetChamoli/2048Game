SIZE =400 #SCREEN SIZE WILL BE 400
GRID_LEN = 4   # ie.; 4x4 
GRID_PADDING = 10 

BACKGROUND_COLOR_GAME ="#414a4c"   #background color of the game
BACKGROUND_COLOR_CELL_EMPTY = "#20f1f6"   #background color of the empty cells (ie; cells containing zeroes '0' )

#background color of each cell with  with different values
BACKGROUND_COLOR_DICT = {2 : "#b914e5" , 4:"#c02be7" , 8: "#c742ea" , 
                        16:"#ce5aec" ,32: "#d572ef" , 64:"#dc89f2" ,
                        128: "#e3a1f4" ,256:"#1099b7"  ,512: "#12acce" , 
                        1024:"#14c0e5"  ,2048:"#a1e5f4"} 

#background color of text
CELL_COLOR_DICT = {2 : "#ffffff" , 4:"#ffffff" , 8: "#ffffff" ,
                  16:"#ffffff" ,32: "#f67036" , 64:"#f67036" ,
                  128: "#f67036" ,256:"#f67036"  ,512: "#feefe8" ,
                  1024:"#feefe8"  ,2048:"#fccfbc"}

#font style
FONT = ('VARDANA',40, "bold")


#movement keys
KEY_UP   ="'w'"
KEY_DOWN ="'s'"
KEY_LEFT ="'a'"
KEY_RIGHT="'d'"
