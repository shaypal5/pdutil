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

    Example
    -------
    >>> import pandas as pd; import pdutil;
    >>> data = [[23, "Jen"], [42, "Ray"], [15, "Fin"]]
    >>> df = pd.DataFrame(data, columns=['age', 'name'])
    >>> for subdf in pdutil.iter.sub_dfs_by_size(df, 2): print(subdf)
       age name
    0   23  Jen
    1   42  Ray
       age name
    2   15  Fin
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

    Example
    -------
    >>> import pandas as pd; import pdutil;
    >>> data = [[23, "Jen"], [42, "Ray"], [15, "Fin"]]
    >>> df = pd.DataFrame(data, columns=['age', 'name'])
    >>> for subdf in pdutil.iter.sub_dfs_by_num(df, 2): print(subdf)
       age name
    0   23  Jen
    1   42  Ray
       age name
    2   15  Fin
    """
    size = len(df) / float(num)
    for i in range(num):
        yield df.iloc[int(round(size * i)): int(round(size * (i + 1)))]
