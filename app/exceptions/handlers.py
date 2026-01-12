"""
Exception handlers for FastAPI application.
"""
import traceback
from typing import Union, Dict, Any
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import SQLAlchemyError
from pydantic import ValidationError

from app.core.logging import logger, structured_logger
from app.exceptions.base import (
    BaseAppException,
    AuthenticationException,
    AuthorizationException,
    ResourceNotFoundException,
    BusinessLogicException,
    ValidationException
)
from app.exceptions.http_exceptions import CustomHTTPException


async def http_exception_handler(request: Request, exc: CustomHTTPException) -> JSONResponse:
    """
    Handle custom HTTP exceptions.
    
    Args:
        request: HTTP request
        exc: HTTP exception
        
    Returns:
        JSONResponse: Error response
    """
    structured_logger.log_error(
        error_type="http_exception",
        message=exc.detail,
        user_id=getattr(request.state, 'user_id', None