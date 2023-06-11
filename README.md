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

- The `notebooks` directory contains Jupyter notebooks used in the thesis, which are accompanied by source references. These notebooks follow a naming convention as:

    ```
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

## Additional Resources

For additional information and detailed insights into the thesis, please refer to the full text of the bachelor thesis document.

## License

The code in this repository is provided under the MIT License.

## Acknowledgments

I would like to express my gratitude to all individuals and organizations that provided assistance and support during the research and development of this study.

Thank you! Obrigado! Danke!
