from .transform import x_y_by_col_lbl

for name in ['transform', 'name']:
    try:
        globals().pop(name)
    except KeyError:
        pass
