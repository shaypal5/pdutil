"""Serialization formats for pandas.DataFrame objects."""

import pandas as pd


class SerializationFormat(object):
    def __init__(self, ext, serialize, deserialize):
        self.ext = ext
        self.serialize = serialize
        self.deserialize = deserialize

    def __repr__(self):
        return "<pdutil.serial.SerializationFormat.{}>".format(self.ext)

    __NAME_TO_OBJ__ = {}

    @classmethod
    def by_name(cls, name):
        """Returns a SerializationFormat object by the format name.

        Parameters
        ----------
        name : str
            The name of the serialization format. E.g. 'csv' or 'feather'.

        Returns
        -------
        SerializationFormat
            An object representing the given serialization format.

        Example
        -------
        >>> SerializationFormat.by_name('csv')
        <pdutil.serial.SerializationFormat.csv>
        """
        return cls.__NAME_TO_OBJ__[name]

    @classmethod
    def __save_by_name__(cls, name, obj):
        cls.__NAME_TO_OBJ__[name] = obj


SerializationFormat.csv = SerializationFormat(
    ext="csv", serialize=pd.DataFrame.to_csv, deserialize=pd.read_csv
)
SerializationFormat.__save_by_name__("csv", SerializationFormat.csv)


SerializationFormat.json = SerializationFormat(
    ext="json", serialize=pd.DataFrame.to_json, deserialize=pd.read_json
)
SerializationFormat.__save_by_name__("json", SerializationFormat.json)


try:
    SerializationFormat.feather = SerializationFormat(
        ext="feather",
        serialize=pd.DataFrame.to_feather,
        deserialize=pd.read_feather,
    )
    SerializationFormat.__save_by_name__(
        "feather", SerializationFormat.feather
    )
except AttributeError:
    pass  # pandas under 0.20 - feather is not a valid serialization format
