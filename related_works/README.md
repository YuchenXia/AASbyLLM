# The main features of this work (AASbyLLM) and the novelties:
Technologies:
- First research prototype applying **generative LLM** for generating AAS
- Apply generative LLMs for **inferencing** and embedding LLMs for **similarity retrieval**

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

## Natural Language Processing 
These works apply embedding language models in NLP for information processing:
### 1. Automated monitoring applications for existing buildings through natural language processing based semantic mapping of operational data and creation of digital twins (2023)
- **Summary**: This paper focuses on creating automated technical monitoring applications for existing buildings using NLP to semantically map operational data and form digital twins. It tackles the challenge of integrating semantically heterogeneous operational data into monitoring applications, traditionally a manual effort-intensive process. The method uses AI to map this data to a standard, creating semantic digital twins of buildings, achieving over 95% effectiveness in automating data point mapping.
- **Authors**: Maximilian Both, Björn Kämper, Alina Cartus, Jo Beermann, Thomas Fessler, Jochen Müller, Christian Diedrich
- **DOI**: https://doi.org/10.1016/j.enbuild.2023.113635


### 2. Comparison of Different NLP Models for Semantic Interoperability of Heterogeneous Asset Administration Shells (2023)
- **Summary**: The paper explores different natural language processing (NLP) embedding models to achieve semantic interoperability in heterogeneous AAS. It focuses on extending the Industrie 4.0 approach to heterogeneous semantics by automating the mapping of varied vocabularies to target semantics using NLP models. The paper compares existing embedding models, evaluates their mapping accuracy, and discusses the integration of structured knowledge via knowledge graphs. It shows that fine-tuning existing models to the target vocabulary based on the ECLASS standard significantly improves mapping accuracy.
- **Authors**: Maximilian Both, Jochen Müller, Christian Diedrich
- **DOI**: https://doi.org/10.1515/auto-2021-0050


### 3. Automated generation of Asset Administration Shell: a transfer learning approach with neural language model and semantic fingerprints (2022)
- **Summary**: Proposes a transfer learning approach with a neural language model to map data properties from various information models into a standardized AAS model. It involves generating "semantic fingerprints," vectors containing latent conceptual meaning, which aid in creating AAS with reduced development effort.
- **Authors**: Yuchen Xia, Nasser Jazdi, Michael Weyrich
- **DOI**: https://doi.org/10.1109/ETFA52439.2022.9921637


### 4. Interoperability of Semantically Heterogeneous Digital Twins through NLP Methods (2022)
- **Summary**: This method improves interactions between Asset Administration Shells by mapping heterogeneous descriptions to a standardized semantic language. It involves an automated matching process using trained embedding models on domain-specific texts for mapping.
- **Authors**: Alina Cartus, Maximilian Both, Nicolai Maisch, Jochen Müller, Christian Diedrich
- **DOI**: https://doi.org/10.34641/clima.2022.143


### 5. Automatisierte Abbildung Semantisch Heterogener I4.0-Verwaltungsschalen (2021)
- **Summary**: The paper discusses automating semantic matching for interoperability between heterogeneous AAS, achieved through automated mapping of unknown vocabularies to a target ontology using NLP methods. It combines ISO standards pre-trained language models with sentence embeddings for this purpose.
- **Authors**: Maximilian Both, Jochen Müller, Christian Diedrich
- **DOI**: https://doi.org/10.1515/auto-2021-0050


## Rule-based:
These papers apply model transfromation and rule-based mappings, mainly utilizing the model-based(/-driven) software engineering (MBSE/MDSE) pattern or semantic web technologies.
### 6. Model Transformation for Asset Administration Shells (2020)
- **Summary**: The authors propose a custom-built Model Transformation Language (MTL) for Asset Administration Shells -- AASMTL-- focusing on its designed abstract syntax and language semantics. The MTL, based on a simplified version of the Object Constraint Language (OCL), is tailored to transform information across various AAS submodels.
- **Authors**: Torben Miny, Michael Thies, Ulrich Epple, Christian Diedrich
- **DOI**: https://doi.org/10.1109/IECON43393.2020.9254649

