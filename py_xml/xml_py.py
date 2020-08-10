import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

path_xml = "E:/corpu/"

class xml_mail():

    def __init__(self):
        self.value = 'XML'



    def get_xml():
        file_xml = "report_realisasi_sharing_2018.xml"
        tree = ET.parse(path_xml+file_xml)
        root = tree.getroot()
        return root




# main = xml_mail()

if __name__ == '__main__':
    print(xml_mail.get_xml())






