import os

from sentence_transformers import SentenceTransformer, util
import pandas
import numpy
from llm import gpt_model_call
import json
import copy
import random
from status_logger import status_logger

class SemanticNodeExtractionAgent:
    def __init__(self):
        self.prompt_template = """Role and goal:
You are a data extractor for identifying the semantic nodes from the input text. A semantic node is defined as a structured unit that captures the essential semantics of a piece of information, describing a property of an entity. Your goal is to produce a list of these semantic nodes from the given texts. Take into account the provided context, instructions, and examples in the following sections. Following these, you will generate key-value pairs.

Context:
The input data may come from data sheets, data tables, database export files, crawled data from the internet, or other sources.
A semantic node has the following fields:
1. Name: A concise and specific title assigned to the semantic node. It should be concise yet descriptive enough to convey the essence of the meaning at a glance.
2. Definition: A definition of what the semantic node represents.
3. Value: The actual data that is described by the semantic node.
4. SourceDescription: An explanation that specify where the semantic node come from, situating the semantic node in the specific context of its source and input text.

Instructions:
As an information extractor, please extract the semantic nodes into a list based on the input information.
You need to determine how many semantic nodes should be generated.
Follow the structure and syntax as shown in the JSON file in the example section.
The output should be in a JSON data structure format.

Example:
Input: 
// you will receive texts here

Output: 
{
  "SemanticNodes": [
    {
      "Name": "Name_1",
      "Definition": "Definition_1",
      "Value": "Value_1",
      "SourceDescription": "SourceDescription_1"
    },
    {
      "Name": "Name_2",
      "Definition": "Definition_2",
      "Value": "Value_2",
      "SourceDescription": "SourceDescription_2"
    }
  ]
}
Input: {{input_text}}
Output: 
"""
        status_logger.log("semantic node extraction agent initialized")

    def generate_output(self, input_text, model):
        status_logger.log("semantic node extraction agent started analysis")
        self.prompt = self.prompt_template.replace("{{input_text}}", input_text)

        try:
            # Get the text output from the GPT model call
            text_output = gpt_model_call(self.prompt, model=model)
        except Exception as e:
            # Handle exceptions that might occur during the GPT model call
            # status_logger.log(f"Error during GPT model call: {e}")
            status_logger.log(f"Error during GPT model call")
            return None

        try:
            # Parse the text output into a JSON object
            semantic_nodes = json.loads(text_output)
        except json.JSONDecodeError as json_err:
            # Handle JSON parsing errors
            status_logger.log(f"JSON decoding error: {json_err}")
            status_logger.log(f"Received text output: {text_output}")
            return None

        # Write the JSON data to a file
        with open('semantic_nodes_indentified.json', 'w') as file:
            json.dump(semantic_nodes, file, indent=4)
        status_logger.log("semantic node extraction agent finished generation")
        status_logger.log(f"semantic node extraction agent output: {semantic_nodes}")
        return semantic_nodes

class SemanticSearchAgent:
    def __init__(self):
        self.dictionary = pandas.read_csv('ECLASS_PR_encoded.csv', sep=',')
        self.properties_vector_float = numpy.load('ECLASS_PR_encoded.npy')
        self.properties_definition = self.dictionary['Definition'].tolist()
        self.properties_IdPR = self.dictionary['IdPR'].tolist()
        self.properties_name = self.dictionary['PreferredName'].tolist()
        self.model = SentenceTransformer('all-distilroberta-v1')
        status_logger.log("semantic search agent initialized")


    def search_from_dictionary(self, search_query, top_hits=5):
        self.results = []
        query_vec = self.model.encode(search_query)
        score_list = [float(util.dot_score(query_vec, v)) for v in self.properties_vector_float]
        top_indexes = numpy.argsort(score_list)[::-1][:top_hits]

        # store the results in a list of tuples
        for idx in top_indexes[:top_hits]:
            self.results.append((self.properties_name[idx], self.properties_definition[idx], self.properties_IdPR[idx]))
        return self.results

    def generate_semantic_nodes_with_similar_annotations(self, semantic_nodes, top_hits=5):
        status_logger.log("semantic search agent started retrieval process")
        semantic_nodes_with_similar_annotation = copy.deepcopy(semantic_nodes)  # To avoid modifying the original input

        for semantic_node in semantic_nodes_with_similar_annotation["SemanticNodes"]:
            # Concatenate Name, Definition, and SourceDescription
            concatenated_text = semantic_node["Name"] + " " + semantic_node["Definition"] + " " + semantic_node[
                "SourceDescription"]

            # Use SemanticSearchAgent to find top x similar entries
            similar_entries = self.search_from_dictionary(concatenated_text, top_hits)

            # Format similar entries and add them to the semantic node
            semantic_node["SimilarAnnotations"] = [{
                "Name": entry[0],
                "Definition": entry[1],
                "SemanticIdentifier": entry[2]
            } for entry in similar_entries]
        with open('semantic_nodes_with_similar_annotation.json', 'w') as file:
            json.dump(semantic_nodes_with_similar_annotation, file, indent=4)
        status_logger.log("semantic search agent finished retrieval")
        status_logger.log(f"semantic search agent output: {semantic_nodes_with_similar_annotation}")
        return semantic_nodes_with_similar_annotation