### 7. Interoperable Digital Twins in IIoT Systems by Transformation of Information Models: A Case Study with Asset Administration Shell (2019)
- **Summary**: The paper presents a system enabling interoperable digital twins in IIoT by transforming information models into AAS format. This process involves a detailed mapping model that dictates the conversion rules from source formats (like ABB Ability™ digital twins) to the AAS format.
- **Authors**: Marie Platenius-Mohr, Somayeh Malakuti, Sten Grüner, Thomas Goldschmidt
- **DOI**: https://doi.org/10.1145/3365871.3365873
  
### 8. A Semi-Automatic Approach for Asset Administration Shell Creation from Heterogeneous Data (2023)
- **Summary**: The paper introduces a semi-automatic approach for AAS creation with a python implementation. It involves extracting engineering information from various document types (PDF, STP, XML, XML/AML, RDF) , then mapping this information to the AAS meta-model. This process creates individual AASs for each document, which are later integrated into a comprehensive AAS representing the asset.
- **Authors**: Jingyun Zhao, Birgit Vogel-Heuser, Fandi Bi, Josua Höfgen, Felix Ocker, Bernd Vojanec, Timo Markert, André Kraft
- **DOI**: https://doi.org/10.1016/j.ifacol.2023.10.1532

### 9. Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies (2023)
- **Summary**: a bidirectional mapping approach that allows to transform between a model represented with the AAS submodels and a model represented with the skill ontology called CaSkMan
- **Authors**: Luis Miguel Vieira Da Silva; Aljosha Köcher; Milapji Singh Gill; Marco Weiss; Alexander Fay
- **DOI**: https://doi.org/10.1109/ETFA54631.2023.10275459


### 10. File- and API-based interoperability of digital twins by model transformation: An IIoT case study using asset administration shell (2020)
- **Summary**: The method for creating the AAS involves a customizable transformation system. This system enables engineers to define transformation rules flexibly and apply them to source and target systems. 
- **Authors**: Marie Platenius-Mohr, Somayeh Malakuti, Sten Grüner, Johannes Schmitt, Thomas Goldschmidt
- **DOI**: https://doi.org/10.1016/j.future.2020.07.004

### 11. Enabling semantic interoperability of asset administration shells through an ontology-based modeling method (2022)
- **Summary**: The paper describes a method for creating AAS using the Ontology Modeling Language (OML) to map AAS models to an ontology-compatible format (OWL). This involves selecting relevant MaRCO ontology concepts and integrating them into the OML vocabulary. The OML Adapter is then used to create a Unified Modeling Language (UML) profile from these OML files. The resulting MaRCO UML profile is applied to the AAS models as stereotypes, allowing the designer to refine them with specific properties. This process enables the conversion of AAS classes into OWL individuals, ensuring semantic interoperability.
- **Authors**: Yining Huang, Saadia Dhouib, Luis Palacios Medinacelli, Jacques Malenfant
- **DOI**: https://doi.org/10.1145/3550356.3561606

### 12. Increasing Interoperability between Digital Twin Standards and Specifications Transformation of DTDL to AAS (2023)
- **Summary**: The work propose a mapping of the AAS element into DTDL model
- **Authors**:  Carlos Schmidt, Friedrich Volz, Ljiljana Stojanovic, Gerhard Sutschet
- **DOI**: https://doi.org/10.3390/s23187742


### 13. Generation of digital twins for information exchange between partners in the Industrie 4.0 value chain (2023)
- **Summary**: Utilizing a model-driven approach: it formalizes the AAS meta-model in a domain-specific language and a intermediate representation, and then generates a compatible schemas for XML, JSON, and RDF formats.
- **Authors**: Nico Braunisch; Marko Ristin-Kaufmann; Robert Lehmann; Martin Wollschlaeger, Hans Wernher van de Venn
- **DOI**: https://doi.org/10.1109/INDIN51400.2023.10218306

### 14. An Industry 4.0 Asset Administration Shell-Enabled Digital Solution for Robot-Based Manufacturing Systems / Toward Data Interoperability of Enterprise and Control Applications via the Industry 4.0 Asset Administration Shell (2021)
- **Summary**: Manually create the AAS with AASX Package Explorer and use a designed XML-Parser to map the AAS and the OPC UA infromation models. Use JSON parser to convert AAS and Excel file
- **Authors**: Xun Ye, Seung Ho Hong, Won Seok Song, Yu Chul Kim, Xiongfeng Zhang
- **DOI**: https://doi.org/10.1109/ACCESS.2021.3128580

