# Predicting Cyber Attack Initiator Type from Global Incidents.

## Team
 Ahuura Faustine ( Dataset selection, understanding and cleaning), Mozan Ahmed Adam (EDA and Visualization), Atim Sharon Chloe (Modeling and Evaluation),*Every member contributed to discussions, documentation, and presentation*

## Overview
This project aims to develop a Machine Learning classification model that predicts the type of cyber attack initiator (for example, nation-state, hacktivist, organized crime group, or individual actor) based on information from recorded global cyber incidents.

By analyzing historical incident data, the model can help identify attack patterns, understand threat behavior, and potentially support cyber defense and risk management decisions.

Dataset Description

The dataset used in this project is the Global Dataset of Cyber Incidents (V1.2) openly available on Zenodo.

Dataset Source: [https://zenodo.org/records/11108195](https://zenodo.org/records/11108195)

The dataset contains over 2,800 records covering cyber incidents that occurred worldwide between 2000 and 2024.
Each row represents a single recorded cyber incident and includes attributes about the attacker, the target, and the characteristics of the event.

| Category               | Example Columns                                                     | Description                                                        |
| ---------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Incident Metadata      | `incident_id`, `year`, `month`, `region`                      | Unique identifiers and time/location details of each attack               |
| Attacker Information   | `initiator_category`, `initiator_country`, `initiator_sector` | Who launched the attack (nation-state, hacktivist, organized crime, etc.) |
| Target Information     | `receiver_category`, `receiver_country`, `receiver_sector`    | Who was targeted (government, business, education, etc.)                  |
| Attack Characteristics | `method`, `impact_level`, `duration_days`, `num_victims`      | How the attack was carried out and its consequences                       |
| Outcomes               | `response_type`, `cost_estimate`, `data_leak`                 | The results or estimated impact of the attack                             |



## Files in this repo
- `data/` — raw and processed dataset
- `cyber_incidents_ml_project.ipynb

## Reproduce results
1. Run EDA notebook, Train model, Evaluate: `cyber_incidents_ml_project.ipynb`
2. Train model: `notebooks/02_train.ipynb`
3. Evaluate: `notebooks/03_evaluate.ipynb`

## Results summary
- Best model: RandomForest (example)
- Key metric: Accuracy = 87%, F1 = 62.2%
- Conclusion: Random Forest is the preferred model for this dataset due to its higher overall accuracy and balanced performance.

.

## Contact
Team lead email or GitHub usernames


# cyber_attack-initiator-prediction
The dataset used in this project is the Global Dataset of Cyber Incidents (V1.2) openly available on Zenodo.

Dataset Source: [https://zenodo.org/records/11108195](https://zenodo.org/records/11108195)

The dataset contains over 2,800 records covering cyber incidents that occurred worldwide between 2000 and 2024.
Each row represents a single recorded cyber incident and includes attributes about the attacker, the target, and the characteristics of the event.


| Category               | Example Columns                                                     | Description                                                        |
| ---------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Incident Metadata      | `incident_id`, `year`, `month`, `region`                      | Unique identifiers and time/location details of each attack               |
| Attacker Information   | `initiator_category`, `initiator_country`, `initiator_sector` | Who launched the attack (nation-state, hacktivist, organized crime, etc.) |
| Target Information     | `receiver_category`, `receiver_country`, `receiver_sector`    | Who was targeted (government, business, education, etc.)                  |
| Attack Characteristics | `method`, `impact_level`, `duration_days`, `num_victims`      | How the attack was carried out and its consequences                       |
| Outcomes               | `response_type`, `cost_estimate`, `data_leak`                 | The results or estimated impact of the attack                             |

 Predicting Cyber Attack Initiator Type from Global Cyber Incidents

Project Overview

This project aims to develop a Machine Learning classification model that predicts the type of cyber attack initiator (for example, nation-state, hacktivist, organized crime group, or individual actor) based on information from recorded global cyber incidents.

By analyzing historical incident data, the model can help identify attack patterns, understand threat behavior, and potentially support cyber defense and risk management decisions.

Dataset Description

The dataset used in this project is the Global Dataset of Cyber Incidents (V1.2) openly available on Zenodo.

Dataset Source: [https://zenodo.org/records/11108195](https://zenodo.org/records/11108195)

The dataset contains over 2,800 records covering cyber incidents that occurred worldwide between 2000 and 2024.
Each row represents a single recorded cyber incident and includes attributes about the attacker, the target, and the characteristics of the event.




 Machine Learning Goal

To predict the attacker category (`initiator_category`) using other incident attributes such as:
Target sector and region
Attack method
Duration and number of victims
Year and geographic region

Project Workflow

1. Data Understanding & Loading – Load and inspect the dataset from Zenodo.
2. Exploratory Data Analysis (EDA)– Explore distributions and relationships between variables.
3. Data Preprocessing– Handle missing values, encode categorical variables, and normalize features.
4. Model Development– Train and evaluate at least two machine learning algorithms (e.g., Logistic Regression, Random Forest).
5. Model Evaluation– Compare performance using metrics such as accuracy, precision, recall, and F1-score.
6. Visualization & Interpretation– Visualize model results, confusion matrices, and feature importance.
7. Presentation– Prepare slides summarizing findings, model performance, and recommendations.

Repository Structure

cyber_incidents_project/
│
├── data/
│   └── Global_Dataset_of_Cyber_Incidents_V1.2.csv
│
├── notebooks/
│   └── cyber_incidents_ml_project.ipynb
│
├── presentation/
│   └── cyber_incidents_presentation.pptx
│
├── README.md
└── requirements.txt

Group Members
Mozan Ahmwd Adam  Data Collection & Cleaning 
Ahuura Faustine  EDA & Visualization        
Atim sharon Chloe  Modeling & Evaluation                |

(Every member contributed to discussions, documentation, and presentation.)

Technologies Used
Python (Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn)
Colab Notebook
GitHub for version control and collaboration



