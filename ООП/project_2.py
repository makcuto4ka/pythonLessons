import tkinter as tk
from tkinter import messagebox

class Matryoshka:
    def __init__(self, size, color):
        self.size = size
        self.color = color

class Player:
    def __init__(self, color, matryoshkas):
        self.color = color
        self.matryoshkas = matryoshkas 
        self.score = 0

    def reset_matryoshkas(self, count):
        self.matryoshkas = [Matryoshka(i+1, self.color) for i in range(count)]

class GameBoard:
    def __init__(self, size=3):
        self.size = size

    def place_matryoshka(self, row, col, matryoshka):
        current = self.cells[row][col]
        if current is None or current.size < matryoshka.size:
            self.cells[row][col] = matryoshka
            return True
        return False

    def check_winner(self):
        check = []
        lines = []
        columns = []
        diag = []
        n = self.size  
        for i in range(n):
            lines.append(self.cells[i])     
            columns.append([self.cells[r][i] for r in range(n)])
        diag1 = [self.cells[i][i] for i in range(n)]
        diag2 = [self.cells[i][n-1-i] for i in range(n)]
        check.append(lines)
        check.append(columns)
        diag.append(diag1)
        diag.append(diag2)
        for ch in check:
            for j in ch:
                if None not in j:
                    colors = [c.color for c in j]
                    if all(cl == colors[0] for cl in colors):
                        return True

        for dg in diag:
            if None not in dg:
                colors = [c.color for c in dg]
                if all(cl == colors[0] for cl in colors):
                    return True
        return False

    def reset(self):
        self.cells = [[None]*self.size for _ in range(self.size)]

