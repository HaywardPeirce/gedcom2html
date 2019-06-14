from gedcom2html import Gedcom2html
import argparse
# g = Gedcom2html()
# g.options.file_path = "demo/dutchroyalfamily.ged"
# g.options.title = "Family tree of the Dutch Royal Family"
# g.options.home_person_id = "I1208"
# g.write_html()

#parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f','--filepath', help='The path to the gedcom file containing the family tree data')
parser.add_argument('-t','--title', help='The title of the family tree site')
args = parser.parse_args()

title = "Family Tree"

file_path = "../family-tree/peirce_public.ged"

if args.filepath: file_path = args.filepath
if args.title: title = args.title

# print(title)
# print(file_path)

g = Gedcom2html()
# g.options.file_path = "demo/americanpresidents.ged"
g.options.file_path = file_path
g.options.title = title
g.write_html()
