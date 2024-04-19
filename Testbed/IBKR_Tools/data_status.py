from enum import Enum


class DataStatus(Enum):
    OK = "CONFIRMED OK: File was successfully written and contains data"
    NOT_EXIST = "FAILURE: File does not exist"
    EMPTY = "FAILURE: File was successfully written but is empty"
