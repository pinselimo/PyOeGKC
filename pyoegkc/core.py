from enum import Enum

from .data import load_district_merges,load_municipality_merges,load_municipality_splits

class SplitStrategy(Enum):
    """Strategy on how to proceed with splits.

    Strategies
    ----------
    BIGGER_POPULOUS : Follow splits with more citizens involved.
    LOWER_POPULOUS : Opposite of BIGGER_POPULOUS.
    """

    BIGGER_POPULOUS = 1
    LOWER_POPULOUS = 2

class Converter:
    def __init__(self, strategy=SplitStrategy.BIGGER_POPULOUS):
        self._dicts = [load_district_merges(), load_municipality_merges()]

        splits = sorted(load_municipality_splits(), key=lambda x:x[3])

        if strategy == SplitStrategy.LOWER_POPULOUS:
            splits = reversed(splits)

        self._dicts.append(
                {pre:post for pre,post,_,_ in splits}
                )

    def convert(self, code):
        for d in self._dicts:
            if code in d:
                return self.convert(self.d[code])
        else:
            return code

    def __getitem__(self, code):
        return self.convert(code)
