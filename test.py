import subprocess

applescript = ('tell application "Calendar" to '
          'tell calendar "Privat" to '
          'make new event with properties {summary:"titel", location:"ort", '
          'start date:date "1. Mai 2025 15:00", end date:date "1. Mai 2025 16:00"}')

# oder in einer Zeile:
# applescript = 'tell application "Calendar" to tell calendar "Privat" to make new event with properties {summary:"titel", location:"ort", start date:date "1. Mai 2025 15:00", end date:date "1. Mai 2025 16:00"}'

try:
    subprocess.run(["osascript", "-e", applescript], check=True)
    print("Termin hinzugefügt.")
except subprocess.CalledProcessError as e:
    print(f"Fehler beim Hinzufügen: {e}")