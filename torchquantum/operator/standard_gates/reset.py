from ..op_types import Operator, AnyWires
from abc import ABCMeta
import torchquantum.functional as tqf


class Reset(Operator, metaclass=ABCMeta):
    """Class for Reset gate."""

    num_params = 0
    num_wires = AnyWires
    op_name = "reset"
    func = staticmethod(tqf.reset)

    @classmethod
    def _matrix(cls, params):
        return None
