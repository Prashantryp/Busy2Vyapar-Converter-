import pandas as pd
import sys
from pathlib import Path

def clean_balance(val):
    try:
        if pd.isna(val) or str(val).strip() == "":
            return 0.00
        s = str(val).strip()
        amt = float(s.replace("Dr","").replace("Cr","").replace(",","").strip())
        if "Cr" in s:
            return -amt
        else:
            return amt
    except:
        return 0.00

def convert_party(input_file, output_file):
    df = pd.read_csv(input_file, header=1, encoding="latin1")
    out = pd.DataFrame()
    out["Name*"] = df["Name"]
    out["Contact No."] = df["Mobile No."] if "Mobile No." in df.columns else ""
    out["Email ID"] = ""
    addr_cols = [c for c in df.columns if "Address" in c]
    if addr_cols:
        out["Address"] = df[addr_cols].fillna("").agg(" ".join, axis=1)
    else:
        out["Address"] = ""
    if "State" in df.columns:
        out["Address"] = out["Address"].astype(str) + " " + df["State"].fillna("").astype(str)
    if "Opening Bal.in Base Currency" in df.columns:
        out["Opening Balance"] = df["Opening Bal.in Base Currency"].apply(clean_balance)
    else:
        out["Opening Balance"] = 0.00
    out["Opening Date (dd/MM/yyyy)"] = "01/04/2024"
    out["GSTIN"] = df["GST No."] if "GST No." in df.columns else ""
    out.to_excel(output_file, index=False)
    print(f"Party master converted: {output_file}")

def convert_item(input_file, output_file):
    df = pd.read_csv(input_file, header=0, encoding="latin1")
    out = pd.DataFrame()
    out["Item Code"] = ["ITM" + str(i+1) for i in range(len(df))]
    out["Item Name"] = df["Name"] if "Name" in df.columns else ""
    out["HSN"] = df["HSN Code"] if "HSN Code" in df.columns else ""
    out["Sale Price"] = df["Sale Rate"] if "Sale Rate" in df.columns else 0.0
    out["Purchase Price"] = df["Purchase Rate"] if "Purchase Rate" in df.columns else 0.0
    if "Op. Stock(Main)" in df.columns:
        out["Opening Stock Quantity"] = df["Op. Stock(Main)"].fillna(0)
    elif "Opening Stock" in df.columns:
        out["Opening Stock Quantity"] = df["Opening Stock"].fillna(0)
    else:
        out["Opening Stock Quantity"] = 0
    if "Tax Category" in df.columns:
        def fmt_tax(val):
            try:
                if pd.isna(val): return ""
                v = str(val).replace("%","").strip()
                if v=="": return ""
                return f"IGST@{v}%"
            except: return ""
        out["Tax Rate"] = df["Tax Category"].apply(fmt_tax)
    else:
        out["Tax Rate"] = ""
    out["Minimum Stock Quantity"] = 0
    out["Item Location"] = ""
    out["Tax Inclusive (Y/N)"] = "N"
    out.to_excel(output_file, index=False)
    print(f"Item master converted: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python converter_vyapar.py party|item input.csv output.xlsx")
        sys.exit(1)
    mode, infile, outfile = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    if mode == "party":
        convert_party(infile, outfile)
    elif mode == "item":
        convert_item(infile, outfile)
    else:
        print("Invalid mode. Use 'party' or 'item'.")
