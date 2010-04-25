from  author_net_functions import *

#perform a dummy search to show how to make the author networks
my_terms="multivariate meta-analysis AND Stat Med[so]"
my_xml_file = "meta.xml"
my_graph_file = "meta.dot"
download_from_pubmed(my_terms, my_xml_file, 2000)

parsed_xml = parse_pubmed_xml(my_xml_file)
author_network(parsed_xml[0], parsed_xml[1], my_graph_file)

