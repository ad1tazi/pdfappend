import sys

from PyPDF2 import PdfFileMerger


def append_files(original, appendage, merged_name='merged'):
    merger = PdfFileMerger()

    merger.append(original)
    merger.append(appendage)

    merger.write(merged_name + '.pdf')
    merger.close()

def main(argv):
    #print(argv)
    if len(argv) > 2:
        append_files(argv[0], argv[1], argv[2])
    else:
        append_files(argv[0], argv[1])

if __name__ == '__main__':
    main(sys.argv[1:])