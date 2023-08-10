from enum import Enum
from pydantic import BaseModel

class LogLevelEnum(str, Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class LogLevel(BaseModel):
    log_level: LogLevelEnum
