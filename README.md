WAŻNE, PAMIĘTAJCIE PRACOWAC NA SWOICH "Branches"











# Strona Python - Instrukcja Instalacji i Uruchomienia

## Wymagania wstępne
- Python 3.10 lub nowszy (sprawdź wersję: `python --version`)
- PIP (instalator pakietów Pythona)
- PostgreSQL (zainstalowany i skonfigurowany)
- Wirtualne środowisko (VENV)

---

## Instalacja projektu na nowym komputerze

### 1. Sklonuj repozytorium lub skopiuj pliki projektu
Upewnij się, że projekt znajduje się na Twoim komputerze.

```bash
git clone <url_do_repozytorium>
cd <nazwa_folderu_projektu>
```
2. Utwórz wirtualne środowisko (jeżeli nie jest już w projekcie, sprawdzic jak)
W folderze projektu utwórz wirtualne środowisko:

```bash
odpal terminal
wpisuj komendy:
cd (sciezka do pliku gdzie masz strone \projekt_studia\strona_studia)
python -m venv venv
```
3. Aktywuj wirtualne środowisko
```
bash
venv\Scripts\activate
```
4.Wykonaj migracje bazy danych
Aby skonfigurować bazę danych, wykonaj poniższe polecenia:

```bash
python manage.py makemigrations
python manage.py migrate
```
5. Uruchom serwer
Uruchom serwer developerski, aby zobaczyć stronę w przeglądarce:

```bash
python manage.py runserver
```
Domyślnie aplikacja będzie dostępna pod adresem:
http://127.0.0.1:8000




kolejnosc
```
cd (sciezka do pliku gdzie masz strone \projekt_studia\strona_studia)
python -m venv venv
pip install django
venv\Scripts\activate
python manage.py runserver
```
