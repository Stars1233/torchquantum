from ..op_types import Operation
from abc import ABCMeta
import torchquantum.functional as tqf


class XXMINYY(Operation, metaclass=ABCMeta):
    """Class for XXMinusYY gate."""

    num_params = 2
    num_wires = 2
    op_name = "xxminyy"
    func = staticmethod(tqf.xxminyy_matrix)

    @classmethod
    def _matrix(cls, params):
        return tqf.xxminyy_matrix(params)
