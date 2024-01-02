# The main features of this work (AASbyLLM) and the novelties:
Technologies:
- First research prototype applying **generative LLM** for generating AAS
- Apply generative LLM for **inferencing** and embedding LLM for **similarity retrieval**

Benefits:
- Wider range of **input flexibility** and format independent
- **Generally applicable** to different disciplinary domains.
- Instead of using manually crafted mapping rules, the system utilizes the knowledge learned in LLMs
- The system adds proper **semantic annotation** for disambiguating the **concepts of the data property**
- The system optimizes relevant details to enhances the quality of AAS 

Implications:
- This prototype demonstrates the machine capability to **semantically understand and generate data properties**.
- This capability can enable:
  1) an **interoperable** information exchange in the context of **digitalization**
  2) and higher degree of **task automation** in the context of **autonomization**

# List of Related Works

## NLP:
These works apply embedding language models in NLP for information processing:
### 1. Automated monitoring applications for existing buildings through natural language processing based semantic mapping of operational data and creation of digital twins
- **Summary**: This paper focuses on creating automated technical monitoring applications for existing buildings using NLP to semantically map operational data and form digital twins. It tackles the challenge of integrating semantically heterogeneous operational data into monitoring applications, traditionally a manual effort-intensive process. The method uses AI to map this data to a standard, creating semantic digital twins of buildings, achieving over 95% effectiveness in automating data point mapping.
- **Authors**:
- **DOI**:


### 2. Comparison of Different NLP Models for Semantic Interoperability of Heterogeneous Asset Administration Shells
- **Summary**: The paper explores different natural language processing (NLP) embedding models to achieve semantic interoperability in heterogeneous AAS. It focuses on extending the Industrie 4.0 approach to heterogeneous semantics by automating the mapping of varied vocabularies to target semantics using NLP models. The paper compares existing embedding models, evaluates their mapping accuracy, and discusses the integration of structured knowledge via knowledge graphs. It shows that fine-tuning existing models to the target vocabulary based on the ECLASS standard significantly improves mapping accuracy.
- **Authors**:
- **DOI**:


### 3. Automated generation of Asset Administration Shell: a transfer learning approach with neural language model and semantic fingerprints
- **Summary**: Proposes a transfer learning approach with a neural language model to map data properties from various information models into a standardized AAS model. It involves generating "semantic fingerprints," vectors containing latent conceptual meaning, which aid in creating AAS with reduced development effort.
- **Authors**:
- **DOI**:


### 4. Interoperability of Semantically Heterogeneous Digital Twins through NLP Methods
- **Summary**: This method improves interactions between Asset Administration Shells by mapping heterogeneous descriptions to a standardized semantic language. It involves an automated matching process using trained embedding models on domain-specific texts for mapping.
- **Authors**:
- **DOI**:


### 5. Automatisierte Abbildung Semantisch Heterogener I4.0-Verwaltungsschalen
- **Summary**: The paper discusses automating semantic matching for interoperability between heterogeneous AAS, achieved through automated mapping of unknown vocabularies to a target ontology using NLP methods. It combines ISO standards pre-trained language models with sentence embeddings for this purpose.
- **Authors**:
- **DOI**:


## Rule-based:
These papers apply model transfromation and rule-based mappings, mainly utilizing the model-based(/-driven) software engineering (MBSE/MDSE) pattern or semantic web technologies.
### 6. Model Transformation for Asset Administration Shells
- **Summary**: The authors propose a custom-built Model Transformation Language (MTL) for Asset Administration Shells -- AASMTL-- focusing on its designed abstract syntax and language semantics. The MTL, based on a simplified version of the Object Constraint Language (OCL), is tailored to transform information across various AAS submodels.
- **Authors**:
- **DOI**:

### 7. Interoperable Digital Twins in IIoT Systems by Transformation of Information Models: A Case Study with Asset Administration Shell
- **Summary**: The paper presents a system enabling interoperable digital twins in IIoT by transforming information models into AAS format. This process involves a detailed mapping model that dictates the conversion rules from source formats (like ABB Ability™ digital twins) to the AAS format.
- **Authors**:
- **DOI**:

### 8. A Semi-Automatic Approach for Asset Administration Shell Creation from Heterogeneous Data
- **Summary**: The paper introduces a semi-automatic approach for AAS creation with a python implementation. It involves extracting engineering information from various document types (PDF, STP, XML, XML/AML, RDF) , then mapping this information to the AAS meta-model. This process creates individual AASs for each document, which are later integrated into a comprehensive AAS representing the asset.
- **Authors**:
- **DOI**:

