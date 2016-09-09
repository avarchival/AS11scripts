"""Work in progress"""

import os
import sys
import subprocess
from glob import glob
from lxml import etree
from subprocess import call

starting_dir = sys.argv[1]



for dirpath, dirnames, filenames in os.walk(starting_dir):
    for filename in [f for f in filenames if f.endswith(".mxf")]:
        full_path = os.path.join(dirpath, filename)
        mediainfo_xml = subprocess.check_output(['mediainfo', '--Output=XML', '-f', full_path])
        
        file_no_path = os.path.basename(full_path)
        file_no_extension = os.path.splitext(os.path.basename(file_no_path))[0]
        xml_file = file_no_extension + '.xml'
        full_xml_path = os.path.join(dirpath,xml_file)
        
        xml_parse = etree.parse(full_xml_path) 
        xml_namespace = xml_parse.xpath('namespace-uri(.)') 


