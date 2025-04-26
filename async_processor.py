import os
import time
import asyncio
from PyPDF2 import PdfReader
from openai import AsyncOpenAI


async def process_page_async(page_content):
    client = AsyncOpenAI()
    prompt = f"You are a medical school residency evaluator, please give this section a score from 1-100. Here is the application: {page_content}"

    response = await client.chat.completions.create(
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


async def process_pdf_async(pdf_path):
    reader = PdfReader(pdf_path)
    tasks = []

    start_time = time.time()

    # Create tasks for all pages
    for i, page in enumerate(reader.pages[:6]):  # Process first 6 pages
        print(f"Creating task for page {i+1}...")
        text = page.extract_text()
        task = asyncio.create_task(process_page_async(text))
        tasks.append((i + 1, task))

    # Wait for all tasks to complete
    results = []
    for page_num, task in tasks:
        result = await task
        results.append((page_num, result))

    end_time = time.time()
    total_time = end_time - start_time

    return results, total_time


async def main():
    results, total_time = await process_pdf_async("sample.pdf")
    print("\nAsynchronous Processing Results:")
    for page_num, result in results:
        print(f"\nPage {page_num} Score:")
        print(result)
    print(f"\nTotal processing time: {total_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
