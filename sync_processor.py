import os
import time
from PyPDF2 import PdfReader
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def process_page_sync(page_content):
    client = OpenAI(api_key=os.getenv("OPENAIKEY"))
    prompt = f"You are a medical school residency evaluator, please give this section a score from 1-100. Here is the application: {page_content}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful medical school residency application evaluator.",
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


def process_pdf_sync(pdf_path):
    reader = PdfReader(pdf_path)
    results = []

    start_time = time.time()

    for i, page in enumerate(reader.pages[:6]):  # Process first 6 pages
        print(f"Processing page {i+1} synchronously...")
        text = page.extract_text()
        result = process_page_sync(text)
        results.append((i + 1, result))

    end_time = time.time()
    total_time = end_time - start_time

    return results, total_time


if __name__ == "__main__":
    results, total_time = process_pdf_sync("sample.pdf")
    print("\nSynchronous Processing Results:")
    for page_num, result in results:
        print(f"\nPage {page_num} Score:")
        print(result)
    print(f"\nTotal processing time: {total_time:.2f} seconds")
