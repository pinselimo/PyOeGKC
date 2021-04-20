from pathlib import Path
from os import path

PACKAGEDIR = Path(__file__).parent.absolute()
DATADIR = path.join(PACKAGEDIR, 'data')
SEPARATOR = ','

def load_municipality_merges():
    merges_2013 = path.join(DATADIR, "merges_municipalities_2013.csv")
    merges_2015 = path.join(DATADIR, "merges_municipalities_2015.csv")
    changes_2017 = path.join(DATADIR, "changes_municipalities_2017.csv")
    merges_2018 = path.join(DATADIR, "merges_municipalities_2018.csv")
    merges_2019 = path.join(DATADIR, "merges_municipalities_2019.csv")
    changes_2020 = path.join(DATADIR, "changes_municipalities_2020.csv")
    return {
            **_load_merges_from(merges_2013)
          , **_load_merges_from(merges_2015)
          , **_load_merges_from(changes_2017)
          , **_load_merges_from(merges_2018)
          , **_load_merges_from(merges_2019)
          , **_load_merges_from(changes_2020)
          }

def load_municipality_splits():
    splits_2015 = path.join(DATADIR, "splits_municipalities_2015.csv")
    splits_2020 = path.join(DATADIR, "splits_municipalities_2020.csv")
    return _load_splits_from(splits_2015) + _load_splits_from(splits_2020)

def load_district_merges():
    merges_2012 = path.join(DATADIR, "merges_districts_2012.csv")
    merges_2013 = path.join(DATADIR, "merges_districts_2013.csv")
    return {**_load_merges_from(merges_2012), **_load_merges_from(merges_2013)}

def _load_merges_from(filename):
    with open(filename, 'r') as f:
        header = f.readline()
        d = dict()
        for line in f.readlines():
            pre,post = line.split(SEPARATOR)
            d[int(pre)] = int(post)
        return d

def _load_splits_from(filename):
    with open(filename, 'r') as f:
        header = f.readline()
        return [
            tuple(map(int,line.split(SEPARATOR)))
            for line in f.readlines()
            ]
