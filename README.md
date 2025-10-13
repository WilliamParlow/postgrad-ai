# Postgraduate AI Repository

This repository contains comprehensive coursework and projects from a postgraduate program in Artificial Intelligence, organized into three main phases covering fundamental concepts, neural networks, and advanced machine learning techniques.

## 📁 Repository Structure

### Phase 1: Foundations (`fase_1/`)
**Introduction to AI and Python Programming**

#### `ai_introduction/`
- **Laboratory**: TensorFlow training lab (`tensorflow_training_lab.py`)
- **Libraries**: 
  - `matplotlib/`: Quick start guides and numpy integration tutorials
  - `tensorflow/`: TensorFlow integration with matplotlib
- **Notebooks/Labs**: Hands-on lab exercises (`lab_1.ipynb`, `lab_2.ipynb`)
- **Problem Solving**: Search algorithms including uniform cost search and breadth-first search

#### `python/`
- **Introduction to Python**: Conditionals, loops, data structures, file manipulation
- **NumPy**: Introduction to numerical computing
- **Pandas**: Comprehensive data manipulation tutorials (8 lessons covering data loading, analysis, cleaning, correlation, and plotting)
- **Exercise Helper**: Practice exercises and utilities

### Phase 2: Artificial Neural Networks (`fase_2/`)
**Deep dive into neural network architectures and implementations**

#### `artificial_neural_networks/`
- **Pattern Classification (PMC)**: 
  - MLP classifiers for Iris dataset and diabetes classification
  - Practical assignments and challenges
- **Scikit-learn Integration**:
  - Perceptron classification
  - SGD Classifier implementations
  - MLP Regressor for house sales prediction
  - Cross-validation and hyperparameter tuning
- **PMC & PMCR**: 
  - MLP Regressor implementations
  - Data normalization and standardization techniques
- **Autoencoders**: 
  - MNIST dataset implementations
  - Fashion-MNIST applications
- **Time-Variant Systems (TDNN)**:
  - Temperature prediction models
  - Self-Organizing Maps (SOM)
  - Radial Basis Function (RBF) networks
- **Validation Techniques**: Cross-validation pipelines and GridSearchCV
- **Pandas Applications**: Advanced data manipulation for neural network preprocessing

### Phase 3: Machine Learning (`fase_3/`)
**Advanced machine learning algorithms and techniques**

#### `machine_learning/`
- **Introduction & Concepts**: Fundamental ML concepts and evaluation metrics
- **Regression Algorithms**: 
  - Sampling techniques
  - Evaluation metrics
  - Various regressor implementations
- **Classification Algorithms**:
  - Evaluation measures
  - Multiple classification algorithms
  - Spam detection applications
- **Ensemble Methods**: 
  - Committee algorithms
  - Ensemble approaches and implementations
- **Hyperparameter Tuning**: Advanced optimization techniques

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Installation
```bash
# Clone the repository
git clone <repository-url>
cd postgrad-ai

# Install all required packages
pip install -r requirements.txt
```

### Manual Installation
If you prefer to install packages individually:

```bash
# Core data science libraries
pip install numpy pandas matplotlib seaborn

# Machine learning frameworks
pip install scikit-learn tensorflow keras

# Jupyter environment
pip install jupyter notebook ipykernel

# Additional utilities
pip install plotly openpyxl
```

### Running the Notebooks
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Navigate to the desired phase and open the notebook files (`.ipynb`)

3. For Google Colab users, upload notebooks directly to Colab for cloud execution

## 📚 Key Technologies & Libraries

### Core Libraries
- **NumPy**: Numerical computing and array operations
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization and plotting
- **Seaborn**: Statistical data visualization

### Machine Learning
- **Scikit-learn**: Traditional ML algorithms (classification, regression, clustering)
- **TensorFlow**: Deep learning framework
- **Keras**: High-level neural network API

### Development Environment
- **Jupyter Notebook**: Interactive development environment
- **Google Colab**: Cloud-based notebook environment

## 🎯 Learning Path

1. **Start with Phase 1**: Build Python and data science fundamentals
2. **Progress to Phase 2**: Dive into neural networks and deep learning
3. **Advance to Phase 3**: Master advanced machine learning techniques

Each phase builds upon the previous one, ensuring a comprehensive understanding of AI and machine learning concepts.

## 📊 Dataset Information

The repository includes various datasets for hands-on learning:
- **Iris Dataset**: Classification exercises
- **MNIST**: Handwritten digit recognition
- **Fashion-MNIST**: Clothing classification
- **House Sales Data**: Regression analysis
- **Temperature Data**: Time series prediction
- **Spam Dataset**: Text classification
- **Breast Cancer Dataset**: Medical classification

## 🔧 Additional Resources

- **Step-by-step Neural Network Process**: `fase_2/artificial_neural_networks/step_by_step_processo_redes_neurais.md`
- **Exercise Files**: Various CSV and Excel files for data manipulation practice
- **Solution Files**: Professor-provided solutions and implementations

## 📝 Notes

- All notebooks are designed to be educational and include detailed comments in Portuguese
- Some notebooks are optimized for Google Colab execution
- The repository follows a progressive learning structure from basic concepts to advanced implementations
- Each phase includes both theoretical concepts and practical implementations

---

*This repository represents a comprehensive postgraduate curriculum in Artificial Intelligence, covering everything from basic Python programming to advanced neural network architectures and machine learning algorithms.*