### 15. Using AutomationML to Generate Digital Twins of Tooling Machines for the Purpose of Developing Energy Efficient Production Systems (2021)
- **Summary**: The paper introduces a methodology leveraging AutomationML and Graph-based Design Languages to automatically generate Digital Twins. Graph-based Design languages contains the defined vocabularies, rules and compilers. AutomationML provides the data interface and serves as data exchange container.
- **Authors**: Nicolai Beisheim, Markus Linde, Tobias Ott, Sebastian Amann
- **DOI**: https://doi.org/10.3233/ATDE210092

### 16. Modelling with AAS and RDF in Industry 4.0 (2023)
- **Summary**: The authors propose a two-fold approach: firstly, they establish a set of rules for converting RDF-based models into AAS models to aid in model development, and secondly, they suggest using RDF-based models to create a digital shadow of AASs, enhancing semantic discoverability.
- **Authors**: Sjoerd Rongen, Nikoletta Nikolova, Mark van der Pas
- **DOI**: https://doi.org/10.1016/j.compind.2023.103910

## 17. Model-Based Test Case Generation for Compliance Checking of Reactive Asset Administration Shells (2022)
- **Summary**: This paper focuses on developing an automated method for generating test cases to verify Asset Administration Shell (AAS) server implementations for Digital Twins in Industry 4.0. The method involves manually creating AAS instance samples, parsing the OpenAPI specification to extract JSON schemas and API endpoints, analyzing dependencies between endpoints, and systematically generating cases for testing AAS-server implementations.
- **Authors**: Björn Otto, Karsten Meinecke, Tobias Kleiner
- **DOI**: (Beiträge des Jahreskolloquiums KommA 2022)

### 18. Semantic Interoperability of Digital Twins: Ontology-based Capability Checking in AAS Modeling Framework (2023)
- **Summary**: It introduces a transformation module that converts between OWL ontologies and UML models, enriching AAS models with semantic annotations in the manufacturing domain. The approach uses the OML adapter for transforming MaRCO vocabularies into a UML profile, which is then applied to AAS models as stereotypes. 
- **Authors**: Yining Huang, Saadia Dhouib, Luis Palacios Medinacelli, Jacques Malenfant
- **DOI**: https://doi.org/10.1109/ICPS58381.2023.10128003

### 19. I4.0-compliant integration of assets utilizing the Asset Administration Shell (2019)
- **Summary**: The paper illustrates the mapping translation of semantic descriptions of plants, machines, or components from OPC UA information models into the AAS model, ensuring standardized and interoperable data.
- **Authors**: Jonathan Fuchs, Jan Schmidt, Jörg Franke, Kasim Rehman, Manuel Sauer, Stamatis Karnouskos
- **DOI**: https://doi.org/10.1109/ETFA.2019.8869255

### 20. Asset Administration Shells, Configuration, Code Generation: A power trio for Industry 4.0 Platforms (2023)
- **Summary**: The paper presents an IIoT platform integrating AAS, flexible configuration support, and code generation for Industry 4.0 platforms. The authors point out the importance of AAS generation for scaling
- **Authors**: Holger Eichelberger, Claudia Niederée
- **DOI**: https://doi.org/10.1109/ETFA54631.2023.10275339

### 21. Asset Administration Shell: Domain Specific Language Approach to Integrate Heterogeneous Device Endpoints (2020)
- **Summary**: The method described in the paper involves developing a domain-specific language to facilitate the data integrations of different manufacturing assets. This DSL is tailored to map different manufacturing assets and protocols, such as OPC-UA and MQTT, into a unified company model.
- **Authors**: Felix Brandt, Eric Brandt, Javad Ghofrani, David Heik, Dirk Reichelt 
- **DOI**: https://doi.org/10.1007/978-3-030-63092-8_72

