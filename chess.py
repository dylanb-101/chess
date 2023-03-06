from tkinter import N, W, E, S,StringVar, ttk, Canvas
from PIL import ImageTk, Image

class Chess():

    

    def __init__(self, root):
        

        # self.root = root
        root.minsize(500, 500)
        root.resizable(False, False)
        root.title("Chess")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # frame = ttk.Frame(root)

        canvas = Canvas(root, width=500, height=500)
        canvas.grid(column=0, row=0, sticky=(N, W, E, S))

        canvas.create_rectangle(0, 0, 60, 60, fill='#2c1608', outline='black')

        board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]

        for col, y in board:
            for row, x in col:
                if x + y % 2 == 0:
                    canvas.create_rectangle(x*60, y*60, x+60, x+60, fill='#2c1608', outline='black')
                else:
                    canvas.create_rectangle(x*60, y*60, x+60, x+60, fill='white', outline='black')


# class Board():
#     def __init__(self, canvas):
#         board = [
#             ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
#             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
#             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
#             ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
#         ]

#         for col, y in board:
#             for row, x in col:
#                 if x + y % 2 == 0:
#                     canvas.create_rectangle(x*60, y*60, x+60, x+60, fill='#2c1608', outline='black')
#                 else:
#                     canvas.create_rectangle(x*60, y*60, x+60, x+60, fill='white', outline='black')
        


        
            
        


        

    

        