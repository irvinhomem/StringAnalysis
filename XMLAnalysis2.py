#%% [markdown]
# Load XML File:

#%%
import os
import re

#%% [markdown]
# This is a testing comment

#%%
#xml_file = open(os.getcwd()+'/combined_output.xml')
# print('TYPE: ' + str(type(xml_file)))
with open(os.getcwd()+'/combined_output.xml', 'r') as xml_file:
    all_xml_data = xml_file.read()

print('String Length: %s' % len(all_xml_data))
print('String Length:', len(all_xml_data))
#print('String Length:' + len(all_xml_data)) # Does not work

#%%
tags = []
for line in xml_file:
   tags.append(re.search('<(.*)>', line))
   #tags.append(line.find)

#print(tags)
print('Length:', tags[0])

#%% [markdown]
# Testing

