from sqlalchemy import text

from backend.app.db.database import engine

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("✅ Database Connected Successfully!")
except Exception as e:
    print("❌ Database Connection Failed")
    print(e)