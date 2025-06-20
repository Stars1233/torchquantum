from ..op_types import DiagonalOperation
from abc import ABCMeta
import torchquantum.functional as tqf


class U1(DiagonalOperation, metaclass=ABCMeta):
    """Class for Controlled Rotation Y gate.  U1 is the same
    as phaseshift.
    """

    num_params = 1
    num_wires = 1
    op_name = "u1"
    func = staticmethod(tqf.u1)

    @classmethod
    def _matrix(cls, params):
        return tqf.u1_matrix(params)


class CU1(DiagonalOperation, metaclass=ABCMeta):
    """Class for controlled U1 gate."""

    num_params = 1
    num_wires = 2
    op_name = "cu1"
    func = staticmethod(tqf.cu1)

    @classmethod
    def _matrix(cls, params):
        return tqf.cu1_matrix(params)
