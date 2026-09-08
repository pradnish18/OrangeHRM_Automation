import os

class Config:
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "Admin")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")
    EXPLICIT_WAIT = 15
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