### 22. Semantic Asset Administration Shell Towards a Cognitive Digital Twin (2023)
- **Summary**: The paper focuses on integrating semantic technologies with Asset Administration Shell (AAS) to create Cognitive Digital Twins (CDTs) for industrial machines, and it details a method of creating an Asset Administration Shell through a combination of ontological modeling and semantic technologies.
- **Authors**: Tomás Moreno, Thiago Sobral, António Almeida, António Lucas Soares, Américo Azevedo 
- **DOI**: https://doi.org/10.1007/978-3-031-38165-2_79

### 23. Generating Industry 4.0 Asset Administration Shells with Data from Engineering Data Logistics
- **Summary**: This paper proposes a method facilitating the collection and export of AAS for logistics data between engineering workgroups and the AutomationML engineering data. It starts by identifying relevant AutomationML domain-specific languages (DSLs) within an engineering network, which include data models from various engineering disciplines and tools. These models are integrated into an overall data model using AutomationML, forming a comprehensive representation of the engineering system. Subsequently, submodels for the AAS are identified based on these integrated engineering objects. The method then utilizes an export adapter to transform the collected data into an AAS AutomationML serialization. This adapter adds necessary role and interface classes and translates attributes into the AAS format. 
- **Authors**: Arndt Lüder, Anna-Kristin Behnert, Felix Rinker, Stefan Biffl
- **DOI**: https://doi.org/10.1109/ETFA46521.2020.9212149

### 24. Towards an Ontology-Based Dictionary for Production Planning and Control in the Domain of Injection Molding (2023)
- **Summary**: The paper details an approach to create a standardized vocabulary for production planning and control (PPC) , aimed at facilitating machine-to-machine communication through AAS. This involves collecting detailed information for each process step in PPC within the injection molding domain and then constructing a UML class diagram. The outcome is an ontology PPCinIM, serving as a PPC dictionary, which underpins the formation of standardized digital twins through AAS and enrich the identifiable semantics of the data properties. 
- **Authors**: Patrick Sapel, Christian Hopmann
- **DOI**: https://doi.org/10.1016/j.jii.2023.100488

### 25. Towards asset administration shell-based continuous engineering in process industries (2023)
- **Summary**: This paper focuses on the data integration of engineering processes in the industrial automation domain within the Industry 4.0 framework. It highlights the importance of embedding engineering information into the digital twin of a process plant to maintain and exchange engineering information across various phases of the plant lifecycle. AAS is defined as a technology-neutral Unified Modelling Language (UML) model with mappings to multiple file-based serializations, such as XML, JSON, and AutomationML, RDF, and interactive APIs for different lifecycle phases. 
- **Authors**: Sten Grüner, Mario Hoernicke, Katharina Stark , Nicolai Schoch, Nafise Eskandani, John Pretlove
- **DOI**: https://doi.org/10.1515/auto-2023-0012

### 26. Insights into Mapping Solutions Based on OPC UA Information Model Applied to the Industry 4.0 Asset Administration Shell (2020)
- **Summary**: The paper discusses modeling techniques for the OPC UA Information Model, which is essential for exposing information in the AAS metamodel. The method for creating an AAS in the paper involves mapping AAS entities into the OPC UA Information Model and structuring the OPC UA AddressSpace.
- **Authors**: Salvatore Cavalieri, Marco Giuseppe Salafia
- **DOI**: https://doi.org/10.3390/computers9020028



# Semantics for data integration:
Other paper point out the importance of the semantics
## 27. The Semantic Asset Administration Shell (2019)
- **Summary**: It introduces an ontology for the AAS specification, creates an RML mapping, enables mappings from between different data formats, and provides resources for validating RDF entities. The paper focuses on bridging the gap between industrial manufacturing frameworks and Semantic Web contributions, aiming to enhance data integration, reasoning, and interoperability in industrial scenarios through semantic formalization.
- **Authors**: Sebastian R. Bader, Maria Maleshkova 
- **DOI**: https://doi.org/10.1007/978-3-030-33220-4_12

### 28. Semantic Asset Administration Shells in Industry 4.0: A Survey (2021)
- **Summary**: The paper explores the technical aspects of Semantic Asset Administration Shells (AAS) in Industry 4.0. It delves into the structure, communication protocols, and interoperability challenges of AAS, emphasizing the need for standardization and semantic technologies integration to facilitate effective digital representation of physical assets in industrial environments.
- **Authors**: Sadeer Beden, Qiushi Cao, Arnold Beckmann
- **DOI**: https://doi.org/10.1109/ICPS49255.2021.9468266