### 9. Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies
- **Summary**: a bidirectional mapping approach that allows to transform between a model represented with the AAS submodels and a model represented with the skill ontology called CaSkMan
- **Authors**:
- **DOI**:


### 10. File- and API-based interoperability of digital twins by model transformation: An IIoT case study using asset administration shell
- **Summary**: The method for creating the AAS involves a customizable transformation system. This system enables engineers to define transformation rules flexibly and apply them to source and target systems. 
- **Authors**:
- **DOI**:

### 11. Enabling semantic interoperability of asset administration shells through an ontology-based modeling method
- **Summary**: The paper describes a method for creating AAS using the Ontology Modeling Language (OML) to map AAS models to an ontology-compatible format (OWL). This involves selecting relevant MaRCO ontology concepts and integrating them into the OML vocabulary. The OML Adapter is then used to create a Unified Modeling Language (UML) profile from these OML files. The resulting MaRCO UML profile is applied to the AAS models as stereotypes, allowing the designer to refine them with specific properties. This process enables the conversion of AAS classes into OWL individuals, ensuring semantic interoperability.
- **Authors**:
- **DOI**:

### 12. Increasing Interoperability between Digital Twin Standards and Specifications Transformation of DTDL to AAS
- **Summary**: The work propose a mapping of the AAS element into DTDL model
- **Authors**:
- **DOI**:


### 13. Generation of digital twins for information exchange between partners in the Industrie 4.0 value chain
- **Summary**: Utilizing a model-driven approach: it formalizes the AAS meta-model in a domain-specific language and a intermediate representation, and then generates a compatible schemas for XML, JSON, and RDF formats.
- **Authors**:
- **DOI**:

### 14. An Industry 4.0 Asset Administration Shell-Enabled Digital Solution for Robot-Based Manufacturing Systems / Toward Data Interoperability of Enterprise and Control Applications via the Industry 4.0 Asset Administration Shell
- **Summary**: Manually create the AAS with AASX Package Explorer and use a designed XML-Parser to map the AAS and the OPC UA infromation models. Use JSON parser to convert AAS and Excel file
- **Authors**:
- **DOI**:

### 15. Using AutomationML to Generate Digital Twins of Tooling Machines for the Purpose of Developing Energy Efficient Production Systems
- **Summary**: The paper introduces a methodology leveraging AutomationML and Graph-based Design Languages to automatically generate Digital Twins. Graph-based Design languages contains the defined vocabularies, rules and compilers. AutomationML provides the data interface and serves as data exchange container.
- **Authors**:
- **DOI**:

### 16. Modelling with AAS and RDF in Industry 4.0
- **Summary**: The authors propose a two-fold approach: firstly, they establish a set of rules for converting RDF-based models into AAS models to aid in model development, and secondly, they suggest using RDF-based models to create a digital shadow of AASs, enhancing semantic discoverability.
- **Authors**:
- **DOI**:

## 17. Model-Based Test Case Generation for Compliance Checking of Reactive Asset Administration Shells
- **Summary**: This paper focuses on developing an automated method for generating test cases to verify Asset Administration Shell (AAS) server implementations for Digital Twins in Industry 4.0. The method involves manually creating AAS instance samples, parsing the OpenAPI specification to extract JSON schemas and API endpoints, analyzing dependencies between endpoints, and systematically generating cases for testing AAS-server implementations.
- **Authors**:
- **DOI**:

### 18. Semantic Interoperability of Digital Twins: Ontology-based Capability Checking in AAS Modeling Framework
- **Summary**: It introduces a transformation module that converts between OWL ontologies and UML models, enriching AAS models with semantic annotations in the manufacturing domain. The approach uses the OML adapter for transforming MaRCO vocabularies into a UML profile, which is then applied to AAS models as stereotypes. 
- **Authors**:
- **DOI**:

### 19. I4.0-compliant integration of assets utilizing the Asset Administration Shell
- **Summary**: The paper illustrates the mapping translation of semantic descriptions of plants, machines, or components from OPC UA information models into the AAS model, ensuring standardized and interoperable data.
- **Authors**:
- **DOI**:

### 20. Asset Administration Shells, Configuration, Code Generation: A power trio for Industry 4.0 Platforms
- **Summary**: The paper presents an IIoT platform integrating AAS, flexible configuration support, and code generation for Industry 4.0 platforms. The authors point out the importance of AAS generation for scaling
- **Authors**:
- **DOI**:

### 21. Asset Administration Shell: Domain Specific Language Approach to Integrate Heterogeneous Device Endpoints
- **Summary**: The method described in the paper involves developing a domain-specific language to facilitate the data integrations of different manufacturing assets. This DSL is tailored to map different manufacturing assets and protocols, such as OPC-UA and MQTT, into a unified company model.
- **Authors**:
- **DOI**:

