# Evaluation Performance Comparison

This project demonstrates the performance difference between synchronous and asynchronous processing when evaluating applications using OpenAI's GPT models. The project includes two implementations that process PDF documents and obtain AI-generated scores for each page.

## Project Structure

- `sync_processor.py`: Processes PDF pages synchronously (one at a time)
- `async_processor.py`: Processes PDF pages asynchronously (concurrent processing)
- `compare_performance.py`: Compares the performance of both implementations
- `requirements.txt`: Lists all project dependencies

## Features

- Processes up to 6 pages of a PDF document
- Uses OpenAI's GPT model to evaluate each page
- Provides scoring from 1-100 for each section
- Compares processing time between sync and async implementations
- Shows detailed performance metrics and score comparisons

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key
- A PDF document for testing

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On Unix or MacOS
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Place your PDF file in the project directory and name it `sample.pdf`

## Usage

1. To run the synchronous processor only:
   ```bash
   python sync_processor.py
   ```

2. To run the asynchronous processor only:
   ```bash
   python async_processor.py
   ```

3. To run the performance comparison:
   ```bash
   python compare_performance.py
   ```

## Expected Output

The comparison script will show:
- Processing time for both synchronous and asynchronous methods
- Percentage improvement in processing speed
- Detailed scores for each page from both methods

Example output:
```
=== Performance Comparison ===
Synchronous processing time: 25.34 seconds
Asynchronous processing time: 5.67 seconds
Speed improvement: 77.62%


```

## Notes

- The asynchronous version typically performs significantly faster as it processes all pages concurrently
- Processing time may vary based on:
  - PDF size and complexity
  - OpenAI API response time
  - Internet connection speed
  - System resources

## Troubleshooting

1. If you get API key errors:
   - Ensure your `.env` file is in the correct location
   - Verify your API key is valid
   - Make sure python-dotenv is properly installed

2. If you get PDF-related errors:
   - Ensure your PDF file is named `sample.pdf`
   - Verify the PDF is not corrupted
   - Check if the PDF is readable and not password-protected
