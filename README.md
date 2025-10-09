# B210-Assignment_4
# a What is the purpose of this program(s)? 
The purpose of this program is to write a function that prints the names of songs that are within a specified range of energy.
# b What does the program do? What are the input(s)? What are the outputs(s)
The program: 
1. Reads a CSV of Taylor Swift tracks (default file: taylor_discography.csv).
2. Robustly parses CSV lines (handles double-quoted fields and commas inside quotes).
3. Strips a UTF‑8 BOM from the header if present so the header column track_name is recognized.
4. Finds the columns named track_name and energy.
5. Filters all tracks whose numeric energy value falls between a user-specified minimum and maximum (inclusive).
6. Prints the matching track names to the console.
The primary input is the taylor_discography.csv file. It also takes the minimum and maximum expected numeric (float) energy values, typically in the [0.0, 1.0] range.
The outputs are printed track names (one per line) for all rows where the energy is within the requested range.
# c How do you use the program?
1. Open PowerShell (or CMD).
2. Run the script with Python:
 If you have Python on PATH:
"C:\Path\To\Python\python.exe" "C:\Users\jinas\Downloads\Assignment 4 Built-In-Functions.py"
3. Follow the prompts:
CSV path [default: C:\Users\jinas\Downloads\taylor_discography.csv]:
Press Enter to use the default file.
OR paste a full path, e.g. C:\other\folder\myfile.csv
OR paste a Python-style call and the script will parse it, e.g.: print_songs_in_energy_range(r'C:\Users\jinas\Downloads\taylor_discography.csv', 0.4, 0.8) (the script extracts the path and number arguments and runs immediately)
Min energy (0.0-1.0) [default: 0.5]: type a number like 0.3
Max energy (0.0-1.0) [default: 0.7]: type a number like 0.7
Output: matching track names will be printed to the console (one per line).
