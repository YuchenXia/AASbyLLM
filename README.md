# AASbyLLM

The web-application is hosted here: [https://aasbyllmapp-v15-1-yawjvp4zbq-ew.a.run.app/](https://aasbyllmappv16-yawjvp4zbq-ew.a.run.app/)
(Note: It may take 30 seconds to 2 minutes for the elastic server system to boot up.)

# The research paper (pre-print draft)
[pre-print draft](https://github.com/YuchenXia/AASbyLLM/blob/main/research_paper/v3_Automated%20Generation%20of%20Asset%20Administration%20Shell%20with%20Large%20Language%20Model.pdf)

### Graphical abstract:
![Graphical abstract](AASbyLLM_graphical_abstract.png)

### LLM-Agent design:
![LLM-Agent design](LLM_agent_design.png)

# The Main Features of 'AASbyLLM' and Its Novel Contributions:
### Technologies:
- First research prototype applying **generative LLM** for generating AAS
- Apply generative LLMs for **inferencing** and embedding LLMs for **similarity retrieval**

### Benefits:
- Wider range of **input flexibility** and format independent, as long as the meaning of text input is understandable
- **Generally applicable** to different disciplinary domains.
- Instead of using manually crafted mapping rules, the system utilizes the knowledge learned by LLMs
- The system adds proper **semantic annotation** for disambiguating the **concepts of the data property**
- The system optimizes relevant information details during the processing and enhances the quality of AAS 

### Implications:
- This prototype demonstrates the machine capability to **semantically understand and generate data properties for industrial applications**.
- This capability can enable:
  1. an **interoperable** information exchange in the context of **digitalization**
  2. and higher degree of **task automation** in the context of **autonomization**

# Details about the prompts for the LLM agents

### The prompts have the following structure
![Prompt structure](prompt_structure.png)

### Extraction agent prompt
The prompt for extraction agent: [extraction_agent_prompt](extraction_agent_prompt.txt)

The extraction LLM agent is designed to identify and extract the name, the value, and an initial definition for a semantic node from the input text. This LLM processes the given input text and initially creates a name, definition, and contextual description for each semantic node as output, enriching the raw data with semantic details in a data structure.

### Semantic search agent
This agent does not require a prompt. Following identification and extraction, this agent performs a semantic search using an embedding LLM to find semantically similar entries in the ECLASS dictionary. The search mechanism is based on our [previous work](https://ieeexplore.ieee.org/document/9921637) , where a vectorized embedding index, called “semantic fingerprint”, is created for comparison between queried text and each ECLASS dictionary entry. The result is a list of retrieved similar definition entries from ECLASS dictionary.

### Synthesis agent prompt
The prompt for extraction agent: [synthesis_agent_prompt](synthesis_agent_prompt.txt)

This step incorporates the results from the semantic search into the generation process. An LLM-agent is prompted to generate a judgment of the relevance of the retrieved entries, accompanied by a short reason in text. The purpose of this step is two folds: firstly, semantic search is based on relationship of semantic similarity, which is a typical proxy metric for search but suboptimal for determining precise relevance. Inappropriate results shall be filtered out; Secondly, in this step, the generated judgement and reason serve as intermediate textual material for considering more nuanced relationships during the whole process. By instructing the LLM to judge and reason for each search result, the LLM generates more precise semantic node. After synthesis, a complete semantic node is created based on RAG, ready for AAS model creation.
