"""Dataframe display-related functions."""

import sys

import numpy as np
import pandas as pd


def df_string(df, percentage_columns=(), format_map=None, **kwargs):
    """Return a nicely formatted string for the given dataframe.

    Arguments
    ---------
    df : pandas.DataFrame
        A dataframe object.
    percentage_columns : iterable
        A list of cloumn names to be displayed with a percentage sign.

    Returns
    -------
    str
        A nicely formatted string for the given dataframe.

    Example
    -------
    >>> import pandas as pd
    >>> df = pd.DataFrame([[8,'a'],[5,'b']],[1,2],['num', 'char'])
    >>> print(df_string(df))
       num char
    1    8    a
    2    5    b
    """
    formatters_map = {}
    for col, dtype in df.dtypes.iteritems():
        if col in percentage_columns:
            formatters_map[col] = "{:,.2f} %".format
        elif dtype == "float64":
            formatters_map[col] = "{:,.2f}".format
    if format_map:
        for key in format_map:
            formatters_map[key] = format_map[key]
    return df.to_string(formatters=formatters_map, **kwargs)


def big_dataframe_setup():  # pragma: no cover
    """Sets pandas to display really big data frames."""
    pd.set_option("display.max_colwidth", sys.maxsize)
    pd.set_option("max_colwidth", sys.maxsize)
    # height has been deprecated.
    # pd.set_option('display.height', sys.maxsize)
    pd.set_option("display.max_rows", sys.maxsize)
    pd.set_option("display.max_columns", sys.maxsize)
    pd.set_option("display.width", sys.maxsize)
    pd.set_option("display.colheader_justify", "center")
    pd.set_option("display.column_space", sys.maxsize)
    pd.set_option("display.max_seq_items", sys.maxsize)
    pd.set_option("display.expand_frame_repr", True)


_PRECENT_WORDS = ["rate", "ratio", "percentage"]


def _default_is_precentage_col(col_name):  # pragma: no cover
    return any([word in col_name.lower() for word in _PRECENT_WORDS])


def _formatters_dict(input_df, percentage_columns=None):  # pragma: no cover
    formatters = {}
    if percentage_columns is None:
        is_precentage_col = _default_is_precentage_col
    else:
        is_precentage_col = lambda col: col in percentage_columns  # noqa: E731
    for col in input_df.columns:
        if is_precentage_col(col):
            formatters[col] = "{:,.2f} %".format
        elif input_df.dtypes[col] in [float, np.float64]:
            formatters[col] = "{:,.2f}".format
    return formatters


def df_to_html(df, percentage_columns=None):  # pragma: no cover
    """Return a nicely formatted HTML code string for the given dataframe.

    Arguments
    ---------
    df : pandas.DataFrame
        A dataframe object.
    percentage_columns : iterable
        A list of cloumn names to be displayed with a percentage sign.

    Returns
    -------
    str
        A nicely formatted string for the given dataframe.
    """
    big_dataframe_setup()
    try:
        res = "<br><h2> {} </h2>".format(df.name)
    except AttributeError:
        res = ""
    df.style.set_properties(**{"text-align": "center"})
    res += df.to_html(
        formatters=_formatters_dict(
            input_df=df, percentage_columns=percentage_columns
        )
    )
    res += "<br>"
    return res
