#%% [markdown]
# Load XML File:

#%%
import os
import re

from lxml import etree, objectify

#%% [markdown]
# This is a testing comment

#%%
#xml_file = open(os.getcwd()+'/combined_output.xml')
# print('TYPE: ' + str(type(xml_file)))
all_xml_data = None
xml_file_path = os.getcwd()+'/combined_output.xml'
with open(os.getcwd()+'/combined_output.xml', 'r') as xml_file:
    all_xml_data = xml_file.read()

print('String Length: %s' % len(all_xml_data))
#print('String Length:', len(all_xml_data))
#print('String Length:' + len(all_xml_data)) # Does not work

#%%
#tags = []
# for line in all_xml_data:
#    #tags.append(re.search('<(.*)>', line))
#    tags = re.split('<|>',line)
#    #tags.append(line.find)

#Works somewhat
tags = re.split('<|>',all_xml_data)
print('Length: %i' % len(tags))
print('First Tag Length: %i' % len(tags[0]))
#print('Tags: %s' % tags)

#New Try
actual_tag = []
potential_tag =None
leading_tag = re.split('<',all_xml_data)
delimiter = '>'
potential_tag = [tag for tag in leading_tag if delimiter in tag]

#actual_tag = re.split(' |=|>', potential_tag)
#tag_list = tag


print('Leading Tags Length: %i' % len(leading_tag))
print('First Leading Tag: %s' % (leading_tag[0]))
print('2nd Leading Tag: %s' % (leading_tag[1]))

print('List of Potential Tags Length: %i' % len(potential_tag))

print('List of Actual Tags Length: %i' % len(actual_tag))

#print("\n".join(potential_tag))

#print("\n".join(leading_tag))

#print('List of Actual Tags: %s' % (actual_tag))
#print(tags)


#%% [markdown]
# Testing
parser = etree.XMLParser(remove_comments=True, recover=True)
#parser = objectify.makeparser(remove_comments=True)
tree = objectify.parse(xml_file_path, parser=parser)

#print(tree)

