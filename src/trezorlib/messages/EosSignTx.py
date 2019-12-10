# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .EosTxHeader import EosTxHeader

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class EosSignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 602

    def __init__(
        self,
        address_n: List[int] = None,
        chain_id: bytes = None,
        header: EosTxHeader = None,
        num_actions: int = None,
    ) -> None:
        self.address_n = address_n if address_n is not None else []
        self.chain_id = chain_id
        self.header = header
        self.num_actions = num_actions

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            2: ('chain_id', p.BytesType, 0),
            3: ('header', EosTxHeader, 0),
            4: ('num_actions', p.UVarintType, 0),
        }
