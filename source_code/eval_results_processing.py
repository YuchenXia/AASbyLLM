import json
import pandas as pd
import os

json_data = json.load(open("human_eval_results/evaluation_results_t1_gpt-3.5-turbo-instruct_rag.json", "r"))

case = "t1_gpt-3.5-turbo-instruct_rag"


def process_json_data(json_data, json_file):
    processed_data = []

    for item in json_data:
        semantic_node = item["SemanticNode"]
        name = semantic_node.get("Name", "")
        value = semantic_node.get("Value", "")
        affordance = item["Annotations"].get("Affordance", "")

        generated_annotation = item["Annotations"].get("GeneratedAnnotation", {}).get("Name", "")+": "+str(item["Annotations"].get("GeneratedAnnotation", {}).get("Definition", ""))

        relevant_evaluated_annotations = []
        relevant_annotations_count = 0
        for annotation in item["Annotations"].get("EvaluatedAnnotations", []):
            if annotation["isRelevant"]:
                relevant_evaluated_annotations.append({
                    "Name": annotation.get("Name", ""),
                    "Definition": annotation.get("Definition", ""),
                    "SemanticIdentifier": annotation.get("SemanticIdentifier", "")
                })
                relevant_annotations_count += 1

        user_rating = item["UserRating"]
        user_rating_transformed = {k: v for k, v in user_rating.items() if k != "isInaccurate"}
        inaccuracies = user_rating.get("isInaccurate", [])
        inaccurate_dict = {
            "Name_inaccurate": "Name" in inaccuracies,
            "Value_inaccurate": "Value" in inaccuracies,
            "GeneratedDefinition_inaccurate": "GeneratedDefinition" in inaccuracies,
            "Affordance_inaccurate": "Affordance" in inaccuracies,
            "Unit_inaccurate": "Unit" in inaccuracies
        }

        processed_item = {
            "source": json_file,
            "SemanticNode_Name": name,
            "SemanticNode_Value": value,
            "Affordance": affordance,
            "GeneratedAnnotation": generated_annotation,
            "EvaluatedAnnotations_relevant": relevant_evaluated_annotations,
            "EvaluatedAnnotation_relevant_number": relevant_annotations_count,
            **user_rating_transformed,
            **inaccurate_dict  # 直接展开 isInaccurate 的键值对
        }
        processed_data.append(processed_item)

    return processed_data


if __name__ == "__main__":
    sheet_names = [ "gpt-3.5-turbo-instruct_rag", "Llama_2_70B_HF", "Llama_2_70B_HF_rag", "Mixtral_8x7B_Instruct", "Mixtral_8x7B_Instruct_rag", "WizardLM_70B", "WizardLM_70B_rag"]
    for sheet_name in sheet_names:

        json_dir = "human_eval_results"
        json_files = [f for f in os.listdir(json_dir) if f.endswith(sheet_name+".json")]

        all_processed_data = []
        for json_file in json_files:
            json_path = os.path.join(json_dir, json_file)
            json_data = json.load(open(json_path, "r"))
            print(f"Processing {json_file}...")
            processed_json_data = process_json_data(json_data, json_file)
            all_processed_data.extend(processed_json_data)

        df = pd.DataFrame(all_processed_data)

        df['EvaluatedAnnotations_relevant'] = df['EvaluatedAnnotations_relevant'].apply(lambda x: json.dumps(x))

        with pd.ExcelWriter("all_results_corr.xlsx", engine="openpyxl", mode='a') as writer:
            df.to_excel(writer, index=False, sheet_name=sheet_name)
