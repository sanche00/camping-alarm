from dataclasses import dataclass, fields
from .hope_reservation import HopeReservation
from .event.exchange_reservation import Reservation
from datetime import date


def isHopeReservation(hope: HopeReservation, reservation: Reservation):
    if hope.reservationDate != reservation.reservationDate:
        return False

    if hope.site == reservation.site:
        if hope.area == reservation.area:
            return True
        if not hope.area:
            return True
    return False


@dataclass(frozen=True, kw_only=False)
class Host:
    name: str
    key: str
    status: str
    hopeReservation = {}

    def addReservation(self, reservation: HopeReservation):
        self.hopeReservation.setdefault(
            reservation.site, []).append(reservation)

    def getHopeReservation(self, reservation: Reservation):
        if not self.hopeReservation.get(reservation.site):
            return []
        hopeReservations: list[HopeReservation] = self.hopeReservation[reservation.site]
        return [hope for hope in hopeReservations if isHopeReservation(hope, reservation)]

    def __len__(self):
        return len(self.hopeReservation)
