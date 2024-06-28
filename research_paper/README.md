# The Research Paper
Details of this work has been documented in a journal paper, we paid the Open-Access-Fee to the publisher to make it open-source:

The Paper: [Generation of Asset Administration Shell With Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0](https://www.doi.org/10.1109/ACCESS.2024.3415470)

>Y. Xia, Z. Xiao, N. Jazdi and M. Weyrich, "Generation of Asset Administration Shell With Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0," in IEEE Access, doi: 10.1109/ACCESS.2024.3415470.

```bibtex
@ARTICLE{10559483,
  author={Xia, Yuchen and Xiao, Zhewen and Jazdi, Nasser and Weyrich, Michael},
  journal={IEEE Access}, 
  title={Generation of Asset Administration Shell With Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0}, 
  year={2024},
  keywords={Semantics;Data models;Digital twins;Context modeling;Interoperability;Unified modeling language;Fourth Industrial Revolution;Asset Administration Shell;Large Language Model;Semantic Interoperability;Digital Twin;Industry 4.0;Generative AI;Retrieval-Augmented Generation},
  doi={10.1109/ACCESS.2024.3415470}}
```

### Abstract
This research introduces a novel approach for achieving semantic interoperability in digital twins and assisting the creation of Asset Administration Shell (AAS) as digital twin model within the context of Industry 4.0. The foundational idea of our research is that the communication based on semantics and the generation of meaningful textual data are directly linked, and we posit that these processes are equivalent if the exchanged information can be serialized in text form. Based on this, we construct a “semantic node” data structure in our research to capture the semantic essence of textual data. Then, a system powered by large language models is designed and implemented to process the “semantic node” and generate standardized digital twin models (AAS instance models in the context of Industry 4.0) from raw textual data collected from datasheets describing technical assets. Our evaluation demonstrates an effective generation rate of 62-79%, indicating a substantial proportion of the information from the source text can be translated error-free to the target digital twin instance model with the generative capability of large language models. This result has a direct application in the context of Industry 4.0, and the designed system is implemented as a data model generation tool for reducing the manual effort in creating AAS model by automatically translating unstructured textual data into a standardized AAS model. The generated AAS model can be integrated into AAS-compliant digital twin software for seamless information exchange and communication. In our evaluation, a comparative analysis of different LLMs and an in-depth ablation study of Retrieval-Augmented Generation (RAG) mechanisms provide insights into the effectiveness of LLM systems for interpreting technical concepts and translating data. Our findings emphasize LLMs’ capability to automate AAS instance creation and contribute to the broader field of semantic interoperability for digital twins in industrial applications.

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
