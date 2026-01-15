
import numpy as np

def compute_pca_from_svd(standardized_returns):
    '''
    Compute PCA metrics using SVD approach.

    Parameters:
    standardized_returns : pandas DataFrame (m x n)

    Returns:
    dict with:
        - eigenvalues
        - variance_explained_ratio
        - cumulative_variance_ratio
    '''
    # Step 1: Scale data
    n_samples = len(standardized_returns)
    B = standardized_returns.values / np.sqrt(n_samples - 1)

    # Step 2: Economy SVD
    U, s, VT = np.linalg.svd(B, full_matrices=False)

    # Step 3: Eigenvalues
    eigenvalues = s ** 2

    # Step 4: Variance explained ratios (%)
    total_variance = np.sum(eigenvalues)
    variance_explained_ratio = (eigenvalues / total_variance) * 100

    # Step 5: Cumulative variance
    cumulative_variance_ratio = np.cumsum(variance_explained_ratio)

    return {
        'eigenvalues': eigenvalues,
        'variance_explained_ratio': variance_explained_ratio,
        'cumulative_variance_ratio': cumulative_variance_ratio
    }


def min_components_for_variance(metrics, threshold=90):
    '''
    Determine minimum number of components to reach variance threshold.
    '''
    cum_var = metrics['cumulative_variance_ratio']
    return int(np.argmax(cum_var >= threshold) + 1)


def weighted_average_eigenvalue(metrics):
    '''
    Compute variance-weighted average eigenvalue.
    '''
    eigenvalues = metrics['eigenvalues']
    weights = metrics['variance_explained_ratio'] / 100
    return float(np.sum(eigenvalues * weights))


def effective_dimension(metrics):
    '''
    Compute effective dimension (participation ratio).
    '''
    var_ratios = metrics['variance_explained_ratio'] / 100
    return float(1 / np.sum(var_ratios ** 2))
