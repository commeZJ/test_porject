import unittest
import requests
import json
import time

class SmileTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.ip ='http://localhost:3000'

    def test_get_all_tasks(self):
        url = self.ip + "/api/tasks"
        response = requests.request("GET",url)

        self.result= response.json()
        self.assertNotEqual(self.result,[])
        #self.assertEqual(self.result['status'],200)
        self.assertEqual(len(self.result),3)

    def login(self,username, password):
        url = "http://localhost:3000/login"
        res= requests.request("POST", url, data={'username': username, 'password': password}).json()
        #print(res)
        return res['token']
'''
    def register(self,username,password,password_confirmation):
        url="http://localhost:3000/register"
        response=requests.request("POST",url,
                                 data={'username':username,
                                 'password':password,
                                 'password_confirmation':password_confirmation})
        self.result=response.json()
'''

if __name__=='__main__':
    unittest.main()