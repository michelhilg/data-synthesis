# Deep Generative Models for Synthetic Image Augmentation in Computer Vision-based Quality Inspection

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
|   |   |-- thesis_section-description.ipynb
        .
        .
        .
|   |-- 04_results
|   |   |-- thesis_section-description.ipynb
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

## Usage

The recomand approach to use this repository is detailed in the following steps:

1. Clone the repository to your local machine:

```
git clone https://github.com/michelhilg/data-synthesis.git
```
2. Sign in or create a Kaggle account in this [link](https://www.kaggle.com). Kaggle is an open-source platform for data science projects that provides a powerful cloud computing environment, offering 30 free GPU hours per week.

3. Connect your cloned files to your Kaggle account. This can be done either by manually uploading the desired notebooks or by using the Kaggle API.

4. Add the necessary data on Kaggle to run the desired notebook using the link provide by the `data/data.md` file:

    * [Link to datasets](https://www.kaggle.com/michelhilgemberg/datasets?scroll=true)

5. Follow the instructions within the notebook to execute the code and reproduce the experiments conducted in the thesis. Please note that when running the notebooks on Kaggle, there is no need for a `requirements.txt` file as Kaggle automatically manages the required packages.


## Additional Resources

For additional information and detailed insights into the thesis, please refer to the full text of the bachelor thesis document.

## License

The code in this repository is provided under the MIT License.

## Acknowledgments

I would like to express my gratitude to all individuals and organizations that provided assistance and support during the research and development of this study.

Thank you! Obrigado! Danke!
