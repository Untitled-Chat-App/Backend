""" (module) chatapp
This contains the Chat_API class (FastAPI subclass)
"""

__all__ = ["Chat_API"]

from fastapi import FastAPI
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler

DESCRIPTION = """
### API/Backend for chat app
"""


class Chat_API(FastAPI):
    """
    The custom subclass of FastAPI called Chat_API

    [API docs](https://github.com/Untitled-Chat-App/Backend/blob/main/docs/docs.md)
    """

    def __init__(self) -> None:
        super().__init__()
        # Docs config
        self.title = "Untitled-Chat API"
        self.version = "0.0.1"
        self.description = DESCRIPTION
        self.license_info = {
            "name": "MIT",
            "url": "https://opensource.org/licenses/MIT",
        }

        # Rate limiting
        self.state.limiter = Limiter(
            key_func=get_remote_address, default_limits=["30/minute"]
        )
        self.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
        self.add_middleware(SlowAPIMiddleware)
