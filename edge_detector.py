import cv2
import os
import time

# Callback-Funktion für die Trackbar
def nothing(x):
    pass

# Kamera initialisieren
cam = cv2.VideoCapture(0)

# Fenster für Kantendarstellung
cv2.namedWindow('Kantich')

# Trackbars für Schwellenwerte
cv2.createTrackbar('Min Threshold', 'Kantich', 30, 255, nothing)
cv2.createTrackbar('Max Threshold', 'Kantich', 100, 255, nothing)

# Ordner erstellen für gespeicherte Dateien
os.makedirs("captures", exist_ok=True)

# Initialisierung für Videoaufnahme
is_recording = False
video_writer = None

while True:
    # Frame von der Kamera lesen
    _, image = cam.read()
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Schwellenwerte von Trackbars abrufen
    min_thresh = cv2.getTrackbarPos('Min Threshold', 'Kantich')
    max_thresh = cv2.getTrackbarPos('Max Threshold', 'Kantich')
    
    # Kanten erkennen
    edges = cv2.Canny(grey, min_thresh, max_thresh)
    
    # Bild anzeigen
    cv2.imshow('Kantich', edges)

    # Video aufnehmen, falls aktiviert
    if is_recording and video_writer:
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        video_writer.write(edges_bgr)

    # Tasteneingaben
    key = cv2.waitKey(1)

    # Beenden der Schleife mit der Taste "q"
    if key == ord("q"):
        break

    # Foto aufnehmen mit der Taste "f"
    elif key == ord("f"):
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        photo_path = f"captures/kantenfoto_{timestamp}.jpg"
        cv2.imwrite(photo_path, edges)
        print(f"Kanten-Foto gespeichert: {photo_path}")

    # Videoaufnahme starten mit der Taste "v"
    elif key == ord("v"):
        if not is_recording:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            video_path = f"captures/kantenvideo_{timestamp}.avi"
            fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Alternativ 'MJPG' oder 'H264'
            frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = 20
            video_writer = cv2.VideoWriter(video_path, fourcc, fps, (frame_width, frame_height))
            is_recording = True
            print(f"Kanten-Videoaufnahme gestartet: {video_path}")
        else:
            print("Kanten-Videoaufnahme läuft bereits.")

    # Videoaufnahme stoppen mit der Taste "s"
    elif key == ord("s") and is_recording:
        is_recording = False
        video_writer.release()
        video_writer = None
        print("Kanten-Videoaufnahme beendet.")

# Kamera und Ressourcen freigeben
cam.release()
if video_writer:
    video_writer.release()
cv2.destroyAllWindows()
