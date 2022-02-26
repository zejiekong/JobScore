from pyresparser import ResumeParser

def parse_file(file_path):
    return ResumeParser(file_path).get_extracted_data()