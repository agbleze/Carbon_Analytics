import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import numpy as np

from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

total_emission_df = pd.read_csv(r'data/total_emission_df.csv')

X_all = total_emission_df[['state',	'lga',	'sector',	'credit_mean',	'income_mean']]

#%%
ord_encode = OrdinalEncoder()
feature_ordinal_encoded = ord_encode.fit_transform(X_all[['sector', 'state', 'lga']])

encoded_features = pd.DataFrame(feature_ordinal_encoded, columns=['sector_encode', 'state_encode', 'lga_encode'])

total_emission_df[['sector_encoded', 'state_encoded', 'lga_encoded']] = encoded_features


ordinal_preprocess = OrdinalEncoder(
  handle_unknown="use_encoded_value", unknown_value=-1
)
impute_missing_predictor_values = SimpleImputer(strategy='mean',
                                                add_indicator=True
                                                )
decision_tree_data_preprocess = make_column_transformer((impute_missing_predictor_values, ['credit_mean', 'income_mean']),
                                                        (ordinal_preprocess, ['sector', 'state', 'lga'])
                                                        )

#%%
# create preprocess for linear model
ohe_preprocess = OneHotEncoder(handle_unknown='ignore')
num_column_preprocess_linear_ml = make_pipeline(impute_missing_predictor_values,
                                                StandardScaler(),
                                                )
linear_model_preprocess_pipeline = make_column_transformer((num_column_preprocess_linear_ml, ['credit_mean', 'income_mean']),
                                                           (ohe_preprocess, ['state', 'sector', 'lga'])
                                                           )