class AnnotationEvaluationAgent:
    def __init__(self):
        self.prompt_template = """Role and goal:
You are an evaluator for assessing the relevance of provided annotations to the original texts. Your goal is to determine if each annotation is applicable to the semantic node extracted from the text, and provide a reason for your judgment.

Context:
You will receive some original texts, a data property extracted from the texts, and some annotations for this data property.
The list of annotations is retrieved based merely on similarity, but these annotations are not necessarily correct and related.
The data property is either a general information or a technical property. 
A general information refers to the basic details about a product that would identify and describe it without getting into the detailed technical specifications, for example, product name, manufacturer name, ordering number, product type, etc.
A technical property refers to a characteristic or attribute that defines or describes the technical aspects of an object, system, material, or process. These properties are usually measurable or quantifiable and are critical in determining how something will function or perform in a specific context.
Affordance refers to the possible specific applications or specific engineering tasks where this information can be used.

Instructions:
Please determine whether each given annotation is relevant to annotate the semantic node without contradictions and give a reason for your decision in one sentence.
After that, you decide the most relevant annotation out of the given annotation list as the best annotation.
Then, you generate your own annotation based on your reasons.
Then, you determine the unit of the data property. If it has no unit, fill the value of unit with "-".
Then, you classify the annotated data property as general information or a technical property using the "ClassifyingScore_GeneralOrTechnical" score from 1 to 5. A score of 1 indicates it is primarily general information, while a score of 5 indicates it is primarily a technical property.
Finally, you generate the affordance of the information, mentioning the possible specific applications or engineering tasks where this information can be used concisely within one sentence. 

Example:
Input:
The original text is: //original text
The semantic node extracted from the text is: //semantic node
The list of annotations is: //list of annotations
Output:
{
    "EvaluatedAnnotations": [
        {
            "Name": "Name_1",
            "Definition": "Definition_1",
            "Reason": "Reason_1",
            "isRelevant": true,
            "SemanticIdentifier": "the_given_semantic_identifier_1"
        },
        {
            "Name": "Name_2",
            "Definition": "Definition_2",
            "Reason": "Reason_2",
            "isRelevant": false,
            "SemanticIdentifier": "the_given_semantic_identifier_2"
        }
    ],
    "BestAnnotation": {
        "Name": "Name_x",
        "Definition": "Definition_x",
        "SemanticIdentifier": "the_given_semantic_identifier_x"
    },
    "GeneratedAnnotation": {
        "Name": "Name_new",
        "Definition": "Definition_new",
        "SemanticIdentifier": null
    },
    "Unit": "Unit_of_the_data_property",
    "ClassifyingScore_GeneralOrTechnical": 3,
    "Affordance": "Affordance_in_one_sentence"
}

Input:
The original text is: {{input_text}}
The semantic node extracted from the text is: {{semantic_node}}
The list of annotations is: {{list_of_annotations}}
Output:
"""
        self.prompt_template_no_external_library = """Role and goal:
You are an annotator to annotate a data property. Your goal is to generate a name and a definition for the data property.

Context:
You will receive some original texts, a data property extracted from the texts for this data property.
The data property is either a general information or a technical property. 
A general information refers to the basic details about a product that would identify and describe it without getting into the detailed technical specifications, for example, product name, manufacturer name, ordering number, product type, etc.
A technical property refers to a characteristic or attribute that defines or describes the technical aspects of an object, system, material, or process. These properties are usually measurable or quantifiable and are critical in determining how something will function or perform in a specific context.
Affordance refers to the possible specific applications or specific engineering tasks where this information can be used.

Instructions:
Please generate a name and a definition explaining the technical property.
Then, you determine the unit of the data property. If it has no unit, fill the value of unit with "-".
Then, you classify the annotated data property as general information or a technical property using the "ClassifyingScore_GeneralOrTechnical" score from 1 to 5. A score of 1 indicates it is primarily general information, while a score of 5 indicates it is primarily a technical property.
Finally, you generate the affordance of the information, mentioning the possible specific applications or specific engineering tasks where this information can be used concisely within one sentence. 

Example:
Input:
The original text is: //original text
The data property extracted from the text is: //data property
Output:
{
    "GeneratedAnnotation": {
        "Name": "Name_new",
        "Definition": "Definition_new",
        "SemanticIdentifier": null
    },
    "Unit": "Unit_of_the_data_property",
    "ClassifyingScore_GeneralOrTechnical": 3,
    "Affordance": "Affordance_in_one_sentence"
}

Input:
The original text is: {{input_text}}
The data property extracted from the text is: {{semantic_node}}
Output:
"""
        status_logger.log("annotation evaluation agent initialized")

    def evaluate_annotations(self, original_text, semantic_nodes_with_similar_annotation, model, use_external_library=True):
        status_logger.log("annotation evaluation agent started evaluation")
        evaluated_annotations_all = []
        for df in semantic_nodes_with_similar_annotation["SemanticNodes"]:
            # Extracting the semantic_node
            semantic_node = {
                "Name": df["Name"],
                "Definition": df["Definition"],
                "Value": df["Value"],
                "SourceDescription": df["SourceDescription"]
            }
            status_logger.log(f"Processing semantic node: \"{semantic_node['Name']}\"")
            # Format the prompt for each semantic node
            if use_external_library:
                list_of_annotations = df["SimilarAnnotations"]
                formatted_prompt = self.prompt_template.replace("{{input_text}}", original_text) \
                    .replace("{{semantic_node}}", json.dumps(semantic_node)) \
                    .replace("{{list_of_annotations}}", json.dumps(list_of_annotations))
            else:
                formatted_prompt = self.prompt_template_no_external_library.replace("{{input_text}}", original_text) \
                    .replace("{{semantic_node}}", json.dumps(semantic_node))
            try:
                # Get the output from the GPT model call for each semantic node
                evaluation_result = gpt_model_call(formatted_prompt, model=model)
            except Exception as e:
                status_logger.log(f"Error during GPT model call for {semantic_node['Name']}: {e}")
                continue

            try:
                # Parse the output from the GPT model for each semantic node
                evaluated_annotations = json.loads(evaluation_result)
                if use_external_library == False:
                    evaluated_annotations["EvaluatedAnnotations"] = [{
                            "Name": None,
                            "Definition": None,
                            "Reason": "not using external library",
                            "isRelevant": False,
                            "SemanticIdentifier": None
                    }]
                    evaluated_annotations["BestAnnotation"] = [{
                        "Name": "[Not using external library]",
                        "Definition": None,
                        "Reason": "not using external library",
                        "isRelevant": False,
                        "SemanticIdentifier": None
                    }]
                evaluated_annotations_all.append({
                    "SemanticNode": semantic_node,
                    "Annotations": evaluated_annotations
                })
            except json.JSONDecodeError as json_err:
                status_logger.log(f"JSON decoding error for {semantic_node['Name']}: {json_err}")
                status_logger.log(f"Received text output: {evaluation_result}")

        with open('evaluated_annotations.json', 'w') as file:
            json.dump(evaluated_annotations_all, file, indent=4)
        status_logger.log("annotation evaluation agent finished evaluation")
        return evaluated_annotations_all

