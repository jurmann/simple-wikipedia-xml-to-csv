# wikipedia-xml-to-csv
Simple python program to write wikipedia data to a csv file from wikipedia xml data dump. This program is still being worked on.

Link to download xml file: https://meta.wikimedia.org/wiki/Data_dump_torrents
Currently only the simple wikipedia has been tested with this program due to storage limitations locally. 

Open python file in text editor and enter input and output files. The input file is the xml file downloaded from wikipedia data dumps. The output file will be created if it does not currently exist. The only columns exported to csv are id, title, timestamp, and text. Please note Excel cannot handle this amount of text in a cell so it is not recommended to open the csv file through excel.
