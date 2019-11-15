import os
import pandas as pd


def main(infile):
    outfile = infile.replace(".xlsx", "_result.csv")
    df = pd.read_excel(infile, header=None) 
    # df.to_excel(outfile, header=False, index=False, encoding="utf_8_sig", engine='xlsxwriter')
    df.to_csv(outfile, header=False, index=False, encoding="utf_8_sig")


if __name__ == "__main__":
    infile = 'data/city.xlsx'
    main(infile)
