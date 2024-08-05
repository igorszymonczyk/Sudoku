import os
import webbrowser

def calculate_average_times():
    times = {}
    try:
        with open("C:\\Users\\Szymo\\Desktop\\studia\\semestr 3\\jezyki skryptowe\\Projekt\\output.txt", "r") as file:
            for line in file:
                parts = line.strip().split(': ')
                if len(parts) != 2 or not parts[0].startswith('Plansza '):
                    print(f"Nieprawidłowy format linii: {line.strip()}")
                    continue

                grid_index = int(parts[0].split()[1])
                time = float(parts[1].split()[0])

                if grid_index not in times:
                    times[grid_index] = []
                times[grid_index].append(time)

        averages = {grid: sum(times_list) / len(times_list) for grid, times_list in times.items()}
        return averages
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return {}

def generate_html_report():
    averages = calculate_average_times()

    html_content = "<html><head><title>Raport Sudoku</title></head><body>"
    html_content += "<h1>Średni czas gry na planszy</h1>"
    for grid, avg_time in averages.items():
        html_content += f"<p>Plansza {grid}: {avg_time:.2f} sekund</p>"
    html_content += "</body></html>"

    with open("raport.html", "w") as file:
        file.write(html_content)

generate_html_report()
webbrowser.open('file://' + os.path.realpath('raport.html'))
