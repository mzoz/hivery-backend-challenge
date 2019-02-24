import unittest
import json

from app import app


class APITestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        res = tester.get('/')
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res.data, b'{"error":"404 Not Found"}\n')

    def test_person(self):
        tester = app.test_client(self)
        res = tester.get('/hivery/api/v1.0/people/678')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['age'], 25)
        self.assertEqual(data['username'], 'Dale Graham')

    def test_friends(self):
        tester = app.test_client(self)
        res = tester.get('/hivery/api/v1.0/people/678/123')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        self.assertEqual(data['common_friends'], [1, 4])

    def test_company(self):
        tester = app.test_client(self)
        res = tester.get('/hivery/api/v1.0/company/DOGSPA')
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data.decode('utf-8'))
        employees = []
        for item in data:
            employees.append(item['index'])
        self.assertEqual(employees, [165, 324, 377, 991, 997])


if __name__ == '__main__':
    unittest.main()