### 29. Semantic Integration Patterns for Industry 4.0 (2022)
- **Summary**: The paper proposes semantic integration patterns and discusses the development of a semantic interoperability middleware to integrate digital twins in manufacturing systems. It focuses on Asset Administration Shell (AAS) models, utilizing  semantically enriched data interfaces.
- **Authors**: Felix Strohmeier, Georg Güntner, Dietmar Glachs, Reinhard Mayr
- **DOI**: https://doi.org/10.5220/0011550100003329

### 30. Semantic Interoperability in the Industry 4.0 Using the IEEE 1451 Standard (2020)
- **Summary**: The paper discusses enhancing semantic interoperability in Industry 4.0 using the IEEE 1451 standards. It highlights the limitations of syntactic interoperability achieved by IEEE 1451.1 and proposes using JSON-Linked Data (JSON-LD) to add semantic descriptions to metadata, enabling better integration with frameworks like OPC UA and oneM2M​​.
- **Authors**: Helbert da Rocha, Antonio Espirito-Santo, Reza Abrishambaf
- **DOI**: https://doi.org/10.1109/IECON43393.2020.9254274

## 31. Asset Administration Shell for the Wiring Harness System (2023)
- **Summary**: The discusses the creation of a digital twin for wiring harness systems in automobiles using AAS. The creation involves collaborative effort among various stakeholders in the value network, including OEMs, suppliers, and software and machine manufacturers. The authors point out the necessities and potentials of automating the effort-intensive AAS creation process of assets by using semantic interoperability and neural language models.
- **Authors**: Georg Schnauffer, David Görzig, Christian Kosel, Johannes Diemer 
- **DOI**: https://doi.org/10.1007/978-3-031-27933-1_30
 
## 32. On the Role of Digital Twins in Data Spaces (2023)
- **Summary**: The authors leverage the International Data Space vocabulary and ontologies to enhance the semantics with semantic ID in AAS in their projects , making the data can be queried from a special connector with the required meaningful description.
- **Authors**: Friedrich Volz, Gerhard Sutschet, Ljiljana Stojanovic, Thomas Usländer
- **DOI**: https://doi.org/10.3390/s23177601

### 33. PLM/ALM Integration With The Asset Administration Shell (2020)
- **Summary**: The paper's proposed method, Plm4AAS, involves the  integration of Product Lifecycle Management (PLM) and Application Lifecycle Management (ALM) through the Asset Administration Shell (AAS). The process includes exporting PLM data using PLM XML and ALM data using ReqIF formats, manually creating an AAS for the asset using tool AASX Package Explorer, and importing these data sets as separate submodels into the AAS. The concept description of the data are based on a standard in order to enable vendor-independent integration.
- **Authors**: Andreas Deuter, Sebastian Imort
- **DOI**: https://doi.org/10.1016/j.promfg.2020.11.040

### 34. The industry 4.0 standards landscape from a semantic integration perspective (2017)
- **Summary**: It proposes the Standards Ontology (STO) for semantically describing and integrating different industrial standards related to Industry 4.0 , thereby aiding in the semantic mapping and integration of exisiting concepts in ontologies.
- **Authors**: Irlán Grangel-González, Paul Baptista, Lavdim Halilaj, Steffen Lohmann, Maria-Esther Vidal, Christian Mader, Sören Auer
- **DOI**: https://doi.org/10.1109/ETFA.2017.8247584

### 35. Migration and synchronization of plant segments with Asset Administration Shells (2022)
- **Summary**: The paper details a migration approach from PackML to AAS in existing plants​​ for multi-vendor data interoperability and functional interoperability. It emphasizes the need for system-wide descriptions of plants and their components.
- **Authors**: Stephan Schäfer, Dirk Schöttke, Thomas Kämpfe, Oliver Lachmann, Aaron Zielstorff, Bernd Tauber
- **DOI**: https://doi.org/10.1109/ETFA52439.2022.9921595

