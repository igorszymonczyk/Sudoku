import sys
import pygame as pg
import random
import time
import subprocess

# Ustawienia okna
pg.init()
screen_size = 750, 870
screen = pg.display.set_mode(screen_size)

# Ustawienia czcionki
font = pg.font.SysFont(None, 80)

# Ustawienia czcionki dla czasu
time_font = pg.font.SysFont(None, 40)

# Zmienna do śledzenia czasu startu
start_time = None

# Plansza Sudoku
original_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

additional_grids = [
    [
        [0, 4, 0, 6, 0, 8, 0, 0, 0],
        [5, 6, 0, 9, 0, 0, 0, 2, 0],
        [1, 9, 7, 2, 4, 0, 3, 0, 0],
        [0, 8, 0, 0, 9, 7, 0, 0, 1],
        [0, 3, 0, 1, 0, 6, 0, 0, 5],
        [0, 0, 9, 5, 0, 3, 4, 6, 0],
        [0, 0, 0, 3, 5, 0, 1, 0, 8],
        [0, 0, 0, 0, 6, 0, 0, 4, 3],
        [0, 7, 3, 0, 0, 9, 6, 0, 2]
    ], 
    [
        [0, 0, 0, 0, 0, 8, 0, 0, 0],
        [3, 0, 0, 4, 2, 0, 1, 0, 0],
        [0, 0, 9, 5, 6, 1, 0, 0, 4],
        [2, 0, 6, 9, 0, 0, 5, 3, 1],
        [1, 0, 0, 0, 0, 7, 6, 0, 9],
        [9, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 5, 3],
        [0, 0, 1, 0, 3, 0, 4, 0, 0],
        [6, 0, 0, 0, 0, 0, 2, 0, 0]
    ], 
    [
        [0, 0, 6, 7, 0, 0, 0, 1, 0],
        [0, 2, 9, 3, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 1, 0, 0, 2, 0, 0, 3, 4],
        [0, 0, 8, 4, 0, 7, 9, 0, 0],
        [4, 9, 0, 0, 1, 0, 0, 7, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 5, 1, 9, 0],
        [0, 7, 0, 0, 0, 8, 5, 0, 0]
    ], 
    [
        [0, 0, 0, 5, 0, 2, 0, 6, 0],
        [2, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 5, 0, 4, 3, 1, 0, 0],
        [6, 0, 2, 0, 0, 0, 0, 0, 7],
        [0, 8, 7, 0, 3, 0, 6, 9, 0],
        [3, 0, 0, 0, 0, 0, 4, 0, 5],
        [0, 0, 6, 4, 7, 0, 9, 0, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 4],
        [0, 7, 0, 9, 0, 8, 0, 0, 0]
    ]
]
number_grid = [[0] * 9 for _ in range(9)]  # Początkowo pusta plansza

for i in range(9):
    for j in range(9):
        number_grid[i][j] = original_grid[i][j]

# Kolor komórek
cell_colors = [['given' if original_grid[i][j] != 0 else None for j in range(9)] for i in range(9)]

# Wybrana komórka (współrzędne w formie tuple: (row, col))
selected_cell = None

def read_input_settings():
    settings = {"kolor tła": "white"}  # domyślne ustawienia
    try:
        with open("C:\\Users\\Szymo\\Desktop\\studia\\semestr 3\\jezyki skryptowe\\Projekt\\input.txt", "r") as file:
            for line in file:
                key, value = line.strip().split(': ')
                settings[key] = value
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    return settings

background_color = read_input_settings()


settings = read_input_settings()

# Zastosowanie wybranej planszy
selected_grid_index = int(settings.get("wybrana plansza", "1")) - 1
original_grid = additional_grids[selected_grid_index]

# Zastosowanie limitu czasu (przykładowo jako maksymalny czas w sekundach)
time_limit = int(settings.get("limit czasu", "0").split()[0]) * 60

# Zastosowanie koloru tła
background_color = settings.get("kolor tła", "white")

def randomize_grid():
    return random.choice(additional_grids + [original_grid])

# Ustawienie początkowej planszy
original_grid = randomize_grid()

number_grid = [[0] * 9 for _ in range(9)]
for i in range(9):
    for j in range(9):
        number_grid[i][j] = original_grid[i][j]

cell_colors = [['given' if original_grid[i][j] != 0 else None for j in range(9)] for i in range(9)]
selected_cell = None

def draw_background():
    # Zastosowanie wybranego koloru tła
    screen.fill(pg.Color(background_color))
    pg.draw.rect(screen, pg.Color("black"), pg.Rect(15, 15, 720, 720), 10)
    for i in range(1, 9):
        line_width = 5 if i % 3 > 0 else 10
        pg.draw.line(screen, pg.Color("black"), (i * 80 + 15, 15), (i * 80 + 15, 730), line_width)
        pg.draw.line(screen, pg.Color("black"), (15, i * 80 + 15), (730, i * 80 + 15), line_width)
    while (i * 80) < 720:
        # Pogrubienie co 3
        line_width = 5 if i % 3 > 0 else 10
        # Rysowanie pionowych linii
        pg.draw.line(screen, pg.Color("black"), pg.Vector2((i * 80) + 15, 15), pg.Vector2((i * 80) + 15, 730),
                     line_width)
        # Rysowanie poziomych linii
        pg.draw.line(screen, pg.Color("black"), pg.Vector2(15, (i * 80) + 15), pg.Vector2(730, (i * 80) + 15),
                     line_width)
        i += 1

