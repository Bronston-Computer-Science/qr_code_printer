from passlib.context import CryptContext
import bcrypt

passwd_context = CryptContext (schemes = ['bcrypt'])

def hash_passwd(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode('utf-8')

def verify_passwd(password: str, hash) -> bool:
    password_byte_enc = password.encode('utf-8')
    return bcrypt.checkpw(password = password_byte_enc , hashed_password = hash)