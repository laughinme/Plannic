from enum import Enum

class WeekDay(str, Enum):
    """Days of week number representation"""
    
    monday = '1'
    tuesday = '2'
    wednesday = '3'
    thursday = '4'
    friday = '5'
    saturday = '6'
