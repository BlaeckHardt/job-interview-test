import os
from app import create_app

__env = os.getenv("ENV") or "dev"
app = create_app(__env)

def run():
    app.run(port=8088, debug=True)

if __name__ == "__main__":
    run()
