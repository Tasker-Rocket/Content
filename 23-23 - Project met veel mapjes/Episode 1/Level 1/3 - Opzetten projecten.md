# Level 1-3  Opzetten projecten
## Taak: Projecten opzetten
Met deze opdracht zet je de andere noodzakelijke projecten op. Elk project heeft zijn eigen verantwoordelijkheid. Bij de scheiding van verantwoordelijkheden hanteer je in dit project het MVC pattern.

Het 'console project' is de 'view' in het `MVC-patroon`. Er moeten nog twee projecten aangemaakt worden in de solution.

Eerst voeg je de twee projecten toe en vervolgens geef je het 'console project' een referentie naar de toegevoegde
projecten om van de toegevoegde projecten gebruik te kunnen maken.

### Aanpak
Standaard heeft Visual Studio rechts een 'Solution Explorer'. Dit is een weergave van alle projecten in de solution en alle onderliggende bestanden binnen de projecten.
In de solution voeg je voor de controller en het model een project toe. Deze projecten zijn van het type Class Library. Vervolgens geef je de view project, het console project, referenties naar de andere projecten.

1. Klik op Solution in de Solution explorer
2. Ga via het contextmenu (klik met rechter muisknop) naar Add > New Project...
3. Zoek op Class Library
4. Selecteer Class Library (.NET Core). Doorloop de stappen waarbij je het project de naam 'Model' geeft.
5. Repeteer voorgaande stappen, met dit verschil: geef als naam 'Controller'.
6. Geef het consoleproject referenties naar de toegevoegde projecten. Klik op het consoleproject.
7. Ga naar de Reference Manager: context menu > Add > Reference. Selecteer de toegevoegde projecten en klik op 'OK'.
