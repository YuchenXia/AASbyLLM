import openai
from dotenv import load_dotenv
import os
from status_logger import status_logger
# import local_models

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
gpt_call_count = 0


def gpt_model_call(prompt, model='gpt-3.5-turbo-instruct'):
    # model_config = {
    #     'gpt-3.5-turbo-instruct': ("gpt-3.5-turbo-instruct", 2700),
    #     'Llama_2_70B_HF': ('meta-llama/Llama-2-70b-hf', 2000),
    #     'Mixtral_8x7B_Instruct': ("mistralai/Mixtral-8x7B-Instruct-v0.1", 4048),
    #     'WizardLM_70B': ("WizardLM/WizardLM-70B-V1.0", 2000)
    # }

    model_config = {
        'gpt-3.5-turbo-instruct': ("gpt-3.5-turbo-instruct", 2700),
        'Llama_2_70B_HF': ('meta-llama/Llama-2-70b-hf', 2000),
        'Mixtral_8x7B_Instruct': ("mistralai/Mixtral-8x7B-Instruct-v0.1", 4048),
        'WizardCoder-Python-34B-V1.0': ("WizardLM/WizardCoder-Python-34B-V1.0", 2000)
    }
    model_name, max_tokens = model_config.get(model)

    global gpt_call_count
    gpt_call_count += 1

    status_logger.log(f"  start GPT generation, count #{gpt_call_count}")

    if model in ['gpt-3.5-turbo-instruct']:
        model_response = openai.Completion.create(
            engine=model_name,
            prompt=prompt,
            temperature=0,
            max_tokens=max_tokens
        )
        model_output = model_response.choices[0].text.strip()

    ## The local_models module is not available in this released version of the code, because it is too large to be included in the repository.
    # else:
    #     model_response = local_models.Complete.create(
    #         prompt=prompt,
    #         model=model_name,
    #         max_tokens=max_tokens,
    #         temperature=0,
    #         stop=["\n\n"]
    #     )
    #     model_output = model_response['output']['choices'][0]['text'].strip()
    #

    status_logger.log(f"  GPT generation finished, count #{gpt_call_count}")
    return model_output
