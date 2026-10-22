#edi_parser.py

import os 
#Automatically find the exact folder where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
# Building the exact path to the data file relative to the script
file_path = os.path.join(script_dir, 'data', 'sample_edi_batch.txt')
#Opening and reading the file content
try:
    with open(file_path, 'r') as file:
        raw_text = file.read()
    print("Successfully loaded the EDI file!\n")
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}.")
    exit()

#Splitting the text into individual segments using the tilde (~) separator
segments = raw_text.split('~')
print(f"Total segments found in file: {len(segments)}\n")
print("-" * 50)
print("EXTRACTING CLAIM INFORMATION:")
print("-" *50)

#Looping through each segment to find and extract Claims (CLM)
for segment in segments:
    #Clean up hidden newlines/spaces
    segment = segment.strip ()
    #Skip if the segment is empty
    if not segment:
        continue

    elements = segment.split('*')
    
    #If the first element is 'CLM', it's a claim segment!
    if elements[0] == 'CLM':
        claim_id = elements[1]
        total_charge = elements[2]
        print(f"-> Found Claim ID: {claim_id} | Total Charge: ${total_charge}")
print("-" * 50)