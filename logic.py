from typing import List

import model
import db
import datetime

TITLE_LIMIT = 30
TEXT_LIMIT = 200
DATE_FORMAT = "%Y/ %m/ %d"


class LogicException(Exception):
    pass

class CalendarLogic():
    def __init__(self):
        self._calendar_db = db.CalendarDB()

    @staticmethod
    def _validate_calendar(calendar: model.Calendar):
         if calendar is None:
             raise LogicException("calendar is None")
         if calendar.title is None or len(calendar.title) > TITLE_LIMIT:
             raise LogicException(f"title length > MAX: {TITLE_LIMIT}")
         if calendar.text is None or len(calendar.text) > TEXT_LIMIT:
             raise LogicException(f"text length > MAX: {TEXT_LIMIT}")
         if calendar.date is not DATE_FORMAT:
             raise LogicException(f"text length > MAX: {DATE_FORMAT}")


    def create(self, calendar: model.Calendar) -> str:
        self._validate_calendar(calendar)
        try:
            return self._calendar_db.create(calendar)
        except Exception as ex:
            raise LogicException(f"failed CREATE operation with: {ex}")
    def list(self) -> List[model.Calendar]:
        try:
            return self._calendar_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")


    def read(self, _id: str) -> model.Calendar:
        try:
            return self._calendar_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")


    def update(self, _id: str, calendar: model.Calendar):
         try:
             return self._calendar_db.update(_id,calendar)
         except Exception as ex:
             raise LogicException(f"failed UPDATE operation with: {ex}")


    def delete(self, _id: str):
         try:
             return self._calendar_db.delete(_id)
         except Exception as ex:
             raise LogicException(f"failed DELETE operation with: {ex}")