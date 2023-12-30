import unittest
from app import create_app
from datetime import datetime


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up your Flask test client
        self.app = create_app()
        self.app.config["TESTING"] = True
        # self.app_context = self.app.app_context()  # Create an app context
        # self.app_context.push()  # Push the context
        self.client = self.app.test_client()

    def test_home_page(self):
        # Test that the home page loads correctly
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_rest_period_calculation_not_respected(self):
        # Test the rest period calculation
        response = self.client.post(
            "/",
            data={
                "on_call_ends[]": [
                    datetime(2023, 1, 1, 17, 0).isoformat(),
                    datetime(2023, 1, 2, 17, 0).isoformat(),
                ],
                "office_start": datetime(2023, 1, 3, 9, 0).isoformat(),
            },
        )
        self.assertIn("Rest period is not respected", response.data.decode())

    def test_rest_period_calculation_respected(self):
        # Test the rest period calculation
        response = self.client.post(
            "/",
            data={
                "on_call_ends[]": [
                    datetime(2024, 1, 1, 18, 0).isoformat(),
                    datetime(2024, 1, 1, 20, 45).isoformat(),
                ],
                "office_start": datetime(2024, 1, 2, 9, 0).isoformat(),
            },
        )
        self.assertIn("Required rest period is respected", response.data.decode())

    def test_about_page(self):
        # Test that the about page loads correctly
        response = self.client.get("/about/")
        # print(response.data)  # To debug
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "About", response.data.decode()
        )  # Optionally check for some content
        self.assertIn("Flask", response.data.decode())

    def test_about_page_redirection(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 308)  # = Permanent Redirect

    def test_static_files(self):
        # List of paths to static files you want to test
        static_files = ["css/style.css", "js/script.js", "images/favicon.ico"]

        for file in static_files:
            response = self.client.get("/static/" + file)
            print(type(response))  # Add this line for debugging
            self.assertEqual(response.status_code, 200, f"Failed to find {file}")

    # def tearDown(self):
    #    self.app_context.pop()  # Pop the context after the test


if __name__ == "__main__":
    unittest.main()
