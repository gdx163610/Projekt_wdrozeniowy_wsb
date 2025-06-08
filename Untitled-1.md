# Dokumentacja projektu: System Zarządzania Uczelnią

## 1. Opis projektu

System zarządzania uczelnią to aplikacja internetowa, która pozwala na organizację planu zajęć, zarządzanie grupami studentów, salami, ocenami, wykładowcami oraz harmonogramem. System został zaprojektowany jako aplikacja oparta na Pythonie z wykorzystaniem frameworka Django do obsługi backendu i frontendowych szablonów.

---

## 2. Struktura projektu

### 2.1. Główne podstrony

1. **Strona główna**  
   - Prezentuje podstawowe informacje o uczelni.
   - Nawigacja do głównych funkcjonalności systemu.

2. **Plan lekcji**  
   - Wyświetlanie harmonogramu zajęć.
   - Szczegóły zajęć (data, godzina, sala, prowadzący).

3. **Oceny**  
   - Widok ocen dla studentów i wykładowców.

4. **Forum**  
   - Moduł dyskusyjny dla studentów i wykładowców.

5. **Kalendarz**  
   - Wizualizacja planu zajęć w formie kalendarza.

6. **Terminy egzaminów**  
   - Lista terminów egzaminów przypisanych do grup studentów.

---

## 3. Architektura projektu

### 3.1. Technologie

- **Język programowania:** Python
- **Framework backendowy:** Django
- **Baza danych:** SQLite (domyślnie, łatwa do zmiany na PostgreSQL)
- **Frontend:** Django Templates (HTML, CSS, JS, Tailwind)
- **Przechowywanie plików:** Brak dedykowanego systemu (możliwość rozbudowy)
- **API:** REST API dla komunikacji wewnętrznej (opcjonalnie do rozbudowy)

---

### 3.2. Struktura folderów

```
PROJEKT-STUDIA/
|-- manage.py                 # Narzędzie zarządzania projektem Django
|-- db.sqlite3                # Baza danych SQLite
|-- requirements.txt          # Lista zależności Pythona
|-- strona_studia/            # Konfiguracja projektu Django
|   |-- settings.py           # Ustawienia projektu
|   |-- urls.py               # Główne mapowanie URL
|   |-- wsgi.py, asgi.py      # Pliki serwera aplikacji
|-- uczelnia/                 # Główna aplikacja funkcjonalna
|   |-- migrations/           # Migracje bazy danych
|   |-- templates/            # Szablony HTML
|   |   |-- uczelnia/
|   |       |-- home.html
|   |       |-- grades.html
|   |       |-- lecturer_list.html
|   |       |-- user_profile.html
|   |-- static/               # Zasoby statyczne (CSS, JS, obrazki)
|   |   |-- css/
|   |       |-- style.css
|   |-- admin.py              # Rejestracja modeli w panelu admina
|   |-- apps.py               # Konfiguracja aplikacji
|   |-- models.py             # Modele danych
|   |-- views.py              # Logika widoków
|   |-- urls.py               # Routing aplikacji
```

---

## 4. Funkcjonalności

### 4.1. Zarządzanie planem zajęć

- **Tworzenie zajęć:**  
  Formularz do wprowadzenia nazwy zajęć, daty, czasu trwania, sali i grupy.
- **Wyświetlanie harmonogramu:**  
  Lista zajęć w formie tabeli z możliwością przejścia do szczegółów.

### 4.2. Widok ocen

- **Dla studentów:**  
  Wyświetlanie ocen przypisanych do konkretnej osoby.
- **Dla wykładowców:**  
  Możliwość wprowadzenia ocen dla grupy studentów.

### 4.3. Forum dyskusyjne

- System postów i komentarzy.
- Podział na tematy (np. przedmioty).

### 4.4. Kalendarz zajęć

- Wizualizacja planu w formie kalendarza.
- Eksport do pliku CSV (opcjonalne).

### 4.5. Bezpieczeństwo

- Autoryzacja na podstawie ról (administrator, wykładowca, student).
- Logowanie i rejestracja z kontrolą danych.

---

## 5. Konfiguracja projektu

### 5.1. Baza danych

