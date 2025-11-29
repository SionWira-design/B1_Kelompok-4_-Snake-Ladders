import tkinter as tk

def create_board(root):

    canvas = tk.Canvas(root, width=500, height=500, bg="white")
    canvas.pack()

    size = 50  
    color1 = "#f0d5b0"
    color2 = "#c79c60"


    for row in range(10):
        for col in range(10):
            x1 = col * size
            y1 = row * size
            x2 = x1 + size
            y2 = y1 + size

            if (row + col) % 2 == 0:
                color = color1
            else:
                color = color2

            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
    add_numbers(canvas)
    token = create_player_token(canvas)
    return canvas, token
def add_numbers(canvas, size = 50):
    number = 1
    for row in range (9, -1, -1):
        if (9 - row) % 2 == 0:
             cols = range(10)
        else:
             cols = range(9, -1, -1)
        for col in cols:
            x = col * size + size/2
            y = row * size + size/2
            canvas.create_text(x, y, text = str(number), font =( "Arial", 12))
            number += 1
def get_cell_center(number, size=50):
    # hitung row & col dari nomor (1-100)
    number -= 1
    row = 9 - (number // 10)
    col = number % 10

    # zig-zag: baris genap dihitung dari kiri → kanan
    # baris ganjil dihitung dari kanan → kiri
    if (9 - row) % 2 == 1:
        col = 9 - col

    # hitung titik tengah sel
    x = col * size + size / 2
    y = row * size + size / 2
    return x, y
def create_player_token(canvas, position =1, size =50):
    x, y =  get_cell_center(position,size)
    r=10
    token = canvas.create_oval(
        x - r, y - r,
        x + r, y + r,
        fill = "red"
    )
    return token

def move_player(canvas, token_id, position, size = 50):
    x, y = get_cell_center(position, size)
    x1, y1, x2, y2 = canvas.coords(token_id)
    current_x = (x1 + x2)/2
    current_y = (y1 + y2)/2
    dx = x - current_x
    dy = y - current_y
    canvas.move(token_id, dx, dy)

    
    

def main():
    root = tk.Tk()
    root.title("Game Ular Tangga - GUI")
    canvas, token = create_board(root)
    move_player(canvas, token, 37)
    root.mainloop()

if __name__ == "__main__":

    main()
