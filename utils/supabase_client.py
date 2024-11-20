import os
from supabase import create_client, Client  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Load environment variables from .env
load_dotenv()

# Function to create and return Supabase client
def get_supabase_client() -> Client:
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")  # Use the Service Role Key for secure access

    if not url or not key:
        raise ValueError("Supabase URL or Service Role Key is missing from environment variables.")

    supabase= create_client(url, key)

    return supabase
