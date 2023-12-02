### 1. Charakterystyka oprogramowania:

- **Nazwa skrócona:** PCP
- **Nazwa pełna:** Porównywarka Cen Produktów
- **Krótki opis ze wskazaniem celów:**
    Projekt Porównywarki Cen Produktów to narzędzie online, które umożliwia użytkownikom szybkie i skuteczne porównanie cen części produktów z wybranych witryn internetowych. Działa poprzez regularne skanowanie wybranych platform zakupowych w celu zbierania informacji o aktualnych cenach produktów. System następnie prezentuje te dane w przejrzysty sposób, umożliwiając konsumentom znalezienie najkorzystniejszych ofert.

### 2. Prawa autorskie:

- **Autorzy:**
    Piotr Kuras, Paweł Brunke, Grzegorz Hintz
- **Warunki licencyjne do oprogramowania wytworzonego przez grupę:**
    - **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**
        - Darmowe użytkowanie, kopiowanie, rozpowszechnianie i modyfikowanie oprogramowania są dozwolone pod warunkiem przypisania odpowiedniego uznanie autorstwa, braku użycia komercyjnego oraz udostępnienia utworów pochodnych na tych samych warunkach.

### 3. Specyfikacja wymagań:

| Identyfikator | Nazwa | Opis | Priorytet | Kategoria |
| --- | --- | --- | --- | --- |
| A1 | Skanowanie Stron Internetowych | Systematyczne skanowanie wybranych witryn internetowych w poszukiwaniu informacji o cenach produktów | 1 | Funkcjonalne |
| A2 | Interfejs Użytkownika | Intuicyjny interfejs umożliwiający łatwe porównywanie cen i korzystanie z różnych funkcji | 1 | Funkcjonalne |
| A3 | Historia Cen | Przechowywanie historii cen produktów i umożliwianie dostępu użytkownikom do tych informacji w formie wykresów | 1 | Funkcjonalne |
| A4 | Tworzenie kont użytkowników | Każdy użytkownik będzie mógł stworzyć konto i korzystać z porównywarki jako osobny user | 1 | Funkcjonalne |
| A5 | Powiadomienia | System powiadomień o istotnych zmianach cen, nowych produktach lub promocjach | 3 | Funkcjonalne |
| A6 | Przejrzystość | Interfejs użytkownika powinien być przejrzysty i prosty w obsłudze | 2 | Niefunkcjonalne |
| A7 | Dostępność | Zapewnienie dostępności usługi przez większość czasu, minimalizacja przestojów | 3 | Niefunkcjonalne |

### 4. Architektura systemu/oprogramowania:

- **Architektura rozwoju – stos technologiczny:**
    - Django 4.2.0
    - Python 3.10
    - Beautiful Soup
    - Requests
    - Bootstrap
    - ...
- **Architektura uruchomieniowa – stos technologiczny:**
    - `docker compose build`
    - `docker compose up`

### 5. Testy:

#### a. Scenariusz testów:

1. Zarejestrowane się na stronę, logowanie się na błędne dane do logowania.
2. Zarejestrowane się na stronę, logowanie się na poprawne dane do logowania, wpisanie błędnego linku produktu.
3. Zarejestrowane się na stronę, logowanie się na poprawne dane do logowania, wpisanie linku produktu z nieobsługiwanego sklepu.
4. Zarejestrowane się na stronę, logowanie się na poprawne dane do logowania, wpisanie poprawnego linku produktu z obsługiwanego sklepu, zaobserwowanie zmian.

#### b. Sprawozdanie z wykonania scenariuszy testów:

Raport w Excelu

