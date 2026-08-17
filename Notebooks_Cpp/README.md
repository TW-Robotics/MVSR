# MVSR – C++ Notebook mit Binder

Dieses Repository stellt das C++-Notebook zur Vorbereitung der ersten MVSR-Einheit
direkt im Browser bereit. Lokal müssen die Studierenden dafür nichts installieren.

Verwendete Umgebung:

- C++17 über `xeus-cpp`
- OpenCV 4.12
- JupyterLab
- Binder / repo2docker

## Repository-Struktur

```text
MVSR_CPP_Binder/
├── MVSR_Jupyter_01_OpenCV_Basics_CPP.ipynb
├── README.md
└── binder/
    └── environment.yml
```

## 1. Repository auf GitHub anlegen

1. Auf GitHub ein neues **öffentliches** Repository erstellen, z. B. `mvsr-cpp-binder`.
2. Den gesamten Inhalt dieses Ordners in das Repository hochladen.
3. Darauf achten, dass `binder/environment.yml` als Unterordner erhalten bleibt.
4. Als Branch kann z. B. `main` verwendet werden.

## 2. Binder starten

Auf `https://mybinder.org` die URL des GitHub-Repositories eintragen.

Beispiel:

```text
https://github.com/DEIN_USERNAME/mvsr-cpp-binder
```

Als Branch:

```text
main
```

Anschließend **launch** auswählen. Beim ersten Aufruf baut Binder die Umgebung;
das kann einige Minuten dauern.

## 3. Direkten Link zum Notebook erstellen

Für Moodle oder andere Lehrplattformen kann direkt auf das Notebook verlinkt werden:

```text
https://mybinder.org/v2/gh/DEIN_USERNAME/mvsr-cpp-binder/main?urlpath=lab/tree/MVSR_Jupyter_01_OpenCV_Basics_CPP.ipynb
```

Dabei müssen nur

```text
DEIN_USERNAME
```

und gegebenenfalls der Repository-Name angepasst werden.

## 4. Optional: Binder-Button im README

```markdown
[![Binder](https://mybinder.org/badge_logo.svg)](
https://mybinder.org/v2/gh/DEIN_USERNAME/mvsr-cpp-binder/main?urlpath=lab/tree/MVSR_Jupyter_01_OpenCV_Basics_CPP.ipynb
)
```

## Hinweise für Studierende

- Das Notebook wird vollständig im Browser ausgeführt.
- Die Codezellen werden mit **Shift + Enter** oder über den Play-Button ausgeführt.
- Die Zellen sollten von oben nach unten ausgeführt werden.
- Änderungen innerhalb einer Binder-Session werden nicht dauerhaft im GitHub-Repository gespeichert.
- Falls Ergebnisse oder Änderungen behalten werden sollen, sollte das bearbeitete Notebook vor dem Beenden der Session lokal gespeichert werden.
- Beim ersten Start kann das Erzeugen der Binder-Umgebung einige Minuten dauern.

## Softwareversion prüfen

Die erste Setup-Zelle des Notebooks gibt die verwendete OpenCV-Version aus:

```cpp
std::cout << "OpenCV-Version: " << CV_VERSION << std::endl;
```

Für die Lehrveranstaltung ist OpenCV **4.12.x** vorgesehen.

## Technischer Hinweis

Die Binder-Umgebung wird über `binder/environment.yml` erzeugt. Die darin
angegebenen Pakete werden aus `conda-forge` installiert. `xeus-cpp` stellt
den C++-Kernel für Jupyter bereit. Das Notebook ist für den C++17-Kernel
`xcpp17` vorbereitet.
