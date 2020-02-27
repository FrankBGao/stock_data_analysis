"""
 "time": "2015-01-08",
  "start": 5.95,
  "max": 6.06,
  "min": 5.91,
  "end": 5.97,
  "volumn": 676.75, //volume
  "money": 4056.12
"""
import pandas as pd
import copy


def visual(data):
    # data = pd.DataFrame()
    data = copy.deepcopy(data)
    data = data.rename(axis="columns",
                       mapper={"date": "time", "open": "start", "close": "end", "high": "max", "low": "min",
                               "volume": "volumn"})

    data = data[["time", "start", "end", "max", "min", "volumn", "point","ptype"]]
    data["money"] = data["start"] * data["volumn"]

    return data.to_json(orient="records")
