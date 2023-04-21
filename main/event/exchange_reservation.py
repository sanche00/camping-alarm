from dataclasses import dataclass
from datetime import date


@dataclass
class Reservation:
    """예약 변경 정보"""
    site: str= None
    name: str= None
    region: str= None
    reservationDate: date = None
    area: str = None
    total: int = None
    remain: int= None
    
        