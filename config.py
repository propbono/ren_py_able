# Configuration file
import os
import sys


class RealConfig:
    # Constant to control version of programme
    VERSION = "0.5.5"

    # Constant to determine where TIFF files are stored
    TIF_DIRECTORY = 'Q:\\TIFF\\Test\\'
    PPF_DIRECTORY = 'B:\\'
    PDF_ARCHIVE_DIRECTORY = 'F:\\00Archiwum - PDFdoCIP\\'
    DOA_DIRECTORY = 'W:\\'


class FakeConfig:
    # Constant to control version of programme
    VERSION = "0.5.5"

    # Constant to determine where TIFF files are stored
    TIF_DIRECTORY = os.path.dirname(sys.argv[0]) + '/tif/'
    PPF_DIRECTORY = os.path.dirname(
        sys.argv[0]) + '/ppf/'  # for compatibility with windows
    PDF_ARCHIVE_DIRECTORY = os.path.dirname(sys.argv[0]) + '/pdf/'
    DOA_DIRECTORY = os.path.dirname(sys.argv[0]) + '/doa/'
	

