# Konvertierer für Österreichische Gemeindekennzahlen

Jede Gemeinde in Österreich erhält eine Gemeindekennzahl. Leider ändern sich diese Zahlen immer wieder aus verschiedenen Gründen.

Die Daten zu diesen Veränderungen sind über verschiedene Excel-Sheets und PDFs verteilt. Mit deser Bibliothek werden sie in einem nachvollziehbaren Format zur Verfügung gestellt. Des weiteren finden sich eine Converter-Klasse und Strategien für den Umgang mit unklaren abfolgen.

Es gibt drei Typen von Datensets:

- Zusammenlegungen (*merges*)
- Änderungen (*changes*)
- Teilungen (*splits*)

## Zusammenlegungen und Änderungen

Zusammenlegungen und Änderungen beinhalten jeweils die Kennzahlen *pre* und *post* der Änderung. Ihre Unterscheidung findet sich nur im Grund der Änderung und dient somit lediglich der Organisation der Daten.

## Gemeindeteilungen

Einige Gemeinden wurden aufgeteilt und die Teile unterschiedlich eingemeindet. Die Teilungen beinhalten daher neben *pre* und *post* auch *houses* und *citizens* welche eingemeindet wurden.

## License

This library is licensed under the ```MIT``` License. Refer to the accompanying LICENSE file for details.

## Original data

The original data is scattered throghout Statistik Austria's site on [municipalities](http://statistik.at/web_de/klassifikationen/regionale_gliederungen/gemeinden/index.html) and [counties](http://statistik.at/web_de/klassifikationen/regionale_gliederungen/politische_bezirke/index.html).

