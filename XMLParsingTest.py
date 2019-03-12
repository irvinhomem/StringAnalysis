import xml.etree.ElementTree
import os
import networkx as nx
import matplotlib.pyplot as plt
import xmltodict

from lxml import etree, objectify
from bs4 import BeautifulSoup

xml_file_path = os.getcwd()+'/combined_output.xml'

#tree = xml.etree.ElementTree.parse(xml_file_path)

parser = etree.XMLParser(remove_comments=True, recover=True )
#parser = objectify.makeparser(remove_comments=True)
tree = objectify.parse(xml_file_path, parser=parser)
print('Type: %s ' % type(tree) )

#xml_dict = xmltodict.parse(xml_file_path)

root = tree.getroot()
print('Root: %s' % tree.getroot())

my_rules = root.findall('rule')
print('Type expected for Child Element Rules -->List: %s' % type(my_rules))
print('Child Element Rules --> List Length: %i' % len(my_rules))

rules_children = root.getchildren()
print('TYPE expected for Rules Children -->List: %s' % type(rules_children))
print('Rules Children --> List Length: %i' % len(rules_children))
print('Rules Children ELEMENT exprected type: %s' % type(rules_children[0]))

print('RULES: %s' % rules_children  )


# Elements carry attributes as a dict
print(rules_children[0].tag)
print(rules_children[0].keys())
print(rules_children[0].get('name'))
print(rules_children[0].get(rules_children[0].keys()[0]))

# Create a set of node-attribute tuples
# https://networkx.github.io/documentation/stable/reference/classes/generated/networkx.Graph.add_nodes_from.html#networkx.Graph.add_nodes_from
all_rule_groups = root.findall('group')
print('All GROUPS length: --> %i' % len(all_rule_groups))
for idx, single_group in enumerate(all_rule_groups):
    #print(idx, single_group)
    print('ELEMENT NAME: %s :: ATRR[%s] :: VALUE[%s]' % (all_rule_groups[idx].tag,all_rule_groups[idx].keys(), all_rule_groups[idx].get('name')))     # or alternatively single_group.tag
    #print(single_group.tag)     # or alternatively single_group.tag


rules = tree.findall('rule')
rules_all = tree.iterfind('rule')

print('Type expected for Rules -->List: %s' % type(rules))
print('Type expected for Rules -->List: %s' % type(rules_all))
print('Rules --> List Length: %i' % len(rules))
#print('Rules --> List Length: %i' % len(rules_all))
print('Rules list: %s' % rules)
print('Rules list: %s' % rules_all)


# Adding XML elements to a Graph
my_graph = nx.Graph()
#my_graph.add_nodes_from(rules_children, data=True)
my_graph.add_nodes_from(rules_children)
print('My GRAPH nodes NUMBER: %s' % my_graph.number_of_nodes())
print('Nodes ALL Type: %s' % type(my_graph.nodes))
print('NODE ... ALL should be dictionary: %s' % (my_graph.nodes))

print('-----------------')
print('Nodes ALL should be dictionary: %s' % type(my_graph.node))
print('Nodes ALL should be dictionary: %s' % type(my_graph.node.data))
print('NODE ... ALL should be dictionary: %s' % (my_graph.node))
print('-----------------')
print('List with DATA: %s' % list(my_graph.nodes.data()))




# Works
nx.draw_circular(my_graph, with_labels=True)
#nx.draw_kamada_kawai(my_graph, with_labels=True)
plt.show()

#my_tree = etree.ElementTree(tree)
#soup = BeautifulSoup(tree, 'lxml')
#lxml
# for node in tree.iter('*'):
#     print(node.tag)

