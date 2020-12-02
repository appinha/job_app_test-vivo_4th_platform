import unittest
import requests
import json
from api.app import app

class TestAPI(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.response = self.app.get('/')

	def post(self):
		url = 'http://127.0.0.1:5000/results/post'
		with open('corrida.log', 'rb') as f:
			response = requests.post(url, files={\
				'file': ('corrida.log', f, 'text/csv', {'Expires': '0'})})
		return response

	def test_post_status_code(self):
		response = self.post()
		self.assertEqual(response.status_code, 200)

	def test_post_content_type(self):
		response = self.post()
		self.assertEqual(response.headers['Content-Type'], 'application/json')

	def test_content_type(self):
		self.assertIn('html', self.response.content_type)
