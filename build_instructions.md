# Build Instructions

1. Install Python (3.10 or higher)
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run converter:
   ```
   python converter_vyapar.py party PARTYVP.csv Vyapar_Parties.xlsx
   python converter_vyapar.py item ITEMVP.csv Vyapar_Items.xlsx
   ```
4. To make EXE:
   ```
   pip install pyinstaller
   pyinstaller --onefile --noconsole --name Busy2VyaparSep25 converter_vyapar.py
   ```
