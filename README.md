# Busy2Vyapar Converter

Convert Busywin exported masters (Party, Item) into Vyapar importable Excel files.

## Features
- Party Master conversion
  - Name, Contact, Address, GSTIN, Opening Balance (Dr/Cr handled), Opening Date
- Item Master conversion
  - Item Name, HSN, Sale/Purchase Price, Opening Stock, Tax Rate, etc.
- Output format matches Vyapar's sample import headers
- Invalid emails blanked automatically

## Usage
1. Install Python 3.10+ and libraries from `requirements.txt`
2. Run command:
   ```
   python converter_vyapar.py party PARTYVP.csv Vyapar_Parties.xlsx
   python converter_vyapar.py item ITEMVP.csv Vyapar_Items.xlsx
   ```
3. Import generated Excel files into Vyapar Desktop (recommended).

## Build EXE
To build a standalone Windows executable:
```
pip install pyinstaller
pyinstaller --onefile --noconsole --name Busy2VyaparSep25 converter_vyapar.py
```
Resulting EXE will be in `dist/Busy2VyaparSep25.exe`.

## License
MIT License
