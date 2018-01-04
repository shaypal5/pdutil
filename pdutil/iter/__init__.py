from .iter import (
    sub_dfs_by_size,
    sub_dfs_by_num,
)


for name in ['iter', 'name']:
    try:
        globals().pop(name)
    except KeyError:
        pass
