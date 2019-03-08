import xml.etree.ElementTree
import os

from lxml import etree, objectify
from bs4 import BeautifulSoup

xml_file_path = os.getcwd()+'/combined_output.xml'

#tree = xml.etree.ElementTree.parse(xml_file_path)

parser = etree.XMLParser(remove_comments=True, recover=True )
#parser = objectify.makeparser(remove_comments=True)
tree = objectify.parse(xml_file_path, parser=parser)
print('Type: %s ' % type(tree) )

root = tree.getroot()
print('Root: %s' % tree.getroot())

my_rules = root.findall('rule')
print('Type expected for Child Element Rules -->List: %s' % type(my_rules))
print('Child Element Rules --> List Length: %i' % len(my_rules))

rules_children = root.getchildren()
print('Type expected for Rules Children -->List: %s' % type(rules_children))
print('Rules Children --> List Length: %i' % len(rules_children))
print('RULES: %s' % rules_children  )

# Elements carrt attributes as a dict
print(rules_children[0].tag)
print(rules_children[0].keys())
print(rules_children[0].get('name'))
print(rules_children[0].get(rules_children[0].keys()[0]))


rules = tree.findall('rule')
rules_all = tree.iterfind('rule')

print('Type expected for Rules -->List: %s' % type(rules))
print('Type expected for Rules -->List: %s' % type(rules_all))
print('Rules --> List Length: %i' % len(rules))
#print('Rules --> List Length: %i' % len(rules_all))
print('Rules list: %s' % rules)
print('Rules list: %s' % rules_all)


#my_tree = etree.ElementTree(tree)

#soup = BeautifulSoup(tree, 'lxml')

#lxml
# for node in tree.iter('*'):
#     print(node.tag)

