import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, project_root)

from services.groq_service import ask_groq

response = ask_groq("What is invoice processing?")

print(response)