from .display import (
    df_string,
    big_dataframe_setup,
    df_to_html,
)


for name in ['display', 'name']:
    try:
        globals().pop(name)
    except KeyError:
        pass
