from .transform import (
    x_y_by_col_lbl,
    or_by_masks,
    or_by_mask_conditions,
)

for name in ['transform', 'name']:
    try:
        globals().pop(name)
    except KeyError:
        pass
