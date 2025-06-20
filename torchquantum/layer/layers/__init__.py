from .swap_layer import SWAPSWAPLayer0
from .ry_layer import (
    RYRYCXLayer0,
    RYRYRYCXCXCXLayer0,
    RYRYRYLayer0,
    RYRYRYSWAPSWAPLayer0,
)
from .layers import (
    CXRZSXLayer0,
    RZZLayer0,
    BarrenLayer0,
    FarhiLayer0,
    MaxwellLayer0,
    RXYZCXLayer0,
)

# layer (children of LayerTemplate0) to add to the layer_name_dict
_all_layers = [
    SWAPSWAPLayer0,
    RYRYCXLayer0,
    RYRYRYCXCXCXLayer0,
    RYRYRYLayer0,
    RYRYRYSWAPSWAPLayer0,
    CXRZSXLayer0,
    RZZLayer0,
    BarrenLayer0,
    FarhiLayer0,
    MaxwellLayer0,
    RXYZCXLayer0,
]

layer_name_dict = {}

for _lyr in _all_layers:
    # check the layer has a non-empty name
    assert _lyr.name is not None, f"Layer name not defined for {layer}"
    layer_name_dict[_lyr.name] = _lyr