class SynthesisAgent:
    def __init__(self):
        self.prompt_template = """GeneratedBetterThanBest": true, DefinitionCreated: """
        status_logger.log("synthesis agent initialized")

    def generate_property_list(self, evaluated_annotations):
        status_logger.log("synthesis agent started synthesis of the intermediate results")
        property_list = []
        for item in evaluated_annotations:
            semantic_node = item["SemanticNode"]
            annotations = item["Annotations"]
            unique_id = '_'.join(f"{random.randint(0, 9999):04}" for _ in range(4))
            cd_iri = f"https://github.com/YuchenXia/AASbyLLM/tree/main/AAS_Samples/ids/cd/{unique_id}"  # TODO: avoid unique id collision (but not of high priority in this prototype. For 10,000,000 generated IDs less than 0.5%)
            is_technical = annotations["ClassifyingScore_GeneralOrTechnical"] > 3  # 5 tendency to technical, 1 general
            property_list.append({
                "P_idShort": semantic_node["Name"],
                "P_description": annotations["GeneratedAnnotation"]["Definition"],
                "P_value": semantic_node.get("Value", ""),
                "P_semanticIdGlobalReference": cd_iri,
                "CD_idShort": semantic_node["Name"],
                "CD_id": cd_iri,
                "CD_description": annotations["GeneratedAnnotation"]["Definition"],
                "CD_preferredName_IEC61360": annotations["GeneratedAnnotation"]["Name"],
                "CD_dataType_IEC61360": "STRING",
                "CD_unit_IEC61360": "",
                "CD_definition_IEC61360": annotations["GeneratedAnnotation"]["Definition"],
                "CD_sourceOfDefinition_IEC61360": "generated by AI software AASbyLLM based on user given texts.",
                "unit": annotations["Unit"],
                "is_technical": is_technical,
                "affordance": annotations["Affordance"]
            })

        with open('synthesized_property_list.json', 'w') as file:
            json.dump(property_list, file, indent=4)
        status_logger.log("synthesis agent finished synthesis")
        return property_list

