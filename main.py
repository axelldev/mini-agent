import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="user prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    try:
        messages = [
            types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
        ]
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=messages
        )
        if response is None or response.usage_metadata is None:
            raise Exception("Usage metadata not found")
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        print("Response:", response.text)
    except Exception as e:
        print("Error", e)


if __name__ == "__main__":
    main()