1. Upewnij się, że SQLite jest dostępny (domyślnie w Pythonie).
2. Jeśli chcesz użyć PostgreSQL:
   ```sql
   CREATE DATABASE university_schedule;
   CREATE USER your_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE university_schedule TO your_user;
   ```

### 5.2. Migracje Django

1. Wykonaj migracje:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 5.3. Tworzenie konta administratora

1. Utwórz konto administratora:
   ```bash
   python manage.py createsuperuser
   ```

---

## 6. Testowanie

### 6.1. Testy manualne

1. Uruchom lokalny serwer:
   ```bash
   python manage.py runserver
   ```
2. Sprawdź dostęp do podstron:
   - Strona główna: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Plan lekcji: [http://127.0.0.1:8000/plan-lekcji/](http://127.0.0.1:8000/plan-lekcji/)

### 6.2. Testy jednostkowe

Dodaj testy w `uczelnia/tests.py`:
```python
from django.test import TestCase
from .models import Sala

class SalaModelTest(TestCase):
    def test_create_sala(self):
        sala = Sala.objects.create(nazwa="Sala 101", lokalizacja="Budynek A")
        self.assertEqual(str(sala), "Sala 101")
```
Uruchom testy:
```bash
python manage.py test
```

---

## 7. Rozbudowa projektu

### 7.1. Integracja z zewnętrznymi API

1. **Google Maps API**  
   - Obliczanie czasu przejazdu między kampusami.
2. **Google Calendar**  
   - Eksport harmonogramu zajęć do kalendarza.

### 7.2. Przechowywanie plików

- Integracja z Amazon S3 lub Google Cloud Storage do przechowywania materiałów edukacyjnych.

### 7.3. Powiadomienia

- Powiadomienia e-mail/SMS o zmianach w planie zajęć (użycie Celery + Twilio).

---

## 8. Wymagania niefunkcjonalne

- **Szybkość działania:** Maksymalny czas ładowania strony: 3 sekundy.
- **Skalowalność:** Obsługa wielokampusu z możliwością dodania nowych oddziałów.
- **Bezpieczeństwo:**
  - Szyfrowanie danych w bazie.
  - Autoryzacja oparta na rolach.

---

## 9. Zależności i powiązania plików

### 9.1. Modele (`models.py`)

- Definiują strukturę danych: Student, Lecturer, Subject, Grade, Schedule, News, NewsRead.
- Każdy model to osobna tabela w bazie danych.
- Przykład: `Grade` jest powiązany z `Student` i `Subject`.

### 9.2. Widoki (`views.py`)

- Odpowiadają za logikę aplikacji.
- Pobierają dane z modeli, przetwarzają je i przekazują do szablonów.
- Przykład: Widok `home` pobiera najbliższe zajęcia, oceny i newsy dla zalogowanego użytkownika.

### 9.3. Szablony (`templates/`)

- Pliki HTML z miejscami na dynamiczne dane (np. `{% for grade in recent_grades %}`).
- Każda podstrona ma swój szablon (np. `home.html`, `grades.html`).

### 9.4. Pliki statyczne (`static/`)

- CSS, JS, obrazki.
- Odpowiadają za wygląd i interaktywność strony.

### 9.5. Routing (`urls.py`)

- Mapuje adresy URL na odpowiednie widoki.
- Przykład: `/grades/` → widok ocen.

### 9.6. Panel admina (`admin.py`)

- Pozwala administratorowi zarządzać wszystkimi danymi przez przeglądarkę.

---

## 10. Przepływ działania

1. Użytkownik wpisuje adres (np. `/home/`).
2. Django sprawdza w `urls.py`, który widok obsługuje ten adres.
3. Widok pobiera dane z modeli (`models.py`).
4. Widok przekazuje dane do szablonu HTML.
5. Szablon wyświetla dane użytkownikowi.
6. Wygląd strony ustalany jest przez CSS z `static/`.

---

## 11. Podsumowanie

Projekt jest modularny i łatwy do rozbudowy. Każda funkcjonalność ma swój model, widok, szablon i styl. Wszystkie części są ze sobą powiązane przez mechanizmy Django, co zapewnia spójność i bezpieczeństwo działania systemu.
