"""
Base exceptions for the application.
"""
from typing import Optional, Dict, Any


class BaseAppException(Exception):
    """Base exception for all application exceptions"""
    
    def __init__(
        self,
        message: str = "An error occurred",
        code: str = "INTERNAL_ERROR",
        status_code: int = 500,
        details: Optional[Dict[str, Any]] = None
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = details or {}
        super().__init__(self.message)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert exception to dictionary for JSON response"""
        return {
            "error": {
                "code": self.code,
                "message": self.message,
                "details": self.details
            }
        }


class DatabaseException(BaseAppException):
    """Database-related exceptions"""
    
    def __init__(
        self,
        message: str = "Database error occurred",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="DATABASE_ERROR",
            status_code=500,
            details=details
        )


class ValidationException(BaseAppException):
    """Validation-related exceptions"""
    
    def __init__(
        self,
        message: str = "Validation failed",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="VALIDATION_ERROR",
            status_code=400,
            details=details
        )


class AuthenticationException(BaseAppException):
    """Authentication-related exceptions"""
    
    def __init__(
        self,
        message: str = "Authentication failed",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="AUTHENTICATION_ERROR",
            status_code=401,
            details=details
        )


class AuthorizationException(BaseAppException):
    """Authorization-related exceptions"""
    
    def __init__(
        self,
        message: str = "Authorization failed",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="AUTHORIZATION_ERROR",
            status_code=403,
            details=details
        )


class ResourceNotFoundException(BaseAppException):
    """Resource not found exceptions"""
    
    def __init__(
        self,
        message: str = "Resource not found",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="RESOURCE_NOT_FOUND",
            status_code=404,
            details=details
        )


class BusinessLogicException(BaseAppException):
    """Business logic-related exceptions"""
    
    def __init__(
        self,
        message: str = "Business logic error",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="BUSINESS_LOGIC_ERROR",
            status_code=400,
            details=details
        )


class ExternalServiceException(BaseAppException):
    """External service-related exceptions"""
    
    def __init__(
        self,
        message: str = "External service error",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="EXTERNAL_SERVICE_ERROR",
            status_code=502,
            details=details
        )


class RateLimitException(BaseAppException):
    """Rate limiting exceptions"""
    
    def __init__(
        self,
        message: str = "Rate limit exceeded",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="RATE_LIMIT_EXCEEDED",
            status_code=429,
            details=details
        )


class ConfigurationException(BaseAppException):
    """Configuration-related exceptions"""
    
    def __init__(
        self,
        message: str = "Configuration error",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            message=message,
            code="CONFIGURATION_ERROR",
            status_code=500,
            details=details
        )


__all__ = [
    "BaseAppException",
    "DatabaseException",
    "ValidationException",
    "AuthenticationException",
    "AuthorizationException",
    "ResourceNotFoundException",
    "BusinessLogicException",
    "ExternalServiceException",
    "RateLimitException",
    "ConfigurationException"
]