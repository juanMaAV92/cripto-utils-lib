from enum import Enum
from pydantic import BaseModel

class OrderTypeEnum(str, Enum):
    LIMIT = "limit"
    MARKET = "market"

class OrderType(BaseModel):
    order_type: OrderTypeEnum
