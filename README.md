# LiveEdgeRecorder

Dieses Projekt erkennt Kanten in einem Live-Video und ermöglicht es, Fotos und Videos von den erkannten Kanten zu speichern.

Volage für das Projekt von `The Morpheus Tutorials` --> [https://www.youtube.com/watch?v=-XXj-uLdGmQ]
## Funktionen:
- Dynamische Kantenerkennung mit benutzerdefinierten Schwellenwerten.
- Fotos im `.jpg`-Format speichern.
- Videos im `.avi`-Format aufnehmen.

## Anforderungen:
Um das Projekt auszuführen alle benötigten Python-Pakete installieren.

```bash
pip install -r requirements.txt
```

## Nutzung

1. **Starte das Skript**:

2. **Tastenkürzel**:
   - `f`: Foto aufnehmen und im Ordner `captures/` speichern.
   - `v`: Videoaufnahme starten und im `.avi`-Format speichern.
   - `s`: Videoaufnahme stoppen.
   - `q`: Programm beenden.

3. **Ergebnisse speichern**:
   - Fotos werden im `captures/` Ordner unter einem Zeitstempel gespeichert.
   - Videos werden ebenfalls im `captures/` Ordner gespeichert und auch mit Zeitstempel benannt.