class AASDataFormation:
    def __init__(self, property_list):
        self.property_list = property_list
        self.aas_template = json.load(open('AAS_template.json'))
        status_logger.log("AAS data formation agent initialized")

    def generate_properties_and_concept_descriptions(self, filename):
        # Process each property from the property list
        status_logger.log("AAS model formation agent started AAS creation")
        for prop in self.property_list:
            a_new_concept_description = {
                "idShort": prop["CD_idShort"],
                "description": [
                    {
                        "language": "en",
                        "text": prop["CD_description"]
                    }
                ],
                "id": prop["CD_id"],
                "embeddedDataSpecifications": [
                    {
                        "dataSpecification": {
                            "type": "ExternalReference",
                            "keys": [
                                {
                                    "type": "GlobalReference",
                                    "value": "http://admin-shell.io/DataSpecificationTemplates/DataSpecificationIEC61360/3/0"
                                }
                            ]
                        },
                        "dataSpecificationContent": {
                            "preferredName": [
                                {
                                    "language": "en",
                                    "text": prop["CD_preferredName_IEC61360"]
                                }
                            ],
                            "unit": prop["CD_unit_IEC61360"],
                            "sourceOfDefinition": prop["CD_sourceOfDefinition_IEC61360"],
                            "dataType": prop["CD_dataType_IEC61360"],
                            "definition": [
                                {
                                    "language": "en",
                                    "text": prop["CD_definition_IEC61360"]
                                }
                            ],
                            "modelType": "DataSpecificationIec61360"
                        }
                    }
                ],
                "modelType": "ConceptDescription"
            }
            self.aas_template["conceptDescriptions"].append(a_new_concept_description)

            # Add the new property to the AAS template
            a_new_property = {
                "idShort": prop["P_idShort"],
                "description": [
                    {
                        "language": "en",
                        "text": prop["P_description"]
                    }
                ],
                "semanticId": {
                    "type": "ExternalReference",
                    "keys": [
                        {
                            "type": "GlobalReference",
                            "value": prop["P_semanticIdGlobalReference"]
                        }
                    ]
                },
                "valueType": "xs:string",  # Assuming the data type in CD_dataType is compatible
                "value": prop["P_value"],
                "modelType": "Property"
            }
            if prop["is_technical"]:
                self.aas_template["submodels"][0]["submodelElements"][1]["value"].append(a_new_property)
            else:
                self.aas_template["submodels"][0]["submodelElements"][0]["value"].append(a_new_property)

        aas_file_path = os.path.join('aas_files', f'{filename}')
        with open(aas_file_path, 'w') as file:
            json.dump(self.aas_template, file, indent=4)
        status_logger.log("AAS data formation agent finished formation")
        return self.aas_template


if __name__ == "__main__":

    extraction_agent = SemanticNodeExtractionAgent()

    input_text= """
Product name
Vacuum and Pressure Sensors

Type
VS-V-SA ST

Weight [g]   
5

Max. overpressure safety [bar]
5
"""
    input_text_1  = """
    Product name
    Vacuum and Pressure Sensors

    Type
    VS-V-SA ST

    Part no.
    10.06.02.00226

    Measured medium
    Non-aggressive gases; dry, oil-free air

    Measuring range [bar] 
    -1,00 ... 0,00 bar

    Max. overpressure safety [bar]
    5

    Inputs/outputs
    Analog: 1...5 V

    Repeatability
    ± 1% of full-scale value

    Electrical connection
    Cable

    Voltage 
    10-24V DC

    Protection type IP
    IP 40

    Temperature influence 
    ± 3% of full-scale value

    Operating temperature [°C]
    0 ... 50 °C

    Length of cable Lk [m] 
    3

    Weight [g]   
    5
    """
    semantic_nodes = extraction_agent.generate_output(input_text)
    search_agent = SemanticSearchAgent()
    semantic_nodes_with_similar_annotation = search_agent.generate_semantic_nodes_with_similar_annotations(
        semantic_nodes)
    evaluation_agent = AnnotationEvaluationAgent()
    evaluated_annotations = evaluation_agent.evaluate_annotations(input_text, semantic_nodes_with_similar_annotation)

    synthesis_agent = SynthesisAgent()
    property_list = synthesis_agent.generate_property_list(evaluated_annotations)
    print(property_list)

    aas_data_formation = AASDataFormation(property_list)
    aas_data_formation.generate_properties_and_concept_descriptions()
