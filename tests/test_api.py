from unittest import TestCase
from requests import Response
from fastapi.testclient import TestClient

from main import app


class TestApi(TestCase):
    """ This class encapsulates all test for the api functionalities"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def _run_std_response_assertions(self, response: Response, status: int) -> None:
        """ Asserts the response status code and response data """
        self.assertEqual(response.status_code, status)
        self.assertTrue(response.json())

    def test_root(self) -> None:
        response = self.client.get("/")

        self._run_std_response_assertions(response, 200)
        self.assertEqual(response.json(), {'message': 'Hello Password Generator!'})
