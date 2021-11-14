# This is a sample Python script.
from owlready2 import *


class OwlCustomParser:
    def __init__(self, file_):
        print('--OwlCustomParser init--')
        self.ontology = get_ontology(f'{file_}').load()
        self.base_file = file_
        self.base_uri = self.ontology.base_iri
        self.annotation_prop = self.base_uri + "forDisplay"

    #todo
    def save_out_as(self):
        return True

    def get_classes(self):
        replacer = str(self.base_file.split('.')[0])+'.'
        # print(annotation_prop)
        query = "SELECT ?uri ?forDisplay ?parent_id  " \
            + "WHERE { ?uri a owl:Class ." \
            + "?uri rdfs:subClassOf ?parent_id ."\
            + "?uri <" + self.annotation_prop + "> ?forDisplay}"

        nodes = default_world.sparql(query)
        classes = []
        for node in nodes:

            classes.append({
                'uri': str(node[0]).replace(replacer, ''),
                'parent_id': str(node[2]).replace(replacer, ''),
                'forDisplay': str(node[1])
            })
        return classes

    def get_instances(self):
        replacer = str(self.base_file.split('.')[0]) + '.'
        query = "SELECT ?uri ?cls ?forDisplay   " \
                + "WHERE { ?uri a owl:NamedIndividual ." \
                + " ?cls a owl:Class ."\
                + "?uri rdf:type ?cls ."\
                + "?uri <" + self.annotation_prop + "> ?forDisplay}"
        instance = default_world.sparql(query)
        instances = []
        for node in instance:
            instances.append({
                'uri': str(node[0]).replace(replacer, ''),
                'parent_id': str(node[1]).replace(replacer, ''),
                'forDisplay': str(node[2])
            })

        return instances

    # Todo
    def get_data_properties(self):

        replacer = str(self.base_file.split('.')[0]) + '.'
        query = "SELECT ?uri ?parent_id ?forDisplay   " \
                + "WHERE { ?uri a owl:DatatypeProperty ." \
                + " ?cls a owl:Class ." \
                + "?uri rdf:type ?cls ." \
                + "?uri <" + self.annotation_prop + "> ?forDisplay}"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = OwlCustomParser('owlfile.owl')
    s.get_instances()

