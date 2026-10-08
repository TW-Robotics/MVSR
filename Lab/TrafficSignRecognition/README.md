# Verkehrszeichenerkennung – Datensatzstruktur

Dieses Verzeichnis legt fest, **wie der Datensatz aufgebaut ist**. Bilder und Labels werden separat bereitgestellt (Link in der Angabe bzw. im Moodle-Kurs). Laden und Auswerten des Datensatzes sind Teil der Aufgabe: Ihr Evaluierungsskript muss jeden Datensatz mit dieser Struktur automatisch einlesen können.

## Datensatz herunterladen

1. `tsr_train.zip` aus dem Moodle-Kurs herunterladen (im Ordner *Downloads* lassen oder neben `download.py` legen).
2. Entpacken:

```bash
python download.py                              # findet tsr_train.zip und entpackt nach dataset/train/
python download.py --zip pfad/zu/tsr_train.zip  # alternativ mit explizitem Pfad
```

Bei der Live-Demo wird `tsr_heldout.zip` ausgegeben und genauso entpackt:

```bash
python download.py --split heldout
```

Das Skript braucht nur die Python-Standardbibliothek.

## Struktur

```
download.py                Entpackt die Zip-Dateien aus Moodle nach dataset/
dataset/
├── classes.csv            Klassenliste (43 Klassen)
├── train/
│   ├── images/            Trainingsbilder (.jpg / .png)
│   └── labels.csv         Ground Truth der Trainingsbilder
└── heldout/
    ├── images/            leer – wird erst bei der Live-Demo ausgegeben
    └── labels.csv         leer – wird erst bei der Live-Demo ausgegeben
```

Der Held-out-Datensatz hat **exakt dieselbe Struktur** wie `train/`. Ihr Skript muss daher den Pfad zu einem Split als Argument übernehmen, z. B.

```bash
python evaluate.py --split dataset/heldout
```

Eine eigene Aufteilung in Training und Validierung nehmen Sie selbst aus `train/` vor.

## Bilder

- Format: JPG oder PNG, RGB, 1360 × 800 Pixel
- Ein Bild kann **kein, ein oder mehrere** Verkehrszeichen enthalten.
- Jede Datei in `images/` gehört zum Datensatz. Bilder, die in `labels.csv` nicht vorkommen, enthalten kein Verkehrszeichen.

## labels.csv

Eine Zeile pro Verkehrszeichen, mit Kopfzeile:

```
filename,x1,y1,x2,y2,class_id
train_0001.png,774,411,815,446,11
train_0001.png,983,388,1024,432,40
train_0002.png,386,494,442,552,38
```

| Spalte | Bedeutung |
|---|---|
| `filename` | Dateiname in `images/` |
| `x1`, `y1` | linke obere Ecke der Bounding Box (Pixel) |
| `x2`, `y2` | rechte untere Ecke der Bounding Box (Pixel) |
| `class_id` | Klasse, siehe `classes.csv` |

Koordinaten: Ursprung links oben, x nach rechts, y nach unten, ganzzahlig. `x2` und `y2` gehören noch zur Box (inklusive).

## classes.csv

```
class_id,category,name_de,name_en
0,prohibitory,Zulässige Höchstgeschwindigkeit 20,Speed limit (20km/h)
...
```

`category` fasst die Klassen in vier Gruppen zusammen (`prohibitory`, `danger`, `mandatory`, `other`), wie im GTSDB-Benchmark üblich. Die Kategorien können zusätzlich ausgewertet werden, z. B. bei Verwechslungen innerhalb einer Gruppe.

Die Klassenverteilung ist unausgeglichen: Für einzelne Klassen gibt es nur sehr wenige Beispiele, manche kommen in `train/` eventuell gar nicht vor. Ihr System und Ihre Auswertung müssen damit umgehen können.

## Quelle

Bilder und Annotationen stammen aus dem German Traffic Sign Detection Benchmark (GTSDB), umbenannt und in PNG konvertiert:

> S. Houben, J. Stallkamp, J. Salmen, M. Schlipsing, C. Igel: *Detection of Traffic Signs in Real-World Images: The German Traffic Sign Detection Benchmark.* International Joint Conference on Neural Networks (IJCNN), 2013.

Die Verwendung des Original-Datensatzes oder anderer Teile des GTSDB ist im Projekt **nicht zulässig**.
