import subprocess
from datetime import datetime, timedelta
import locale

# Stelle sicher, dass deutsche Monatsnamen verwendet werden
try:
    locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
except locale.Error:
    print("Warnung: deutsche Locale konnte nicht gesetzt werden. Stelle sicher, dass 'de_DE.UTF-8' installiert ist.")

def parseTermine(dateipfad):
    with open(dateipfad, "r", encoding="utf-8") as f:
        inhalte = f.read()

    eintraege = inhalte.strip().split('---')
    termine = []

    for eintrag in eintraege:
        daten = {}
        for zeile in eintrag.strip().splitlines():
            zeile = zeile.strip()
            if not zeile or zeile.startswith("#"):
                continue  # Ignoriere leere Zeilen und reine Kommentare
            # Entferne Inline-Kommentare
            if "#" in zeile:
                zeile = zeile.split("#", 1)[0].strip()
            if ":" in zeile:
                key, value = zeile.split(":", 1)
                daten[key.strip().lower()] = value.strip()
        if daten:
            termine.append(daten)

    return termine

def buildApplescript(termin):
    kalender = termin.get("kalender", "Privat")
    titel = termin.get("titel", "Ohne Titel")
    datum = termin.get("datum")
    datumbis = termin.get("datumbis") or datum
    uhrzeit_von = termin.get("von")
    uhrzeit_bis = termin.get("bis")
    dauer = termin.get("dauer")
    ort = termin.get("ort", "")

    start_datetime = datetime.strptime(f"{datum} {uhrzeit_von}", "%Y-%m-%d %H:%M")

    if uhrzeit_bis:
        end_datetime = datetime.strptime(f"{datumbis} {uhrzeit_bis}", "%Y-%m-%d %H:%M")
    elif dauer:
        end_datetime = start_datetime + timedelta(minutes=int(dauer))
    else:
        end_datetime = start_datetime + timedelta(hours=1) # Standarddauer 1 Stunde

    # AppleScript erwartet: 1. Mai 2025 14:00
    dateStart = start_datetime.strftime('%-d. %B %Y %H:%M')
    dareEnd = end_datetime.strftime('%-d. %B %Y %H:%M')

    applescript = (
        f'tell application "Calendar" to '
        f'tell calendar "{kalender}" to '
        f'make new event with properties {{summary:"{titel}", location:"{ort}", '
        f'start date:date "{dateStart}", end date:date "{dareEnd}"}}'
    )

    # oder in einer Zeile:
    # applescript = f'''tell application "Calendar" to tell calendar "{kalender}" to make new event with properties {{summary:"{titel}", location:"{ort}", start date:date "{dateStart}", end date:date "{dareEnd}"}}'''

    return applescript

def createTermine(datei):
    termine = parseTermine(datei)
    for termin in termine:
        script = buildApplescript(termin)
        try:
            subprocess.run(["osascript", "-e", script], check=True)
            print(f"Termin '{termin.get('titel')}' hinzugefügt.")
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Hinzufügen von '{termin.get('titel')}': {e}")

if __name__ == "__main__":
    createTermine("termine.txt")