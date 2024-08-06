# Sudoku Game in Python

### Wprowadzenie
Projekt Gra Sudoku to aplikacja stworzona w języku Python z wykorzystaniem biblioteki Pygame. Aplikacja umożliwia grę w Sudoku, generowanie raportów dotyczących czasu gry oraz tworzenie kopii zapasowych plików projektu.

### Struktura Projektu
Projekt składa się z trzech głównych komponentów:
1. `Sudoku.py`: Główny skrypt gry.
2. `raport.py`: Skrypt do generowania raportów HTML.
3. `run_sudoku.bat`: Plik wsadowy do uruchamiania gry i zarządzania projektami.

### Sudoku.py
Skrypt `Sudoku.py` jest sercem gry Sudoku. Zawiera logikę gry, interfejs użytkownika oraz zarządzanie czasem gry.

**Główne Komponenty:**
- Inicjalizacja Pygame i ustawienia ekranu.
- Ładowanie i wyświetlanie plansz Sudoku.
- Obsługa zdarzeń (np. kliknięcia myszą, wprowadzanie liczb).
- Rysowanie interfejsu użytkownika (plansza, liczby, przycisk resetowania).
- Zapisywanie czasu gry i wybór aktywnej planszy.
- Wywołanie skryptu `raport.py` przy zamykaniu aplikacji.

### Raport.py
Skrypt `raport.py` służy do generowania raportu w formacie HTML, który zawiera średni czas gry dla każdej planszy.

**Główne Funkcje:**
- Czytanie danych z pliku `output.txt`.
- Obliczanie średniego czasu gry na każdej planszy.
- Generowanie pliku HTML z wynikami.
- Automatyczne otwieranie wygenerowanego raportu w przeglądarce.

### Run_sudoku.bat
Plik `run_sudoku.bat` to plik wsadowy, który umożliwia łatwe uruchamianie gry, generowanie raportów oraz tworzenie backupu plików projektu.

**Opcje:**
1. Uruchom program Python: Uruchamia skrypt `Sudoku.py`.
2. Generuj raport: Uruchamia skrypt `raport.py`.
3. Stwórz backup: Tworzy kopię pliku `Sudoku.py`.
4. Wyjdź: Zamyka menu wsadowe.

### Wymagania Systemowe
- Python 3.8 lub nowszy.
- Biblioteka Pygame.
- Dostęp do przeglądarki internetowej (dla raportu HTML).

### Instrukcja Uruchomienia
1. Uruchom plik `run_sudoku.bat`.
2. Wybierz odpowiednią opcję z menu.
3. Graj w Sudoku, generuj raporty lub twórz backupy zgodnie z potrzebami.
