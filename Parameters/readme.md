In this folder, you can find quantitaive parameters mapped to the model, which can be used, for example, for kinetic/thermodynamic modelling and analysis.
### ./thermodynamics
Estimates (mean vector and covariance matrix) of the transformed Gibbs free energies of reactions ($\Delta_rG'^{\circ}$) for all metabolic reactions in the model, accounting for compartment-specific parameters (pH, pMg, ionic strength, potential) and multi-compartment reactions. Note that few reactions for which estimates could not be obtained are present in the datset and encoded with a very large variance in the covariance matrix ($10^{10}$). Depending on the application at hand, large eigenvalues in the covariance matrix can create numerical issues, in which case we reccomend omitting these reactions from the matrix and simply treat them as missing estimates.

### ./apparent_turnover_numbers
Apparent turnover numbers fitted to proteomic data from [1]. These are the same values used to compute enzyme costs in EC-*i*CH360 Since these parameters were *simultaneously* fitted  to enzyme abundance data across multiple growth conditions, they are not condition-specific. Rather, they encode average saturation trends across conditions. More information is available on the *i*CH360 pre-print.