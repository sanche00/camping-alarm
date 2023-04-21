from dataclasses import dataclass, fields
from datetime import date

@dataclass
class HopeReservation:
    site: str
    name: str
    region: str = None
    reservationDate: date = None
    area: str = None