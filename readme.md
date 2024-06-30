# *i*CH360: a compact model of *Escherichia Coli* core and biosynthesis metabolism
![Alt text](Visualisation/examples/full_map_map_w_fluxes_and_labels.png "The complete map of iCH360 with overlaid a flux distribution computed for aerobic growth on glucose")
### What is *i*CH360?
*i*CH360 is a medium-scale, *Goldilocks* model of *Escherichia Coli* K-12 MG1655 energy and biosynthesis metabolism. Derived from the genome-scale model *i*ML1515 [1], *i*CH360 includes all pathways required for energy production and the biosynthesis of the main biomass building blocks, such as amino acids, nucleotides, and fatty acids, and accounts for more complex biomass requirements via an equivalent cost in terms of precursors. 

The stoichiometric model is supported by a knowledge graph, constructed using both data from the EcoCyc database [2] and manual curation. In this graph, nodes represent biological entities (reactions, proteins, genes or compounds) and edges represent (potentially quantitative) functional relationships between them, including catalysis, protein subunit composition, protein modification, and regulatory interactions.

You can find more information about the model, the supporting knowledge graph, and their applications in our pre-print:

https://arxiv.org/abs/2406.16596

or in the [Docs](./Docs/) section of the repo.
### In this repo, you will find:
- The stoichiometric model of *iCH360* in SBML and JSON formats, which can be opened, manipulated and optimised with the COBRA toolbox [3].
- The *i*CH360 knowldge graph in GML and Cytoscape (.cyjs) formats.
- The metabolic maps for the complete model and its subsystems for visualisation with Escher [4]
- Thermodynamic ($\Delta G'^{\circ}$) and kinetic (apparent turnover numbers) parameter sets mapped to the model.


In addition to the main metabolic models, the repo contains the following two model variants, also in SBML/JSON formats:
- EC-*i*CH360, a version of the model that includes enzyme capacity constraints, based on the sMOMENT format [5]
- *i*CH360red, a minimally-reduced version of the model (18 less reactions), which is amenable to elementary flux modes (EFMs) enumeration and analysis.

### Docs and Tutorials
You can find more information about the model, its variants, and the knowledge graph in the [Docs](./Docs/) section. In addition, the [Examples](./Examples/) sections contains a number of short metabolic modelling tutorials that can help you getting started using the model.
### Citing us
If you use *i*CH360 in your work, please cite the supporting manuscript

```
@misc{corrao2024iCH360,
      title={A compact model of Escherichia coli core and biosynthetic metabolism}, 
      author={Marco Corrao and Hai He and Wolfram Liebermeister and Elad Noor},
      year={2024},
      eprint={2406.16596},
      archivePrefix={arXiv},
      primaryClass={q-bio.MN}
      url={https://arxiv.org/abs/2406.16596}, 
}
```
### References
1. Monk, J. M. et al. iML1515, a knowledgebase that computes Escherichia coli traits. Nat Biotechnol 35, 904–908 (2017).
2. Keseler, I. M. et al. The EcoCyc database: reflecting new knowledge about Escherichia coli K-12. Nucleic Acids Res 45, D543–D550 (2017).
3. Ebrahim, A., Lerman, J. A., Palsson, B. O. & Hyduke, D. R. COBRApy: COnstraints-Based Reconstruction and Analysis for Python. BMC Systems Biology 7, 74 (2013).
4. King, Z. A. et al. Escher: A Web Application for Building, Sharing, and Embedding Data-Rich Visualizations of Biological Pathways. PLOS Computational Biology 11, e1004321 (2015).
5. Bekiaris, P. S. & Klamt, S. Automatic construction of metabolic models with enzyme constraints. BMC Bioinformatics 21, 19 (2020).


