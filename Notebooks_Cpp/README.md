# MVSR – C++ Notebooks mit MyBinder

Dieser Bereich des Repositories enthält die **C++-Notebooks zur Vorbereitung der MVSR-Einheiten**.  
Die Notebooks können über **MyBinder direkt im Browser** ausgeführt und bearbeitet werden. Eine lokale Installation von C++ oder OpenCV ist dafür nicht erforderlich.

## Verwendete Umgebung

- C++17 über `xeus-cling`
- OpenCV 4.6
- JupyterLab
- Binder / repo2docker

## Repository-Struktur

Die Binder-Konfiguration liegt im Root des GitHub-Repositories und wird von allen C++-Notebooks gemeinsam verwendet.

Hier ein Überblick über die Struktur:

```text
REPOSITORY/
├── binder/
│   ├── environment.yml
│   └── apt.txt
│
├── Notebooks_Cpp/
│   ├── README.md
│   ├── MVSR_01_Grundlagen_CPP.ipynb
│   ├── MVSR_02_Bildverarbeitung_CPP.ipynb
│   └── ...
│
└── test_images/
    └── ...
```

## MyBinder starten

Auf [mybinder.org](https://mybinder.org) wird das **gesamte GitHub-Repository** gestartet.

Unter **GitHub repository name or URL** wird die URL des Repositories eingetragen, zum Beispiel:

```text
https://github.com/DEIN_USERNAME/DEIN_REPOSITORY
```

Unter **Git ref** wird

```text
main
```

eingetragen.

Anschließend **Launch** auswählen. Beim ersten Aufruf baut Binder die Umgebung; das kann einige Minuten dauern.

Nach dem Start kann im JupyterLab-Dateibrowser der Ordner mit den C++-Notebooks geöffnet und das gewünschte Notebook ausgewählt werden.

## Hinweise für Studierende

- Die Notebooks werden vollständig im Browser ausgeführt.
- Der C++-Code kann direkt in den Notebook-Zellen bearbeitet werden.
- Codezellen werden mit **Shift + Enter** oder über den Play-Button ausgeführt.
- Die Zellen sollten grundsätzlich von oben nach unten ausgeführt werden.
- C++ wird mit `xeus-cling` inkrementell ausgeführt. Bereits deklarierte Variablen können daher beim wiederholten Ausführen einzelner Zellen zu Fehlermeldungen führen.
- Falls notwendig, kann der Kernel neu gestartet und das Notebook erneut von oben nach unten ausgeführt werden.
- Änderungen innerhalb einer Binder-Session werden **nicht dauerhaft im GitHub-Repository gespeichert**.
- Falls Ergebnisse oder Änderungen behalten werden sollen, muss das bearbeitete Notebook vor dem Beenden der Session gespeichert bzw. heruntergeladen werden.
- Beim ersten Start kann das Erzeugen der Binder-Umgebung einige Minuten dauern.

## Softwareversion prüfen

Die Setup-Zelle der Notebooks gibt die verwendete OpenCV-Version aus:

```cpp
std::cout << "OpenCV-Version: " << CV_VERSION << std::endl;
```

Für die C++-Notebooks in MyBinder wird **OpenCV 4.6** verwendet.

## Technischer Hinweis

Die gemeinsame Binder-Umgebung wird über den Ordner `binder/` im Root des Repositories erzeugt.

`binder/environment.yml` installiert den C++-Kernel `xeus-cling`.  
OpenCV wird in der Binder-Umgebung über das Ubuntu-Paket `libopencv-dev` aus `binder/apt.txt` bereitgestellt.

Die Notebooks verwenden C++17. Binder-spezifische Einstellungen, beispielsweise das Laden der OpenCV-Bibliotheken über `#pragma cling`, sind direkt in den jeweiligen Notebooks dokumentiert.

Neue Notebooks können im C++-Ordner ergänzt werden und verwenden automatisch dieselbe Binder-Umgebung.