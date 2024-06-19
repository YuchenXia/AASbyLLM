from agents import *
from flask import Flask, render_template, request, jsonify, send_file
from datetime import datetime
from dotenv import load_dotenv
from flask_cors import CORS
from status_logger import status_logger
from secrets import token_hex
import os


app = Flask(__name__)
CORS(app)

load_dotenv()

extraction_agent = SemanticNodeExtractionAgent()
# search_agent = SemanticSearchAgent()
evaluation_agent = AnnotationEvaluationAgent()
synthesis_agent = SynthesisAgent()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_aas():
    data = request.json
    input_text = data['textInput']
    selected_model = data.get('model')
    use_external_library = data.get('useExternalLibrary')
    active_example_button = data.get('activeExampleButton')
    status_logger.log("Beginning AAS generation...")
    status_logger.log(f"using model: {selected_model}")
    status_logger.log(f"use external library : {use_external_library}")

    semantic_nodes = extraction_agent.generate_output(input_text, model=selected_model)
    number_of_semantic_nodes = len(semantic_nodes['SemanticNodes'])
    status_logger.log(f"{number_of_semantic_nodes} semantic nodes extracted, continuing...")
    if(use_external_library):
        semantic_nodes_with_similar_annotation = search_agent.generate_semantic_nodes_with_similar_annotations(semantic_nodes)
        evaluated_annotations = evaluation_agent.evaluate_annotations(input_text, semantic_nodes_with_similar_annotation, model=selected_model, use_external_library=use_external_library)
    else:
        evaluated_annotations = evaluation_agent.evaluate_annotations(input_text, semantic_nodes, model=selected_model, use_external_library=use_external_library)
    property_list = synthesis_agent.generate_property_list(evaluated_annotations)
    results_for_human_validation = evaluated_annotations

    current_time_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    ramdom_hex = token_hex(2)
    if use_external_library:
        session_key = f'{active_example_button}_{selected_model}_rag_{current_time_str}_{ramdom_hex}'
    else:
        session_key = f'{active_example_button}_{selected_model}_{current_time_str}_{ramdom_hex}'
    filename = f'aas_file_{session_key}.json'
    aas_data_formation = AASDataFormation(property_list)
    aas = aas_data_formation.generate_properties_and_concept_descriptions(filename=filename)
    response_data = {
        "session_key": session_key,
        "aas": aas,
        "resultsForHumanEvaluation": results_for_human_validation
    }

    with open(f'sent_data\\{session_key}.json', 'w') as f:
        json.dump(response_data, f, indent=4)
    return jsonify(response_data)


@app.route('/submitRatings/<session_key>', methods=['POST'])
def handle_submit_ratings(session_key):
    status_logger.log("User Ratings Received.")
    file_path = os.path.join('sent_data', f'{session_key}.json')
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        session_data = json.load(file)
    results_for_human_evaluation = session_data['resultsForHumanEvaluation']
    ratings = request.json['ratingsData']
    for rating_data in ratings:
        index = int(rating_data['index'])
        userConfused = rating_data['userConfused']
        impKnowledge = rating_data['impKnowledge']
        if userConfused == "0":
            impKnowledge = "0"
        overall = rating_data['overall']
        definition = rating_data['definition']
        affordance = rating_data['affordance']
        isInaccurateList = rating_data['isInaccurate']

        if 0 <= index < len(results_for_human_evaluation):
            results_for_human_evaluation[index]['UserRating'] = {
                "userConfused": userConfused,
                "impKnowledge": impKnowledge,
                "overall": overall,
                "definition": definition,
                "affordance": affordance,
                "isInaccurate": isInaccurateList
            }

    evaluation_results = results_for_human_evaluation
    filename = f'evaluation_results_{session_key}'
    file_path_name = os.path.join('evaluation_results', f'{filename}.json')
    with open(file_path_name, 'w') as f:
        json.dump(evaluation_results, f, indent=4)
    status_logger.log("Evaluation results recorded: " + filename)
    return jsonify({"evaluationFileName": filename})


@app.route('/download-aas/<filename>', methods=['GET'])
def download_aas(filename):
    aas_file_path = os.path.join('aas_files', f'{filename}.json')
    return send_file(aas_file_path, as_attachment=True)

@app.route('/status', methods=['GET'])
def get_status():
    logs = status_logger.get_logs()
    return jsonify(logs)

@app.route('/download-evaluation/<filename>', methods=['GET'])
def download_evaluation(filename):
    file_path = os.path.join('evaluation_results', f'{filename}.json')
    return send_file(file_path, as_attachment=True)


# Evaluation app
@app.route('/eval')
def eval_index():
    return render_template('eval.html')


@app.route('/eval/case', methods=['POST'])
def eval_case():
    data = request.get_json()
    value = data.get('value')
    model = data.get('model')
    if data.get('rag') == "true":
        file_path = os.path.join('eval_samples', f'{value}_{model}_rag.json')
    else:
        file_path = os.path.join('eval_samples', f'{value}_{model}.json')
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        response_data = json.load(file)
    response_data['numberOfSemanticNodes'] = len(response_data['resultsForHumanEvaluation'])
    return jsonify(response_data)

@app.route('/downloadSamplePDF/<string:pdf_id>', methods=['GET'])
def download_sample_pdf(pdf_id):
    file_name = f'{pdf_id}.pdf'
    file_path = f'pdfs/{file_name}'
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
