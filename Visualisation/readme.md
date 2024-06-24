# Escher Maps for the iCH360

Here, you will find a number of maps built in Escher [1], which you can use to visualise the model along with flux distributions and other experimental data.
### ./model_map
Constains the main Escher maps for iCH360. There are two ways to visualise iCH360:
1. The first is a full map (full_map.json), over flux distributions computed from iCH360 can be visualised directly.
2. The second is a compressed map, wherein long linear pathways have been converted into compressed pseudoreactions (indicated with "CP" at the end of their names). This is very compact, but cannot be used directly with iCH360. Instead, to use the compress map:
    - generate a flux distribution as a Pandas Series (e.g. using cobra.Model.optimize())
    - use the function export_fluxes_for_compressed_map() from visualisation_utils.py to map this to the compressed map.
    - upload the generated .json file as reaction data over the compressed map on Escher

### ./pathway_maps
Contains Escher maps for the specific subsystems in the model:
- biosynthesis of each amino-acid from core-metabolism precursors
- biosynthesis of nucleotides and deoxyribonucleotides
- biosynthesis of saturated and unsaturated fatty acids
- C1 metabolism

### ./pathways_not_in_model
Contains a collection of Escher maps for pathways not directly included in the model, but that were used to compute the equivalent biomass function. these include
- Biosynthesis of phospholipids
- Biosynthesis of murein
- biosynthesis of KDO-lipid
- de novo biosynthesis of cofactors
- active transport of ions and metals

Here are some examples of how the map look!

The complete map of iCH360
![Alt text](examples/complete_map.png "The complete map of iCH360")

The compressed map of iCH360
![Alt text](examples/compressed_map.png "The comressed map of iCH360")

### References
1. King, Z. A. et al. Escher: A Web Application for Building, Sharing, and Embedding Data-Rich Visualizations of Biological Pathways. PLOS Computational Biology 11, e1004321 (2015).
