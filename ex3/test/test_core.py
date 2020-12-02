from api.app import app
import sys
import unittest
import requests
import json

class TestHomeView(unittest.TestCase):

	def setUp(self):
		app_test = app.test_client()
		self.response = app_test.get('/')

	def test_content_type(self):
		self.assertIn('html', self.response.content_type)
