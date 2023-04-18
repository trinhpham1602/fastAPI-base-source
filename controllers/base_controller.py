from fastapi import APIRouter
from services.base_service import BaseService
from abc import ABC, abstractmethod


class BaseController(ABC):
    def __init__(self, router: APIRouter, base_service: BaseService):
        self.router = router
        self.service = base_service
        self.configure_routes()

    @abstractmethod
    def configure_routes(self):
        pass
