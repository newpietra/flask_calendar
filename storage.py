from typing import List

import model

class StorageException(Exception):
    pass


class LocalStorage:
    def __init__(self):
        self._id_counter = 0
        self._storage = {}


    def create(self, calendar: model.Calendar) -> str:
        self._id_counter += 1
        calendar.id = str(self._id_counter)
        self._storage[calendar.id] = calendar
        return calendar.id

    def list(self) -> List[model.Calendar]:
        return list(self._storage.values)


    def read(self, _id: str) -> model.Calendar:
        if _id not in self._storage:
            raise StorageException(f"{id} not found in storage")
        return self._storage[_id]


    def update(self, _id: str, calendar: model.Calendar):
        if _id not in self._storage:
            raise StorageException(f"{id} not found in storage")
        calendar.id = _id
        self._storage[calendar.id] = calendar


    def delete(self, _id: str):
        if _id not in self._storage:
           raise StorageException(f"{id} not found in storage")
        del self._storage[_id]