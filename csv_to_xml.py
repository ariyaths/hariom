#csv_to_xml

#           Title                   Type Format  Year Rating  Stars  \
# 0  Enemy Behind           War,Thriller    DVD  2003     PG     10   
# 1  Transformers  Anime,Science Fiction    DVD  1989      R      9   

#              Description  
# 0          Talk about...  
# 1  A Schientific fiction 
# https://stackoverflow.com/questions/41059264/simple-csv-to-xml-conversion-python

# Holdings
# Price
# Eff Global Weight (%)
# Eff Weight (%)
# Global Weight (%)
# Gross Exposure
# Holdings Date
# Holdings Update Date
# Mkt Value
# Notional
# Par Value
# Weight (%)
# Active Weight (%)
# Eff Global Active Weight (%)

import pandas as pd
df = pd.read_csv('limits.csv', sep=',')

def convert_row(row):
    return """<movietitle="%s">
    <type>%s</type>
    <format>%s</format>
    <year>%s</year>
    <rating>%s</rating>
    <stars>%s</stars>
    <description>%s</description>
</movie>""" % (
    row.Title, row.Type, row.Format, row.Year, row.Rating, row.Stars, row.Description)

print '\n'.join(df.apply(convert_row, axis=1))