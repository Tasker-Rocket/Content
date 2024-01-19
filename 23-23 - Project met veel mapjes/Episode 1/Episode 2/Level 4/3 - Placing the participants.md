# Placing the participants
## Taak
Voordat de race kan beginnen moeten alle deelnemers een plek krijgen op de baan. Je gaat in deze taak de klasse Race uitbreiden zodat alle deelnemers een logische startpositie krijgen toegewezen.

Het is raadzaam om eerst na te denken voordat je gaat programmeren. De taak klinkt eenvoudig: geef alle deelnemers een logische startpositie. Toch zal je met meerdere factoren rekening moeten houden. De belangrijkste regel is dat er maar 2 deelnemers op een sectie geplaatst mogen worden. Daarnaast moeten alle deelnemers een startpositie krijgen passend bij de type race, dus niet willekeurig geplaatst op de baan.

Wanneer je een strategie hebt bedacht en deze aan het programmeren bent gebruik de debugger regelmatig. De trial and error methode gaat je veel tijd, energie en veel frustratie kosten! Nogmaals, gebruik de debugger!

## Aanpak
1. Maak In de klasse Race een methode aan die als doel heeft alle deelnemers op de baan een start positie te geven.
2. Implementeer de methode. Gebruik de properties Track en Participants als input. Sla de meegegeven start posities aan de deelnemers op in de variable _positions, gebruik hierbij de methode GetSectionData als hulpmiddel. Tip: gebruik de property SectionType van Section om logische start posities te selecteren.
3. Breid de constructor van de klasse uit en roep de methode aan.