### 36. An Approach for Realizing Hybrid Digital Twins Using Asset Administration Shells and Apache StreamPipes (2021)
- **Summary**: The paper outlines a method for enhancing the interoperability AAS-based digital twins in a semantically consistent manner. The developed tool Apache StreamPipes can be used for processing heterogenous data from different data sources and sinks, e.g., communicated data from different network protocols, files, or databases
- **Authors**: Michael Jacoby, Branislav Jovicic, Ljiljana Stojanovic, Nenad Stojanović
- **DOI**: https://doi.org/10.3390/info12060217

### 37. Asset Administration Shell as Integration Layer for the Orchestration of Mixed Process and Manufacturing Plants (2022)
- **Summary**: The method for creating the AAS involves integrating the MTP and PackML standards.The AAS is used to form an integration layer to abstract differences between MTP and PackML standards.
- **Authors**: Julian Grothoff, Sten Grüner, Christian Barth, Alexander Kehl, Matthias Freund, Tobias Klausmann
- **DOI**: https://doi.org/10.1109/ETFA52439.2022.9921653

### 38. Data Administration Shell for Data-Science-Driven Development (2021)
- **Summary**: The paper focuses on linking data sets with information about their origin, analyses, results, and scripts, encasing them into AAS with necessary metadata and links to related development artifacts. The purpose is to facilitate the reuse of data sets for information sharing and management in joint cross-enterprise engineering projects.
- **Authors**: Andreas Löcklin, Hannes Vietz, Dustin White, Tamás Ruppert, Nasser Jazdi, Michael Weyrich
- **DOI**: https://doi.org/10.1016/j.procir.2021.05.019

### 39. Architecture Blueprints for the Application of the Industry 4.0 Asset Administration Shell (2022)
- **Summary**: It outlines the methodologies based on numerous use cases, emphasizing the significance of semantic annotation, common data models, and unique identifiers for AAS elements. Additionally, the paper highlights the importance of data conversion in serialization and de-serialization processes, ensuring a unified understanding and efficient management of AAS submodel data across different organizational environments.
- **Authors**: Frank Schnicke, Thomas Kuhn, Tobias Klausmann, Sten Grüner, Daniel Porta
- **DOI**: https://doi.org/10.1109/ETFA52439.2022.9921694

### 40. Overview and Comparison of Asset Information Model Standards (2023)
- **Summary**: It addresses the challenge posed by the variety of protocols for information exchange and evaluates different standards for the virtual description of an automation device. These standards include W3C WoT Thing Description, Asset Administration Shell, Digital Factory Framework, Automation Markup Language, Module Type Package, OPC UA, Process Automation - Device Information Model, and Field Device Integration. The standards are compared across four categories: property representation, service representation, information modeling for direct device access, and discovery mechanisms. The paper emphasizes the need for generic integration strategies, model transformation and semantic annotations to combine these models, as no single standard fully addresses all use cases​​.
- **Authors**: Torben Miny, Michael Thies, Lina Lukic, Sebastian Käbisch, Kazeem Oladipupo, Christian Diedrich
- **DOI**: https://doi.org/10.1109/ACCESS.2023.3312286


# Other tools:
Methods and tools that simplify the creation of AAS (2021)
### 41. Automated Design and Integration of Asset Administration Shells in Components of Industry 4.0
- **Summary**: The method for creating Asset Administration Shells (AAS) in the paper involves a semi-automated process using a configuration wizard. This wizard is designed to accelerate the formation process and simplify the implementation of AASs. It ensures that the administration shells are generated in compliance with Industry 4.0 standards and requirements. 
- **Authors**: Jakub Arm, Tomas Benesl, Petr Marcon, Zdenek Bradac, Tizian Schröder, Alexander Belyaev, Thomas Werner, Vlastimil Braun, Pavel Kamensky, Frantisek Zezulka, Christian Diedrich, Premysl Dohnal
- **DOI**: https://doi.org/10.3390/s21062004

## 42. AASX Server
- **Summary**: 
- **URL**: https://github.com/admin-shell-io/aasx-server

## 43. Eclipse BaSyx
- **Summary**: 
- **URL**: https://projects.eclipse.org/projects/dt.basyx

## 44. FA3ST Service
- **Summary**: 
- **URL**: https://github.com/FraunhoferIOSB/FAAAST-Service
- 
## 45. NOVAAS
- **Summary**: 
- **URL**: https://gitlab.com/novaas/catalog/nova-school-of-science-and-technology/novaas
