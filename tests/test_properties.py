import os

# ENVIRONMENT=stage pytest . -s
def test_getenv():
    environment = os.getenv("ENVIRONMENT", "local")
    print(f"\nEnvironment: {environment}")

