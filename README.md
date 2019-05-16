# Convert gedcom to html with bootstrap, d3, and jquery using python

## Setup

1. Download a copy of `d3.v4.min.js` and place it in the `assets/js` folder. You can find this file [here](https://d3js.org/d3.v4.min.js).
2. Download a copy of [Font Awesome 4.7.0](https://fontawesome.com/v4.7.0/get-started/), save the extracted `font-awesome-4.7.0` folder to the `assets/` folder as `font-awesome`.

## Usage

Generates an example set of pages with a folder `generated/` using the included demo `.ged` file for the family history of US presidents.
```
python exmaple.py
```

## Method options

# g.options.file_path = "demo/dutchroyalfamily.ged"
# g.options.title = "Family tree of the Dutch Royal Family"
# g.options.home_person_id = "I1208"

## An example says it all. So have a look at:
* [Dutch Royal Family](//picnicprojects.com/gedcom2html/dutchroyalfamily/)
## Features
- one html page for each individual in the gedcom file
- ancenstor and descendant fan charts
- a navigator chart (with d3 force simulation)
## Special Thanks
- gedcom2html uses [gedcom.py](https://github.com/nickreynke/python-gedcom) by Nick Reynke to parse the gedcom file
- [famousfamilytrees](http://famousfamilytrees.blogspot.com/?m=1) for the demo gedcom files
## To do
- beautify CSS / colors
- command line options
   * -private
      * none
      * hide dates of people alive
      * hide all people alive
   * -output-dir
   * -language
- list of people in right column
- improve age calculation

### Hayward TODO
- setup circle CI build based on gedcom repo commits
- host on heroku?
- ~~correct backwards date format~~
- add navigation sidebar
- move graphs into individual tabs
- include middle names in main chart area
- correctly display referred name (married vs brith) and nick/call name
- add additional information along the right side of page (notes, schooling, etc)
- ~~change chart blue colour to be lighter shade~~