def draw_numbers():
    # Rysowanie liczb na planszy
    row = 0
    offset = 35
    while row < 9:
        col = 0
        while col < 9:
            output = number_grid[row][col]
            color = cell_colors[row][col]
            if output != 0:
                n_text = font.render(str(output), True, pg.Color('black') if color != 'user' else pg.Color('blue'))
                screen.blit(n_text, pg.Vector2((col * 80) + offset + 5, (row * 80) + offset - 2))
            col += 1
        row += 1

def draw_selected_cell():
    # Rysowanie zaznaczonej komórki na niebiesko
    if selected_cell:
        row, col = selected_cell
        pg.draw.rect(screen, pg.Color("blue"), pg.Rect((col * 80) + 15, (row * 80) + 15, 80, 80), 5)

def is_valid_move(row, col, num):
    # Sprawdź wiersz
    if num in number_grid[row]:
        return False

    # Sprawdź kolumnę
    if num in [number_grid[i][col] for i in range(9)]:
        return False

    # Sprawdź kwadrat 3x3
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if number_grid[start_row + i][start_col + j] == num:
                return False

    return True

def is_given_number(row, col):
    # Sprawdź, czy liczba jest narzucona z góry (czarna)
    return cell_colors[row][col] == 'given'

def check_validity(row, col):
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    # Sprawdź poprawność wprowadzonej liczby
    num = number_grid[row][col]
    if num != 0:
        # Sprawdź wiersz, kolumnę i kwadrat
        valid_row = all(number != num for number in number_grid[row] if number != 0)
        valid_col = all(number != num for number in (number_grid[i][col] for i in range(9) if number_grid[i][col] != 0))
        valid_square = all(
            number != num for number in (
                number_grid[start_row + i][start_col + j] for i in range(3) for j in range(3)
                if number_grid[start_row + i][start_col + j] != 0
            )
        )
        return valid_row and valid_col and valid_square
    return True

def reset_game():
    global original_grid, number_grid, cell_colors, start_time, selected_grid_index
    # Resetowanie czasu przy każdym nowym starcie gry
    start_time = time.time()
    selected_grid_index = random.randint(0, len(additional_grids) - 1)
    original_grid = randomize_grid()
    number_grid = [[0] * 9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            number_grid[i][j] = original_grid[i][j]
    cell_colors = [['given' if original_grid[i][j] != 0 else None for j in range(9)] for i in range(9)]

reset_game() # Wywołanie funkcji reset_game na początku programu

def draw_time():
    # Wyświetlanie czasu gry
    if start_time:
        elapsed_time = time.time() - start_time
        time_string = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
        time_text = time_font.render(f"Czas: {time_string}", True, pg.Color("black"))
        screen.blit(time_text, (500, 790))

def save_time(grid_index):
    if start_time:
        elapsed_time = time.time() - start_time
        with open("C:\\Users\\Szymo\\Desktop\\studia\\semestr 3\\jezyki skryptowe\\Projekt\\output.txt", "a") as file:
             file.write(f"Plansza {grid_index + 1}: {elapsed_time:.2f} sekund\n")

def handle_input():
    global selected_cell, selected_grid_index
    for event in pg.event.get():
        if event.type == pg.QUIT:
            save_time(selected_grid_index)  # Zapisanie czasu przy zamykaniu gry
            subprocess.run(["python", "C:\\Users\\Szymo\\Desktop\\studia\\semestr 3\\jezyki skryptowe\\Projekt\\raport.py"])
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            # Obsługa kliknięcia myszą
            x, y = event.pos
            col = (x - 15) // 80
            row = (y - 15) // 80
            if 0 <= row < 9 and 0 <= col < 9:
                selected_cell = (row, col)
        elif event.type == pg.KEYDOWN and selected_cell:
            # Obsługa klawiatury
            row, col = selected_cell
            if event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                # Wprowadzenie liczby do planszy, jeśli jest to ruch dozwolony
                if not is_given_number(row, col):# and is_valid_move(row, col, int(event.unicode)) and check_validity(row, col):
                    number_grid[row][col] = int(event.unicode)
                    cell_colors[row][col] = 'user'  # Ustaw kolor dla liczby wprowadzonej przez użytkownika
            elif event.key == pg.K_BACKSPACE:
                # Usunięcie liczby z planszy za pomocą klawisza Backspace
                if not is_given_number(row, col):
                    number_grid[row][col] = 0
                    cell_colors[row][col] = None  # Usuń kolor, gdy liczba zostanie usunięta
            elif event.key == pg.K_r:
                # Resetowanie gry po naciśnięciu klawisza R
                reset_game()

def draw_reset_button():
    # Rysowanie przycisku RESET GRY
    reset_button_rect = pg.Rect(15, 780, 120, 50)
    reset_text = font.render("RESET GRY", True, pg.Color("black"))
    # Dostosuj rozmiar czcionki
    reset_font = pg.font.SysFont(None, 40)
    
    reset_text = reset_font.render("RESET GRY [R]", True, pg.Color("black"))
    screen.blit(reset_text, (25, 790))

def game_loop():
    # Główna pętla gry
    handle_input()
    draw_background()
    draw_numbers()
    draw_selected_cell()
    draw_reset_button()
    draw_time()
    pg.display.flip()

# Główna pętla programu
while True:
    game_loop()