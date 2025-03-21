
import secrets

# Create your models here.

def generate_hex_code():
    return secrets.token_hex(3)
print(generate_hex_code())