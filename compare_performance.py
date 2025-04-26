import asyncio
import time
from sync_processor import process_pdf_sync
from async_processor import process_pdf_async


async def main():
    print("Starting performance comparison...\n")

    print("Running synchronous version...")
    sync_results, sync_time = process_pdf_sync("sample.pdf")

    print("\nRunning asynchronous version...")
    async_results, async_time = await process_pdf_async("sample.pdf")

    print("\n=== Performance Comparison ===")
    print(f"Synchronous processing time: {sync_time:.2f} seconds")
    print(f"Asynchronous processing time: {async_time:.2f} seconds")
    print(f"Speed improvement: {(sync_time - async_time) / sync_time * 100:.2f}%")

    # print("\n=== Score Comparison ===")
    # print("Synchronous Results:")
    # for page_num, result in sync_results:
    #     print(f"\nPage {page_num}:")
    #     print(result)

    # print("\nAsynchronous Results:")
    # for page_num, result in async_results:
    #     print(f"\nPage {page_num}:")
    #     print(result)


if __name__ == "__main__":
    asyncio.run(main())
