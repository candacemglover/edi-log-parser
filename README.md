# EDI Claim Data Parser

## Overview
A lightweight Python script built to parse raw, unstructured X12 EDI electronic claim files. This project automates the extraction of key healthcare billing data—specifically targeting claim IDs and total charge amounts—without relying on manual entry or heavy external libraries.

## Problem Solved
Healthcare billing logs and electronic data interchange (EDI) files are typically delivered as massive, unformatted text files. Reviewing these logs manually to check claim details is tedious and inefficient. This script uses custom Python string-parsing logic to ingest the raw text, segment the data, and extract essential financial records instantly.

## Tech Stack & Skills Demonstrated
* **Language:** Python
* **Core Concepts:** File handling (`open`), string splitting (`.split()`), conditional logic (`if/else`), and data de-serialization.

## How the Script Works
1. **File Ingestion:** Securely opens and reads the raw text file using Python context managers.
2. **Segment Splitting:** Breaks the continuous text wall into individual data segments using the standard X12 tilde (`~`) delimiter.
3. **Element Parsing:** Loops through each segment, splits by asterisks (`*`), and isolates specific indices to pull claim IDs and charges.
4. **Output:** Prints the extracted metrics cleanly to the terminal.

## How to Run This Project
1. Clone or download this repository.
2. Ensure you have Python installed.
3. Run the parser script in your terminal:
   ```bash
   py edi_parser.py