### 22. Semantic Asset Administration Shell Towards a Cognitive Digital Twin
- **Summary**: The paper focuses on integrating semantic technologies with Asset Administration Shell (AAS) to create Cognitive Digital Twins (CDTs) for industrial machines, and it details a method of creating an Asset Administration Shell through a combination of ontological modeling and semantic technologies.
- **Authors**:
- **DOI**:

### 23. Generating Industry 4.0 Asset Administration Shells with Data from Engineering Data Logistics
- **Summary**: This paper proposes a method facilitating the collection and export of AAS for logistics data between engineering workgroups and the AutomationML engineering data. It starts by identifying relevant AutomationML domain-specific languages (DSLs) within an engineering network, which include data models from various engineering disciplines and tools. These models are integrated into an overall data model using AutomationML, forming a comprehensive representation of the engineering system. Subsequently, submodels for the AAS are identified based on these integrated engineering objects. The method then utilizes an export adapter to transform the collected data into an AAS AutomationML serialization. This adapter adds necessary role and interface classes and translates attributes into the AAS format. 
- **Authors**:
- **DOI**:

### 24. Towards an Ontology-Based Dictionary for Production Planning and Control in the Domain of Injection Molding
- **Summary**: The paper details an approach to create a standardized vocabulary for production planning and control (PPC) , aimed at facilitating machine-to-machine communication through AAS. This involves collecting detailed information for each process step in PPC within the injection molding domain and then constructing a UML class diagram. The outcome is an ontology PPCinIM, serving as a PPC dictionary, which underpins the formation of standardized digital twins through AAS and enrich the identifiable semantics of the data properties. 
- **Authors**:
- **DOI**:

### 25. Towards asset administration shell-based continuous engineering in process industries
- **Summary**: This paper focuses on the data integration of engineering processes in the industrial automation domain within the Industry 4.0 framework. It highlights the importance of embedding engineering information into the digital twin of a process plant to maintain and exchange engineering information across various phases of the plant lifecycle. AAS is defined as a technology-neutral Unified Modelling Language (UML) model with mappings to multiple file-based serializations, such as XML, JSON, and AutomationML, RDF, and interactive APIs for different lifecycle phases. 
- **Authors**:
- **DOI**:

### 26. Insights into Mapping Solutions Based on OPC UA Information Model Applied to the Industry 4.0 Asset Administration Shell
- **Summary**: The paper discusses modeling techniques for the OPC UA Information Model, which is essential for exposing information in the AAS metamodel. The method for creating an AAS in the paper involves mapping AAS entities into the OPC UA Information Model and structuring the OPC UA AddressSpace.
- **Authors**:
- **DOI**:



# Semantics for data integration:
Other paper point out the importance of the semantics
## 27. The Semantic Asset Administration Shell
- **Summary**: It introduces an ontology for the AAS specification, creates an RML mapping, enables mappings from between different data formats, and provides resources for validating RDF entities. The paper focuses on bridging the gap between industrial manufacturing frameworks and Semantic Web contributions, aiming to enhance data integration, reasoning, and interoperability in industrial scenarios through semantic formalization.
- **Authors**:
- **DOI**:

### 28. Semantic Asset Administration Shells in Industry 4.0: A Survey
- **Summary**: The paper explores the technical aspects of Semantic Asset Administration Shells (AAS) in Industry 4.0. It delves into the structure, communication protocols, and interoperability challenges of AAS, emphasizing the need for standardization and semantic technologies integration to facilitate effective digital representation of physical assets in industrial environments.
- **Authors**:
- **DOI**:

### 29. Semantic Integration Patterns for Industry 4.0 
- **Summary**: The paper proposes semantic integration patterns and discusses the development of a semantic interoperability middleware to integrate digital twins in manufacturing systems. It focuses on Asset Administration Shell (AAS) models, utilizing  semantically enriched data interfaces.
- **Authors**:
- **DOI**:

### 30. Semantic Interoperability in the Industry 4.0 Using the IEEE 1451 Standard
- **Summary**: The paper discusses enhancing semantic interoperability in Industry 4.0 using the IEEE 1451 standards. It highlights the limitations of syntactic interoperability achieved by IEEE 1451.1 and proposes using JSON-Linked Data (JSON-LD) to add semantic descriptions to metadata, enabling better integration with frameworks like OPC UA and oneM2M​​.
- **Authors**:
- **DOI**:

