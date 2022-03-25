import sqlite3
import unittest
class checkdata(unittest.TestCase):
    def setUp(self):
        self.Name = "John"
        self.Code = "1102"
        self.connection = sqlite3.connect("employee.db")
    def tearDown(self):
        self.Name=" "
        self.Code=" "
        self.connection.close()
    def test_verify_name(self):
        result = self.connection.execute("select name from details where empcode="+self.Code)
        for i in result:
            fetcheddata= (i[0])
        self.assertEqual(self.Name,fetcheddata)
if __name__=="__main__":
    unittest.main()