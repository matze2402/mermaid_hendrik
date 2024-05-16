# import logging
import pandas as pd
import yaml
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.yamlutils import as_yaml
from linkml_runtime.linkml_model.meta import ClassDefinition
from linkml.generators.pythongen import PythonGenerator
from linkml.generators.shaclgen import ShaclGenerator
from linkml.generators.yumlgen import YumlGenerator
import yaml
# from LinkML_template_of_DCATap import Container

"""
Please let this script rn twice, because the first time it will create the file personinfo_tut_7.py, which is needed for the second run.
You will therefore need to delete the commenting marks in the second run.
So the last import statement above should be uncommented and the last six lines should be uncommented in the second run.
"""

with open("LinkML_template_for_DCATap_20240417.yaml") as file:
    data = file.read()

gen_ser = PythonGenerator(data).serialize()
gen_yuml_ser = YumlGenerator(data).serialize()
gen_shacl_ser = ShaclGenerator(data).serialize()

with open("LinkML_template_of_DCATap_20240417.py", 'w') as outfile:
    outfile.write(gen_ser)

with open("LinkML_template_for_DCATap_20240417.shacl.ttl", 'w') as outfile:
    outfile.write(gen_shacl_ser)


