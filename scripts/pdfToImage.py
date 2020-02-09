import os
import sys
import argparse

from pdf2image import convert_from_path

usage = "python %s --pdf <PDF_location>"%(sys.argv[0])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage)
    parser.add_argument("--pdf", dest="pdfFile", help="the source path of PDF file")
    parser.add_argument("--out", dest = "outDir", help= "Website location where to save IMAGES")
    args = parser.parse_args()
    
    pages = convert_from_path(os.path.abspath(args.pdfFile))
    for i,page in enumerate(pages):
        outLoc = os.path.abspath(os.path.join(args.outDir, "file%s.jpg"%(i)))
        page.save(outLoc, 'JPEG')