Estimates of the transformed Gibbs free energies of reactions ($\Delta_rG'^{\circ}$) for all metabolic reactions in the model, accounting for compartment-specific parameters (pH, pMg, ionic strength, potential) and multi-compartment reactions. The estimates were obtained via the component-contribution method described in [1,2] assuming the following compartment parameters [3]:

|Compartment|pH  |pMg|I  |$\phi$   |T     |
|-----------|----|---|---|------|------|
|e          |6.90|3.0|0.1|0.000 |310.15|
|p          |6.91|3.0|0.1|-0.001|310.15|
|c          |7.80|3.0|0.1|-0.086|310.15|

 where $I$ is the ionic strength, $\phi$ is the potential, and $T$ is the temperature.

The estimates are provided via a mean vector (`drg0_prime_mean.csv`) and a covariance matrix square root (`drg0_cov_sqrt.csv`). The estimates can thus be modelled by a multivariate normal random vector:
$$\Delta_rG'^{\circ} \sim \mathcal{N}(\mu,~ QQ^{\top})$$
where $\mu$ is the provided mean vector and $Q$ is the provided covariance matrix square root.root 

 **Note**
 
A few reactions for which estimates could not be obtained are present in the datset and encoded with a very large variance in the covariance matrix ($10^{10}$). Depending on the application at hand, large eigenvalues in the covariance matrix can create numerical issues, in which case we reccomend omitting these reactions from the matrix and simply treat them as missing estimates.

### References
1. Noor, E., Haraldsdóttir, H. S., Milo, R. & Fleming, R. M. T. Consistent Estimation of Gibbs Energy Using Component Contributions. PLOS Computational Biology 9, e1003098 (2013).
2.  Beber, M. E. et al. eQuilibrator 3.0: a database solution for thermodynamic constant estimation. Nucleic Acids Research 50, D603–D609 (2022).
3. Gollub, M. G., Backes, T., Kaltenbach, H.-M. & Stelling, J. ENKIE: A package for predicting enzyme kinetic parameter values and their uncertainties. 2023.03.08.531697 Preprint at https://doi.org/10.1101/2023.03.08.531697 (2023).
