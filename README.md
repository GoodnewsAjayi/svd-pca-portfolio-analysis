
# PCA Metrics Using SVD (Finance & Risk Analysis)

This repository implements **Principal Component Analysis (PCA)** using a **Singular Value Decomposition (SVD)** approach, applied to standardized financial return data.

The project was developed as part of an advanced financial data analysis module and covers:
- Memory and computational efficiency of Economy SVD
- PCA eigenvalues and variance explained
- Dimensionality reduction decisions
- Effective dimension (participation ratio)

---

## 📁 Project Structure

```
.
├── pca_svd_analysis.py   # Core PCA + SVD logic
├── README.md            # Project documentation
```

---

## 🚀 Features

The script provides reusable functions to:

### 1. PCA via SVD
- Scale standardized returns correctly
- Perform Economy SVD
- Compute eigenvalues of the covariance matrix
- Compute:
  - Variance explained (%)
  - Cumulative variance (%)

### 2. Minimum Components for Variance Threshold
- Determine how many principal components are needed to explain a target variance (e.g. 90%)

### 3. Weighted Average Eigenvalue
- Compute a variance-weighted eigenvalue score (useful as a diversification metric)

### 4. Effective Dimension (Participation Ratio)
- Measure how many components *effectively* contribute to variance

---

## 📌 Mathematical Background

Given standardized returns matrix \( X \) of shape \( m \times n \):

1. Scale data:
\[
B = \frac{X}{\sqrt{m - 1}}
\]

2. Economy SVD:
\[
B = U \Sigma V^T
\]

3. Covariance matrix:
\[
\text{Cov} = V \Sigma^2 V^T
\]

- Eigenvalues = squared singular values
- Eigenvectors = columns of \( V \)

---

## 🧠 Practical Interpretation

| Metric | Meaning |
|------|--------|
| Variance Explained | Importance of each principal component |
| Cumulative Variance | How many PCs are needed |
| Weighted Avg Eigenvalue | Variance concentration |
| Effective Dimension | True diversification level |

---

## 🧪 Example Usage

```python
from pca_svd_analysis import (
    compute_pca_from_svd,
    min_components_for_variance,
    weighted_average_eigenvalue,
    effective_dimension
)

metrics = compute_pca_from_svd(standardized_returns)

k = min_components_for_variance(metrics, threshold=90)
wavg = weighted_average_eigenvalue(metrics)
eff_dim = effective_dimension(metrics)
```

---

## 📊 Typical Outputs

- Eigenvalues sum to number of assets
- Variance explained sums to 100%
- Effective dimension is usually < number of assets

---

## 🛠 Requirements

- Python 3.8+
- NumPy
- Pandas

Install dependencies:
```bash
pip install numpy pandas
```

---

## 📈 Use Cases

- Portfolio risk decomposition
- Factor analysis
- Dimensionality reduction
- Quantitative finance research
- Interview / academic demonstrations

---

## 📄 License

MIT License.  
Feel free to use, adapt, and extend.

---

## ✨ Author

Prepared for academic and professional quantitative finance applications.
