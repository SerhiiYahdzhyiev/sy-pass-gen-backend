import re

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

    def test_generate(self) -> None:
        test_pattern = r"^([a-zA-Z0-9]){10}"
        valid_params = {
                "length": 10,
                "lowercase": True,
                "uppercase": False,
                "digits": True,
                "special": False,
                }
        response = self.client.post("/generate", json=valid_params)
        self._run_std_response_assertions(response, 200)
        data = response.json()

        suggestion = data["password_suggestion"]
        self.assertTrue(re.match(test_pattern, suggestion))
        
        invalid_params = {
                "length": 0,
                "lowercase": True,
                "uppercase": False,
                "digits": True,
                "special": False,
                }
        response = self.client.post("/generate", json=invalid_params)
        self._run_std_response_assertions(response, 500)
        data = response.json()

        detail = data["detail"]
        self.assertEqual(detail, "Cannot generate password with 0 or negative length!")
        
        invalid_params = {
                "length": 10,
                "lowercase": False,
                "uppercase": False,
                "digits": False,
                "special": False,
                }
        response = self.client.post("/generate", json=invalid_params)
        self._run_std_response_assertions(response, 500)
        data = response.json()

        detail = data["detail"]
        self.assertEqual(detail, "Cannot generate password from empty set of possible characters!")
