import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_chat_success(self):
        response = self.app.post('/api/chat', json={"message": "hello"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.get_json())

    def test_chat_no_message(self):
        response = self.app.post('/api/chat', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_health_check(self):
        response = self.app.get('/api/health')
        self.assertIn(response.status_code, [200, 207])
        self.assertIn("status", response.get_json())

if __name__ == '__main__':
    unittest.main()
