# Converter for Austrian municipality codes

Every municipality in Austria receives a code number. Unfortunately, these change every other year as politicians do their thing.

The data is only available in diffused PDFs and some excel sheets, making it hard to track these changes. This library contains the changes in a trackable format. It also defines its own converter and conversion strategies for disambiguation.

Three types of datasets are included:

- Merges
- Changes
- Splits

## Merges and changes

Merges and changes both contain code tuplets of *Pre* and *Post* change. The difference is, that merges result from merges of municipalities while changes have different reasons. It's really just for easier tracking.

## Split municipalities

Some municipalities were split and parts attributed to different newly established enclosures. Splits therefore contain the number of *houses* and *citizens* attributed to each new municipality. Hence, strategies on how to proceed with these exist in the ```Converter``` instance.

## License

This library is licensed under the ```MIT``` License. Refer to the accompanying LICENSE file for details.

## Original data

The original data is scattered throghout Statistik Austria's site on [municipalities](http://statistik.at/web_de/klassifikationen/regionale_gliederungen/gemeinden/index.html) and [counties](http://statistik.at/web_de/klassifikationen/regionale_gliederungen/politische_bezirke/index.html).

