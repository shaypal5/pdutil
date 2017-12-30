"""Iteration over pandas DataFrames."""


def sub_dfs_by_size(df, size):
    """Get a generator yielding consecutive sub-dataframes of the given size.

    Arguments
    ---------
    df : pandas.DataFrame
        The dataframe for which to get sub-dataframes.
    size : int
        The size of each sub-dataframe.

    Returns
    -------
    generator
        A generator yielding consecutive sub-dataframe of the given size.
    """
    for i in range(0, len(df), size):
        yield (df.iloc[i:i + size])


def sub_dfs_by_num(df, num):
    """Get a generator yielding num consecutive sub-dataframes of the given df.

    Arguments
    ---------
    df : pandas.DataFrame
        The dataframe for which to get sub-dataframes.
    num : int
        The number of sub-dataframe to divide the given dataframe into.

    Returns
    -------
    generator
        A generator yielding n consecutive sub-dataframes of the given df.
    """
    size = len(df) / float(num)
    for i in range(num):
        yield df.iloc[int(round(size * i)): int(round(size * (i + 1)))]
