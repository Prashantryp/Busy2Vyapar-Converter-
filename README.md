# Busy2Vyapar Converter

🚀 A simple open-source tool to convert **Busywin exported master files** (Party & Item) into **Vyapar importable Excel files**.

---

## ✨ Features
- **Party Master Conversion**
  - Fields: Name, Contact No, Address, GSTIN, Opening Balance (Dr/Cr handled), Opening Date
- **Item Master Conversion**
  - Fields: Item Name, HSN, Sale/Purchase Price, Opening Stock Quantity, Tax Rate
- Automatic cleanup:
  - Invalid emails are blanked
  - Dr/Cr balances converted to numeric (+/-)
  - Auto Item Codes generated if missing
- Output format matches Vyapar’s official import template.

---

## 📦 Requirements
- Python 3.10 or higher
- Libraries: `pandas`, `openpyxl`

Install dependencies:
```bash
pip install -r requirements.txt
