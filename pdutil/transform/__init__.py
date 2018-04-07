from .transform import (  # noqa: F401
    x_y_by_col_lbl,
    x_y_by_col_lbl_inplace,
    or_by_masks,
    or_by_mask_conditions,
)

for name in ['transform', 'name']:
    try:
        globals().pop(name)
    except KeyError:
        pass
