# This is a sample Python script.
from owlready2 import *


class OwlCustomParser:
    def __init__(self, file_):
        print('--OwlCustomParser init--')
        self.ontology = get_ontology(f'{file_}').load()
        self.base_file = file_
        self.base_uri = self.ontology.base_iri

    def save_out_as(self):
        return True

    def get_classes(self):
        replacer = str(self.base_file.split('.')[0])+'.'
        annotation_prop =self.base_uri+"forDisplay"
        # print(annotation_prop)
        query = "SELECT ?uri ?forDisplay ?parent_id  " \
            + "WHERE { ?uri a owl:Class ." \
            + "?uri rdfs:subClassOf ?parent_id ."\
            + "?uri <" + annotation_prop + "> ?forDisplay}"

        nodes = default_world.sparql(query)
        classes = []
        for node in nodes:

            classes.append({
                'uri': str(node[0]).replace(replacer, ''),
                'parent_id': str(node[2]).replace(replacer, ''),
                'forDisplay': str(node[1])
            })
        print(classes)

    def get_instances(self):

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = OwlCustomParser('owlfile.owl')
    s.get_classes()

