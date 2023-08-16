
from pydantic import BaseModel

class ErrorCodes( BaseModel ):
    VALIDATION_ERROR: str = 'Validation error'
    HTTP_ERROR: str = 'http error'
    DATABASE_ERROR: str = 'has ocurred a databse error'
    INVALID_PARAMETER: str = 'Invalid parameter'