import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


if SECRET_KEY is None:
    raise RuntimeError("SECRET_KEY is None")

if ALGORITHM is None:
    raise RuntimeError("ALGORITHM is None" )

try:
    ACCESS_TOKEN_EXPIRE_MINUTES = int(ACCESS_TOKEN_EXPIRE_MINUTES)
except ValueError:
    raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES does not exist or is not an integer")
except TypeError:
    raise TypeError("ACCESS_TOKEN_EXPIRE_MINUTES does not exist or is not an integer")
