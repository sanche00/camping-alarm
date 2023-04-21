import unittest
from main.host import Host
from main.hope_reservation import HopeReservation
from datetime import date
# import main
from main.event.exchange_reservation import Reservation

class TestHostMethods(unittest.TestCase):

    host :Host
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.host = Host(name='test', key='key', status='사용중')
        


    def test_addtest(self):
        self.host.addReservation(HopeReservation(area=None, site='test',name='테스트', reservationDate=date(2023,3,3)))
        self.assertEqual(len(self.host), 1)
        self.host.addReservation(HopeReservation(area='test1', site='test',name='테스트', reservationDate=date(2023,3,4)))
        self.assertEqual(len(self.host), 1)

    def test_getHopeReservation(self):
        ret = self.host.getHopeReservation(Reservation(area='test1', site='test',name='테스트', reservationDate=date(2023,3,4)))
        self.assertTrue(bool(ret))
        ret = self.host.getHopeReservation(Reservation(area='test1', site='test',name='테스트', reservationDate=date(2023,3,5)))
        self.assertFalse(bool(ret))
        ret = self.host.getHopeReservation(Reservation(area='test1', site='test2',name='테스트', reservationDate=date(2023,3,4)))
        self.assertFalse(bool(ret))
        
# if __name__ == '__main__':
#     unittest.main()