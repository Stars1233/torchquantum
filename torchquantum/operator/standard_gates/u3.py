from ..op_types import Operation
from abc import ABCMeta
import torchquantum.functional as tqf


class U3(Operation, metaclass=ABCMeta):
    """Class for U3 gate."""

    num_params = 3
    num_wires = 1
    op_name = "u3"
    func = staticmethod(tqf.u3)

    @classmethod
    def _matrix(cls, params):
        return tqf.u3_matrix(params)


U = U3


class CU3(Operation, metaclass=ABCMeta):
    """Class for Controlled U3 gate."""

    num_params = 3
    num_wires = 2
    op_name = "cu3"
    func = staticmethod(tqf.cu3)

    @classmethod
    def _matrix(cls, params):
        return tqf.cu3_matrix(params)


class CU(Operation, metaclass=ABCMeta):
    """Class for Controlled U gate (4-parameter two-qubit gate)."""

    num_params = 4
    num_wires = 2
    op_name = "cu"
    func = staticmethod(tqf.cu)

    @classmethod
    def _matrix(cls, params):
        return tqf.cu_matrix(params)
