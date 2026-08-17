from backend.app.core.security import create_access_token

token = create_access_token(
    {"sub": "shivam@example.com"}
)

print(token)