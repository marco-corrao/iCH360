## *i*CH360 model folder
All models are provided in SBML (.xml) and JSON (.json) formats, and can be loaded and optimised directly in COBRA/COBRApy.

In this folder, you'll find the relevant files for the following model variants:
### *i*CH360
The main stoichiometric model, additionally containing annotations to external databases and Gene-protein-reaction (GPR) rules.

### *i*CH360red
The *i*CH360red submodel is a curated reduction of iCH360 containing 18 fewer metabolic reactions  and is designed to be amenable for EFM enumeration and analysis.

### EC_*i*CH360
Contains the Enzyme-Constrained (EC) version of the model (based on te sMOMENT formalism), parametrised with *typical* apparent turnover numbers ( $k_{app}$ ), which were fitted to measurements of enzyme abundance across multiple growth conditions. You can find more information on how these parameters were obtained in our pre-print.