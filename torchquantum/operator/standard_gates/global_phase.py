from ..op_types import Operation
from abc import ABCMeta
import torchquantum.functional as tqf


class GlobalPhase(Operation, metaclass=ABCMeta):
    """Class for Global Phase gate."""

    num_params = 1
    num_wires = 0
    op_name = "globalphase"
    func = staticmethod(tqf.globalphase)

    @classmethod
    def _matrix(cls, params):
        return tqf.globalphase_matrix(params)
