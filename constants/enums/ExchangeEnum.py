from enum import Enum
from pydantic import BaseModel

class ExchangeEnum(str, Enum):
    BYBIT = "bybit"


class Exchange(BaseModel):
    exchange: ExchangeEnum
