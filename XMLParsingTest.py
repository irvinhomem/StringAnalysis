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

#print(tree.getroot().)

my_tree = etree.ElementTree(tree)

soup = BeautifulSoup(tree, 'lxml')

#lxml
for node in tree.iter('*'):
    print(node.tag)

