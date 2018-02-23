import xml.etree.ElementTree as ET
import csv

# enter file location to write to (new csv file)
write_file = ''

# enter xml file location to read from
read_file = ''

print 'setting up csv...'
csv_file = open(write_file)
first_row = [['page_id', 'title', 'timestamp', 'text']]

print 'parsing ...'

tree = ET.parse(read_file)

print 'getting root ...'
root = tree.getroot()
print 'running ...'

with csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(first_row)

    for page in root.findall('page'):
        title = None
        page_id = False
        text = None
        timestamp = None
        try:
            title = page.find('title').text.encode('utf-8')
            page_id = page.find('id').text.encode('utf-8')

            try:
                int(page_id)
            except:
                page_id = False
        except:
            pass

        for this in page.findall('revision'):
            try:
                text = this.find('text').text.encode('utf-8')
                timestamp = this.find('timestamp').text.encode('utf-8')
            except:
                pass

        row = [[page_id, title, timestamp, text]]

        # verify rows have values before writing to csv
        if bool(int(page_id)) and bool(title) and bool(timestamp) and bool(text):
            writer.writerows(row)

print 'PROCESS COMPLETE'
