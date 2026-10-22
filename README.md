# Healthcare EDI Claims Parser & SQL Analytics Pipeline

## Executive Summary
A mini-ETL (Extract, Transform, Load) pipeline that automates the processing of raw, unstructured X12 EDI healthcare claims data. The pipeline uses a custom Python script to parse raw text streams, extracts claim identifiers and total charge amounts into a structured dataset, loads the records into a local SQLite relational database, and executes SQL queries to aggregate financial batch metrics.

## The Problem Solved
Healthcare billing logs and electronic data interchange (EDI) files are typically delivered as massive, unformatted X12 text files. Reviewing these logs manually to check claim details is tedious and error-prone. This project automates the extraction and database ingestion of claim records, making batch metrics instantly queryable.

## Technical Stack & Skills Demonstrated
* **Programming & Libraries:** Python, Pandas, SQLite (`sqlite3`), `os` file pathing
* **Database & Querying:** Relational Database Design, SQL Aggregations (`COUNT`, `SUM`)
* **Core Analytics Skills:** File Parsing, Data De-Serialization, Exception Handling, Data Pipeline Automation

## Pipeline Architecture & Workflow
1. **Extraction (Python):** Ingests raw X12 EDI text logs (`sample_edi_batch.txt`), using custom string-splitting rules to isolate segment markers (`~`) and element delimiters (`*`).
2. **Transformation (Pandas):** Filters for claim segments (`CLM`), extracts Claim IDs and financial charges, and structures records into a clean Pandas DataFrame exported as a CSV.
3. **Loading (SQLite):** Connects to a local SQLite database (`claims.db`) and creates a structured relational table (`claims`).
4. **Querying (SQL):** Runs SQL query scripts to calculate batch metrics, including total claims processed and total financial charges.

## How to Run
1. Clone or download this repository.
2. Ensure Python and Pandas are installed (`py -m pip install pandas`).
3. Run the scripts in sequence:
   ```bash
   py edi_parser.py   # Parses raw text and creates CSV
   py load_db.py      # Ingests CSV into SQLite database
   py query_db.py     # Executes SQL queries and prints batch results
