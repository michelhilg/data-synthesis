# Deep Generative Models for Data Synthesis in Manufacturing

## Introduction

This repository contains the code and information related to a bachelor thesis titled "Deep Generative Models for Data Synthesis in Manufacturing". The thesis focuses on the generation of synthetic images in the manufacturing domain using deep generative models techniques. The primary goal of this study is to apply and compare different deep generative models for synthetic image augmentation in order to perform a DL-model-based visual quality inspection in a complex manufacturing use case with limited data

## Repository Structure

The repository adheres to the cookie cutter structure, which is defined as follows:

```
|-- data/
|   |-- data.md
|-- models/
|   |-- models.md
|-- notebooks/
|   |-- 03_research_desing/
|   |   |-- research-desing-notebooks.ipynb
        .
        .
        .
|   |-- 04_results
|   |   |-- results-notebooks.ipynb
        .
        .
        .
|-- reports/
|   |-- figures/
|   |   |-- thesis-figures.drawio
        .
        .
        .
|   |-- bachelor-thesis.pdf
|-- src/
|   |-- data/
|   |   |-- data-related-python-scripts.py
        .
        .
        .
|-- .gitignore
|-- LICENSE
|-- README.md
```

- The `notebooks` directory contains Jupyter notebooks used in the thesis. They follows a naming conventional as:

    * ```
    parent_folder_as_thesis_chapter/thesis_section-description.ipynb

    ```

- The `data` directory contains a markdown file with information about the datasets used and created in the thesis. This markdown presents a link to access the data.

- The `model` directory contains a markdown file with information about the pre-trained models created in the thesis. This markdown presents a link to access the models.

- The `reports` directory contains:
    * A folder with the arts created over the thesis elaboration in a editable mode on open-source .drawio format. 
    * The final thesis document.

- The `src` directory contains python scrips related to data processing steps. Here is defined the scripts for labeling the dataset and also perform the conventional augmentation tecnique.

- The `.gitignore` file is used for organizing and managing files within the Git repository.

- The `LICENSE` has information about the use of this content.

- The `README.md` file (this file) provides an overview and instructions for using the repository.
