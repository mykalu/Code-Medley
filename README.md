# Code Medley
Little things I've written that aren't quite big enough to be in their own repositories, but are nonetheless interesting and worth sharing (in my humble opinion)!

# Contents
## Rust
### `quicksort`
- Implementation of Hoare's partitioning algorithm, with the median index selected as the pivot
## Python
### `datasci`
- Implementation of a [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis)-based algorithm for reducing data to two dimensions
### `linalg`
- Function for calculating an eigenvalue of a matrix given a corresponding eigenvector  
- Function for estimating an eigenvector of a matrix given a corresponding eigenvalue
  - Uses the [inverse iteration](https://en.wikipedia.org/wiki/Inverse_iteration) algorithm
- Function for estimating the covariance matrix of a data matrix
- Function for estimating the top eigenvector of a matrix
  - Uses the [power iteration](https://en.wikipedia.org/wiki/Power_iteration) algorithm
- Function for matrix deflation to nullify an eigenpair
  - Uses the Wielandt deflation algorithm
### `utils`
- Function for asserting the datatype of a variable
- Function for asserting the dimensionality of a `np.ndarray`
- Function for reshaping a `np.ndarray` into a two-dimensional column vector
- Function for reshaping a `np.ndarray` into a two-dimensional row vector