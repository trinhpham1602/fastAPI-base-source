from repository.base_repository import BaseRepository
from abc import ABC


class BaseService(ABC):
    def __init__(self, base_repo: BaseRepository):
        self.base_repo = base_repo