## 31. Asset Administration Shell for the Wiring Harness System
- **Summary**: The discusses the creation of a digital twin for wiring harness systems in automobiles using AAS. The creation involves collaborative effort among various stakeholders in the value network, including OEMs, suppliers, and software and machine manufacturers. The authors point out the necessities and potentials of automating the effort-intensive AAS creation process of assets by using semantic interoperability and neural language models.
- **Authors**:
- **DOI**:
 
## 32. On the Role of Digital Twins in Data Spaces
- **Summary**: The authors leverage the International Data Space vocabulary and ontologies to enhance the semantics with semantic ID in AAS in their projects , making the data can be queried from a special connector with the required meaningful description.
- **Authors**:
- **DOI**:

### 33. PLM/ALM Integration With The Asset Administration Shell
- **Summary**: The paper's proposed method, Plm4AAS, involves the  integration of Product Lifecycle Management (PLM) and Application Lifecycle Management (ALM) through the Asset Administration Shell (AAS). The process includes exporting PLM data using PLM XML and ALM data using ReqIF formats, manually creating an AAS for the asset using tool AASX Package Explorer, and importing these data sets as separate submodels into the AAS. The concept description of the data are based on a standard in order to enable vendor-independent integration.
- **Authors**:
- **DOI**:

### 34. The industry 4.0 standards landscape from a semantic integration perspective
- **Summary**: It proposes the Standards Ontology (STO) for semantically describing and integrating different industrial standards related to Industry 4.0 , thereby aiding in the semantic mapping and integration of exisiting concepts in ontologies.
- **Authors**:
- **DOI**:

### 35. Migration and synchronization of plant segments with Asset Administration Shells
- **Summary**: The paper details a migration approach from PackML to AAS in existing plants​​ for multi-vendor data interoperability and functional interoperability. It emphasizes the need for system-wide descriptions of plants and their components.
- **Authors**:
- **DOI**:

### 36. An Approach for Realizing Hybrid Digital Twins Using Asset Administration Shells and Apache StreamPipes
- **Summary**: The paper outlines a method for enhancing the interoperability AAS-based digital twins in a semantically consistent manner. The developed tool Apache StreamPipes can be used for processing heterogenous data from different data sources and sinks, e.g., communicated data from different network protocols, files, or databases
- **Authors**:
- **DOI**:

### 37. Asset Administration Shell as Integration Layer for the Orchestration of Mixed Process and Manufacturing Plants
- **Summary**: The method for creating the AAS involves integrating the MTP and PackML standards.The AAS is used to form an integration layer to abstract differences between MTP and PackML standards.
- **Authors**:
- **DOI**:

### 38. Data Administration Shell for Data-Science-Driven Development
- **Summary**: The paper focuses on linking data sets with information about their origin, analyses, results, and scripts, encasing them into AAS with necessary metadata and links to related development artifacts. The purpose is to facilitate the reuse of data sets for information sharing and management in joint cross-enterprise engineering projects.
- **Authors**:
- **DOI**:

### 39. Architecture Blueprints for the Application of the Industry 4.0 Asset Administration Shell
- **Summary**: It outlines the methodologies based on numerous use cases, emphasizing the significance of semantic annotation, common data models, and unique identifiers for AAS elements. Additionally, the paper highlights the importance of data conversion in serialization and de-serialization processes, ensuring a unified understanding and efficient management of AAS submodel data across different organizational environments.
- **Authors**:
- **DOI**:

### 40. Overview and Comparison of Asset Information Model Standards
- **Summary**: It addresses the challenge posed by the variety of protocols for information exchange and evaluates different standards for the virtual description of an automation device. These standards include W3C WoT Thing Description, Asset Administration Shell, Digital Factory Framework, Automation Markup Language, Module Type Package, OPC UA, Process Automation - Device Information Model, and Field Device Integration. The standards are compared across four categories: property representation, service representation, information modeling for direct device access, and discovery mechanisms. The paper emphasizes the need for generic integration strategies, model transformation and semantic annotations to combine these models, as no single standard fully addresses all use cases​​.
- **Authors**:
- **DOI**:


# Other tools:
Methods and tools that simplify the creation of AAS
### 41. Automated Design and Integration of Asset Administration Shells in Components of Industry 4.0
- **Summary**: The method for creating Asset Administration Shells (AAS) in the paper involves a semi-automated process using a configuration wizard. This wizard is designed to accelerate the formation process and simplify the implementation of AASs. It ensures that the administration shells are generated in compliance with Industry 4.0 standards and requirements. 
- **Authors**:
- **DOI**:

## 42. AASX Server
- **Summary**: 
- **URL**:

## 43. Eclipse BaSyx
- **Summary**: 
- **URL**:

## 44. FA3ST Service
- **Summary**: 
- **URL**:
- 
## 45. NOVAAS
- **Summary**: 
- **URL**:
