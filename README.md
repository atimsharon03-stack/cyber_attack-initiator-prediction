# Predicting Cyber Attack Initiator Type from Global Incidents.

## Team
 Ahuura Faustine ( Dataset selection, understanding and cleaning), Mozan Ahmed Adam (EDA and Visualization), Atim Sharon Chloe (Modeling and Evaluation),
 *Every member contributed to discussions, documentation, and presentation*

## Overview
This project aims to develop a Machine Learning classification model that predicts the type of cyber attack initiator (for example, nation-state, hacktivist, organized crime group, or individual actor) based on information from recorded global cyber incidents.

By analyzing historical incident data, the model can help identify attack patterns, understand threat behavior, and potentially support cyber defense and risk management decisions.

## Dataset Description

The dataset used in this project is the Global Dataset of Cyber Incidents (V1.2) openly available on Zenodo.

Dataset Source: [https://zenodo.org/records/11108195](https://zenodo.org/records/11108195)

The dataset contains over 2,800 records covering cyber incidents that occurred worldwide between 2000 and 2024.
Each row represents a single recorded cyber incident and includes attributes about the attacker, the target, and the characteristics of the event.

| Category               | Example Columns                                                     | Description                                                        |
| ---------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Incident Metadata      | incident_id, year, month, region                      | Unique identifiers and time/location details of each attack               |
| Attacker Information   | initiator_category, initiator_country, initiator_sector | Who launched the attack (nation-state, hacktivist, organized crime, etc.) |
| Target Information     | receiver_category, receiver_country, receiver_sector    | Who was targeted (government, business, education, etc.)                  |
| Attack Characteristics | method, impact_level, duration_days, num_victims      | How the attack was carried out and its consequences                       |
| Outcomes               | response_type, cost_estimate, data_leak                 | The results or estimated impact of the attack                             |



## Files in this repo
- EuRepoC_Global_Database_1.2 .csv
- Predicting_Cyber_Attack_Initiator_Type_from_Global_Cyber_Incidents .ipynb

## Reproduce results
1. Run EDA notebook, Train model, Evaluate: Predicting_Cyber_Attack_Initiator_Type_from_Global_Cyber_Incidents .ipynb

## Results summary
- Best model: RandomForest 
- Key metric: Accuracy = 87%, F1 = 62.2%
- Conclusion: Random Forest is the preferred model for this dataset due to its higher overall accuracy and balanced performance.

## Technologies Used
Python (Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn),
Colab Notebook,
GitHub for version control and collaboration








 





