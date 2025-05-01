# text2termine

Ein kleines macOS-Tool, um Termine aus einer Textdatei automatisch in den Kalender zu importieren.

## Features

- Termine in natürlicher Textform definieren
- Unterstützt `Datum`, `DatumBis`, `Von`, `Bis`, `Dauer`, `Ort`, `Kalender`, `Titel`, `Beschreibung`
- Automatischer Fallback, falls `Bis` oder `DatumBis` fehlen
- Unterstützt Kommentare (Zeilen mit `#`)
- Läuft mit AppleScript (nur macOS)

## Nutzung

- python3 text2termine.py

## Termine festlegen

- in: termine.txt

## Format

Kalender: Privat
Titel: Meeting mit Team
Datum: 2025-05-01
DatumBis:
Von: 14:00
Bis: 15:00
Dauer:
Ort: Büro
Beschreibung: Test

---

Kalender: Privat
Titel: Kaffee mit Kevin
Datum: 2025-05-01
DatumBis:
Von: 16:00
Bis:
Dauer: 30
Ort: Café nebenan
Beschreibung:

---

### Optionale Werte

- DatumBis
- Bis
- Dauer

### Kommentare

- mit # möglich