class GameGUI:
    COLORS = ["red", "blue", "green", "purple"]

    def __init__(self):
        self.gui = tk.Tk()
        self.gui.title("Матрёшки")
        self.board = GameBoard()
        self.players = []
        self.current_index = 0
        self.selected_size = None
        self.num_matryoshkas = 6
        self.cell_size = 100

        self.setup_menu()
        self.create_widgets()
        self.open_settings()
        self.gui.mainloop()

    def setup_menu(self):
        menu = tk.Menu(self.gui)
        settings_menu = tk.Menu(menu, tearoff=0)
        settings_menu.add_command(label="Начать заново", command=self.open_settings)
        menu.add_cascade(label="Настройки", menu=settings_menu)
        self.gui.config(menu=menu)

    def create_widgets(self):
        self.canvas = tk.Canvas(self.gui, width=self.cell_size*self.board.size, height=self.cell_size*self.board.size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.matryoshkas_frame = tk.Frame(self.gui)
        self.matryoshkas_frame.pack(pady=10)

        self.status_label = tk.Label(self.gui, text="")
        self.status_label.pack()

    def open_settings(self):
        dlg = tk.Toplevel(self.gui)
        dlg.title("Насройки")

        tk.Label(dlg, text="Выберите количество матрёшек (3–10):").grid(row=0, column=0)
        slider = tk.Scale(dlg, from_=3, to=10, orient=tk.HORIZONTAL)
        slider.set(self.num_matryoshkas)
        slider.grid(row=0, column=1)

        selection = {}
        canvases = {}
        for idx, key in enumerate(("p1", "p2"), start=1):
            tk.Label(dlg, text=f"Игрок {idx} цвет:").grid(row=idx, column=0)
            frame = tk.Frame(dlg)
            frame.grid(row=idx, column=1)
            canvases[key] = []
            for col in self.COLORS:
                cc = tk.Canvas(frame, width=24, height=24)
                oid = cc.create_oval(2,2,22,22, fill=col, outline="black")
                cc.pack(side=tk.LEFT)
                canvases[key].append((cc, oid, col))
                def make_handler(c, k):
                    def h(event=None):
                        selection[k] = c
                        for w, oid2, _ in canvases[k]:
                            w.itemconfig(oid2, outline="black", width=1)
                        for w, oid2, color in canvases[k]:
                            if color == c:
                                w.itemconfig(oid2, outline="yellow", width=2)
                    return h
                cc.bind("<Button-1>", make_handler(col, key))

        def start():
            c1, c2 = selection.get('p1'), selection.get('p2')
            if not c1 or not c2:
                messagebox.showwarning("Error", "Игроки должны выбрать цвета.")
                return
            if c1 == c2:
                messagebox.showwarning("Error", "У игроков должны быть разные цвета.")
                return
            self.num_matryoshkas = slider.get()
            self.init_game(c1, c2)
            dlg.destroy()

        tk.Button(dlg, text="Начать игру", command=start).grid(row=3, column=0, columnspan=2)
        dlg.transient(self.gui)
        dlg.grab_set()
        self.gui.wait_window(dlg)

    def init_game(self, c1, c2):
        self.players = [Player( c1, []), Player( c2, [])]
        for p in self.players:
            p.reset_matryoshkas(self.num_matryoshkas)
        self.current_index = 0
        self.selected_size = None
        self.board.reset()
        self.canvas.delete("all")
        self.draw_grid()
        self.draw_matryoshka_select()
        self.update_status()

    def draw_grid(self):
        for i in range(self.board.size+1):
            self.canvas.create_line(0, i*self.cell_size,
                                     self.cell_size*self.board.size, i*self.cell_size)
            self.canvas.create_line(i*self.cell_size, 0,
                                     i*self.cell_size, self.cell_size*self.board.size)

    def draw_matryoshka_select(self):
        for w in self.matryoshkas_frame.winfo_children():
            w.destroy()
        for matryoshka in self.players[self.current_index].matryoshkas:
            c = tk.Canvas(self.matryoshkas_frame, width=40, height=40, highlightthickness=0)
            x0, y0 = 20, 20
            maxr = 15
            r = matryoshka.size * maxr / self.num_matryoshkas
            c.create_oval(x0-r, y0-r, x0+r, y0+r, fill=matryoshka.color)
            c.create_text(x0, y0, text=str(matryoshka.size), fill='white')
            c.pack(side=tk.LEFT, padx=5)
            def handler(sz=matryoshka.size, widget=c):
                self.selected_size = sz
                for w in self.matryoshkas_frame.winfo_children():
                    w.configure(bg=self.gui['bg'])
                widget.configure(bg='lightgrey')
            c.bind("<Button-1>", lambda e, h=handler: h())

    def on_canvas_click(self, event):
        if self.selected_size is None:
            messagebox.showwarning("Выберите матрешку", "Сначала выбери матрешку.")
            return
        row, col = event.y // self.cell_size, event.x // self.cell_size
        player = self.players[self.current_index]
        matryoshka = next((p for p in player.matryoshkas if p.size == self.selected_size), None)
        if not self.board.place_matryoshka(row, col, matryoshka):
            messagebox.showwarning("Invalid", "Не удается разместить на равной или большей матрешке.")
            return
        player.matryoshkas.remove(matryoshka)
        self.draw_matryoshka(row, col, matryoshka)
        if self.board.check_winner():
            player.score += 1
            messagebox.showinfo("Раун окончен", f"{player.color} победил!")
            self.next_round()
            return
        self.current_index = 1 - self.current_index
        self.selected_size = None
        self.draw_matryoshka_select()
        self.update_status()

    def draw_matryoshka(self, row, col, matryoshka):
        x0 = col*self.cell_size + self.cell_size/2
        y0 = row*self.cell_size + self.cell_size/2
        maxr = self.cell_size/2 - 5
        r = matryoshka.size * maxr / self.num_matryoshkas
        self.canvas.create_oval(x0-r, y0-r, x0+r, y0+r, fill=matryoshka.color)
        self.canvas.create_text(x0, y0, text=str(matryoshka.size), fill='white')

    def next_round(self):
        for p in self.players:
            p.reset_matryoshkas(self.num_matryoshkas)
        self.board.reset()
        self.canvas.delete('all')
        self.draw_grid()
        self.selected_size = None
        self.draw_matryoshka_select()
        self.update_status()

    def update_status(self):
        p1, p2 = self.players
        self.status_label.config( text=f"{p1.color}: {p1.score}  |  {p2.color}: {p2.score}")

GameGUI()
