from ..op_types import DiagonalOperation
from abc import ABCMeta
import torchquantum.functional as tqf


class PhaseShift(DiagonalOperation, metaclass=ABCMeta):
    """Class for PhaseShift Gate."""

    num_params = 1
    num_wires = 1
    op_name = "phaseshift"
    func = staticmethod(tqf.phaseshift)

    @classmethod
    def _matrix(cls, params):
        return tqf.phaseshift_matrix(params)
