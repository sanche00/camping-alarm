from dataclasses import dataclass, fields
from .hope_reservation import HopeReservation
from .event.exchange_reservation import Reservation
from datetime import date

def isHopeReservation(hope:HopeReservation, reservation:Reservation):
    if hope.reservationDate != reservation.reservationDate:
        return False
    
    if hope.site == reservation.site :
        if hope.area == reservation.area : 
            return True
        if not hope.area: 
            return True
    return False

@dataclass(frozen=True, kw_only=False)
class Host:
    name:str
    key:str
    status:str
    hopeReservation = {}
    
    def addReservation(self, reservation:HopeReservation): 
        self.hopeReservation.setdefault(reservation.site, []).append(reservation)
        # addHopeReservations = []
        # if self.hopeReservation.get(str(reservation.site)):
        #     addHopeReservations = self.hopeReservation.get(reservation.site)
        # addHopeReservations.append(reservation)
        # self.hopeReservation[reservation.site] = addHopeReservations

    def getHopeReservation(self, reservation:Reservation):
        if not self.hopeReservation.get(reservation.site):
            return []
        hopeReservations:list[HopeReservation] = self.hopeReservation[reservation.site]
        return list(filter(lambda x: isHopeReservation(x, reservation), hopeReservations))
        
        
    def __len__(self):
        return len(self.hopeReservation);
