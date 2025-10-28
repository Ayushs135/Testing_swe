from locust import HttpUser, task, between
import json

class FirebaseUser(HttpUser):
    wait_time = between(1, 3) 

    firebase_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDiehZHyHpOpaZKbBqiE3YpLQeA1i3M0EE"
    headers = {"Content-Type": "application/json"}

    # --- Task 1: Successful login (correct credentials) ---
    @task(5)
    def successful_login(self):
        payload = {
            "email": "Admin@new.com",
            "password": "Admin123",
            "returnSecureToken": True
        }

        with self.client.post(
            self.firebase_url,
            data=json.dumps(payload),
            headers=self.headers,
            catch_response=True,
            name="/firebase-login-success"
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Expected 200 but got {response.status_code}")

    # --- Task 2: Failed login (incorrect credentials) ---
    @task(2)
    def failed_login(self):
        payload = {
            "email": "testuser1@example.com",
            "password": "wrongpassword",
            "returnSecureToken": True
        }

        with self.client.post(
            self.firebase_url,
            data=json.dumps(payload),
            headers=self.headers,
            catch_response=True,
            name="/firebase-login-fail"
        ) as response:
            if response.status_code == 400:
                response.failure("Invalid credentials (expected failure)")
            elif response.status_code == 200:
                response.failure("Unexpected success on invalid credentials!")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")
