#%% import packages
#%%
from random import random
import pandas as pd
import datar as dr
from datar import dplyr, f
from datar import tidyr
import datar.all as all
import datar.base as base
from sklearn.model_selection import (cross_val_score, 
                                     cross_val_score, 
                                     cross_val_predict
                                     )


#%%
sect11b_harvestw3 = pd.read_csv(r'data/sect11b_harvestw3.csv')

#%%
fuel_data_harvest = (sect11b_harvestw3 >> 
                     dplyr.filter(
                                   (f.item_desc== "KEROSENE")| 
                                   (f.item_desc == 'GAS')|
                                   (f.item_desc == "ELECTRICITY")|
                                   (f.item_desc == "FIREWOOD")|
                                   (f.item_desc == "CHARCOAL")|
                                   (f.item_desc == "PETROL")|
                                   (f.item_desc == "DIESEL")
                                ) >>
                     tidyr.pivot_wider(names_from=f.item_desc, 
                                       values_from=f.s11bq4
                                       ) 
                     >>
                     all.replace_na(dict(CHARCOAL = 0, KEROSENE = 0, GAS = 0, 
                                         ELECTRICITY = 0,FIREWOOD = 0, 
                                         PETROL = 0, DIESEL = 0
                                         )
                                    )
                    )


#%%
fuel_data_harvest_sum = (fuel_data_harvest.groupby(by=['state', 'lga', 'sector', 'hhid'])
                         ["CHARCOAL", "DIESEL", "ELECTRICITY",
                         "KEROSENE","GAS", "PETROL", "FIREWOOD"]
                         .agg('sum')
                         .reset_index()
                        )

#%%
### estimate co2 emission for petrol at household level
petrol_data_harvet_CO2emission = (fuel_data_harvest_sum >> 
                                  dplyr.select(f[0:4], f.PETROL) >>
                                    dplyr.mutate(petrol_total_expend = f.PETROL,
                                                price_per_ltr = 87, 
                                                total_ltr_consumed = (f.petrol_total_expend / f.price_per_ltr), 
                                                GHG_emission_factor_CO2 = 2.31,
                                                petrol_total_CO2_emitted_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2)
                                                )
                            )

#%%
### estimate co2 emission for kerosene at household level
kerosene_data_harvest_CO2emission = (fuel_data_harvest_sum >> dplyr.select(f[0:4], f.KEROSENE) >>
                          dplyr.mutate(kerosene_total_expend = f.KEROSENE,
                                       price_per_ltr = 50,
                                       total_ltr_consumed = (f.kerosene_total_expend/f.price_per_ltr),
                                       GHG_emission_factor_CO2 = 2.5,
                                       kerosene_total_CO2_emitted_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2)
                                       )
 )

#%%
### estimate co2 emission for LPG at household level
lpgas_data_harvest_CO2emission = (fuel_data_harvest_sum >> 
                                  dplyr.select(f[0:4], f.GAS) >>
                                    dplyr.mutate(gas_total_expend = f.GAS, 
                                                price_per_ltr = 368.396,
                                                total_kg_consumed = (f.gas_total_expend/f.price_per_ltr), 
                                                kg_to_liter_conversion = 1.96, 
                                                total_ltr_consumed = (f.total_kg_consumed * f.kg_to_liter_conversion), 
                                                GHG_emission_factor_CO2 = 1.51,
                                                lpgas_total_CO2_emitted_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2)
                                                )
                                )

#%%
### estimate co2 emission for electricity at household level
electricity_data_harvest_CO2emission = (fuel_data_harvest_sum >> 
                                        dplyr.select(f[0:4], f.ELECTRICITY) >>
                                        dplyr.mutate(electricity_total_expend = f.ELECTRICITY, 
                                                    price_per_KWh = 29, 
                                                    total_KWh_consumed = (f.electricity_total_expend/f.price_per_KWh),
                                                    GHG_emission_factor_CO2 = 0.4034043, 
                                                    electricity_total_CO2_emitted_kg = (f.total_KWh_consumed * f.GHG_emission_factor_CO2)
                                                    )
                                     )

#%%
## estimate co2 emission for charcoal at household level
charcoal_data_harvest_co2emission = (fuel_data_harvest_sum >> dplyr.select(f[0:4], f.CHARCOAL) >>
                                                            dplyr.mutate(charcoal_total_expend = f.CHARCOAL, 
                                                                        price_per_kg = 13.542815, 
                                                                        total_kg_consumed = (f.charcoal_total_expend/f.price_per_kg),
                                                                        convert_kg_to_tonnes = 0.001,
                                                                        total_tonn_consumed = (f.total_kg_consumed * f.convert_kg_to_tonnes),
                                                                        GHG_emission_factor_CO2 = 3304,
                                                                        charcoal_total_CO2_emitted_kg = (f.total_tonn_consumed * f.GHG_emission_factor_CO2))
                                                                
                                )

#%%
## ESTIMATE CO2 EMSSIONS FOR DIESIEL 
diesel_data_harvest_co2emission = (fuel_data_harvest_sum >> 
                                   dplyr.select(f[0:4], f.DIESEL) >>
                                    dplyr.mutate(diesel_total_expend = f.DIESEL, 
                                                price_per_ltr = 145, 
                                                total_ltr_consumed = (f.diesel_total_expend / f.price_per_ltr),
                                                GHG_emission_factor_CO2kg_per_ltr = 2.676492,
                                                diesel_total_CO2_emitted_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2kg_per_ltr)
                                            )
                                 )

#%%
## Estimate CO2 EMISSIONS FOR FIREWOOD
firewood_data_harvest_co2emission = (fuel_data_harvest_sum >>
                                      dplyr.select(fuel_data_harvest_sum[0:4], f.FIREWOOD) >>
                                      dplyr.mutate(firewood_total_expend = f.FIREWOOD,
                                                    price_per_kg = 8.125689,
                                                    total_firewood_kg = (f.firewood_total_expend / f.price_per_kg),
                                                    kg_to_tonnes = 0.001,
                                                    firewood_tonnes = f.total_firewood_kg * f.kg_to_tonnes,
                                                    GHG_emission_factor_CO2kg_per_tonnes = 1.747,
                                                    firewood_total_CO2_emitted_kg = (f.total_firewood_kg * f.GHG_emission_factor_CO2kg_per_tonnes)
                                                  )    
                                    )



#%%
# ASSIGN FUEL name to fuel eg df['PETRO'] = 'petrol'
# Rename fuel to 'fuel_type' eg df.rename(columns='fuel_type')

#%%
df_merge = pd.concat([petrol_data_harvet_CO2emission,kerosene_data_harvest_CO2emission, 
                      lpgas_data_harvest_CO2emission, electricity_data_harvest_CO2emission, 
                      charcoal_data_harvest_co2emission, 
                      diesel_data_harvest_co2emission,
                      firewood_data_harvest_co2emission
                      ]
                    )




# %%
df_merge.isnull().sum()

#%%
from typing import List, Optional

# %%
colnames = ['petrol_total_CO2_emitted_kg', 'kerosene_total_CO2_emitted_kg', 
            'lpgas_total_CO2_emitted_kg', 'electricity_total_CO2_emitted_kg', 
            'charcoal_total_CO2_emitted_kg', 'diesel_total_CO2_emitted_kg',
            'firewood_total_CO2_emitted_kg','state', 'lga', 'hhid', 'sector',
            'total_CO2_kg'
            ]
 
#%%
# for colname in colnames:
#   df_merge[colname].fillna(0, inplace= True)

#df_merge['petrol_total_CO2_emitted_kg'] +  df_merge['kerosene_total_CO2_emitted_kg']

#%% In order to sum up co2 by fuel type for each hhid, we need to 
# find a way to handle NaNs. fill NaN with 0 to make the rowise sum

df_merge.fillna(0, inplace=True)

#%%
df_merge['total_CO2_kg'] = (df_merge['petrol_total_CO2_emitted_kg'] + df_merge['kerosene_total_CO2_emitted_kg'] +
                            df_merge['lpgas_total_CO2_emitted_kg'] + df_merge['electricity_total_CO2_emitted_kg'] +
                            df_merge['charcoal_total_CO2_emitted_kg'] + df_merge['diesel_total_CO2_emitted_kg'] + 
                            df_merge['firewood_total_CO2_emitted_kg']
                            )
  
# %%
#colnames.extend(['total_CO2_kg'])

#%%
co2_data = df_merge[colnames]

#%%
co2_data.isnull().sum()

#%% At this point when total_CO2_kg == 0 then it means no data was available for 
## each of the fuel type because we replaced NaN with 0 for expenditure on each 
## fuel type inorder to have combinations of all enegy consumption by hhid
## The 0 are filtered inorder to have the right number of hhid for estimating the mean

co2_all_df = co2_data[co2_data['total_CO2_kg'] > 0]

# %% find
#co2_grp = co2_data.groupby(['state','lga', 'sector', 'hhid'])[['total_CO2_kg']].mean().reset_index()

co2_all_mean = co2_all_df.groupby(['state','lga', 'sector', 'hhid'])[['total_CO2_kg']].mean().reset_index()

#%%
#co2_grp

# %%
#co2_grp['hhid'].nunique()
# %%
# s3q21a HOW MUCH WAS YOUR LAST PAYMENT?(NAIRA)
income_df = pd.read_csv(r'data/sect3_plantingw3.csv')

income_df_select = income_df[['state',	'lga', 'sector', 'hhid', 's3q21a', 's3q13a']]

# %%
income_per_hhid_df =( income_df_select.groupby(['state',	'lga', 'sector',	'hhid'])['s3q21a']
                     .mean().reset_index()
                     .rename(columns={'s3q21a': 'income_mean'})
                     )

#%%
income_per_hhid_df

# %%
"""
7. What is the average loan / credit received by households / individuals in
the 10 lowest paid labour type compared to the 10 highest paid labour type

s4cq6   >>>> HOW MUCH WAS BORROWED?
"""

#%%
#sect4c2_plantingw3 = 
credit_df = pd.read_csv("data/sect4c2_plantingw3.csv")
# %%
credit_df.rename({"s4cq6": "credit"}, inplace=True, axis="columns")

#%%
credit_df_select = credit_df[['state',	'lga',	'sector', 'hhid', 'credit']]

#%%
credit_mean_df = (credit_df_select.groupby(['state',	'lga',	'sector', 'hhid'])
                  [['credit']].mean().reset_index().rename(columns={'credit': 'credit_mean'})
                  )

#%%
#income_per_hhid_df.join(other=credit_mean_df, how='outer', lsuffix='_income', rsuffix='_credit')
credit_mean_df['credit_mean'].fillna(credit_mean_df.groupby('lga')['credit_mean'].mean())

#%%
credit_sub = credit_mean_df[['hhid', 'credit_mean']]
income_sub = income_per_hhid_df[['hhid', 'income_mean']]
#credit_sub.join(co2_all_mean, on='hhid', how='right', rsuffix='_co2')

#try_co2 = co2_all_mean.join(credit_sub, on='hhid', how='left', lsuffix='_credit')

#%%
co_cred_merge = co2_all_mean.merge(credit_sub, on='hhid', how='left')
co2_cred_income_merge = co_cred_merge.merge(income_sub, on="hhid", how="left")
total_emission_df = co2_cred_income_merge.copy()


#%%
total_emission_df.dropna()


#%% Developing amodel
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import BaggingRegressor
from xgboost import XGBRFRegressor
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
#%%
# create nnnn bnnnPREDICTORS and TARGET dataset
X = total_emission_df[['income_mean', 'credit_mean']]
y = total_emission_df[['total_CO2_kg']]

#%% split training and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=0)

hist_model = HistGradientBoostingRegressor(random_state=0)

#%%
hist_model.fit(X=X_train, y=y_train)

#%%
y_pred = hist_model.predict(X_test)

#%%
test_rmse = mean_squared_error(y_true=y_test, y_pred=y_pred, squared= False)
train_rmse = mean_squared_error(y_true=y_train, y_pred=hist_model.predict(X_train), squared=False)

#%%
bagging = BaggingRegressor(base_estimator=hist_model, random_state=0)

#%%
bagging.fit(X_train, y_train)

#%%
bagg_y_pred_test = bagging.predict(X_test)

mean_squared_error(y_true=y_test, y_pred=bagg_y_pred_test, squared= False)


#%%
import stat
import scipy.stats as stats
import numpy as np

param_grid = {'max_depth': np.random.randint(low=1, high=20, size=21) ,
              'learning_rate': stats.uniform(0,1),
              'min_samples_leaf': np.random.randint(low=1, high=20, size=21),
              'l2_regularization': np.linspace(0, 1, num=10)
            }

n_iter_search = 20
#%%
randoncv = RandomizedSearchCV(estimator = hist_model,
                              param_distributions=param_grid,
                              cv=10, n_iter=n_iter_search,
                              random_state=0,# scoring=mean_squared_error, 
                              verbose=2
                            )


#%%
randoncv.fit(X_train, y_train)

#%%
rand_y_pred = randoncv.predict(X_test)

#%%
mean_squared_error(y_true=y_test, y_pred=rand_y_pred, squared=False)

#%%
randoncv.best_params_

#%%
hist_best_model = HistGradientBoostingRegressor(random_state=0,
                                                l2_regularization=0.8888888888888888,
                                                learning_rate=0.9023485831739843,
                                                max_depth=1,
                                                min_samples_leaf=7,
                                                #random_state=0
                                              )


hist_bagging = BaggingRegressor(base_estimator=hist_best_model,random_state=0)

#%%
hist_bagging.fit(X_train, y_train)

#%%
y_pred_hist_bagg_test = hist_bagging.predict(X_test)

#%%
mean_squared_error(y_true=y_test, y_pred=y_pred_hist_bagg_test, squared=False)

#%%
##########  Include state, sector and lga for prediction  ####################
#
#
X_all = total_emission_df[['state',	'lga',	'sector',	'credit_mean',	'income_mean']]

#%%
ord_encode = OrdinalEncoder()

#%%
#X_all[['sector_encode']] =
sec_ord = ord_encode.fit_transform(X_all[['sector', 'state', 'lga']])

encoded_features = pd.DataFrame(sec_ord, columns=['sector_encode', 'state_encode', 'lga_encode'])

#%%
X_all[['sector_encoded', 'state_encoded', 'lga_encoded']] = encoded_features

#%% use only the ordinal encoded features
X_all.drop(columns=['sector', 'state', 'lga'], inplace= True)

#%%
X_all_train, X_all_test, y_all_train, y_all_test =  train_test_split(X_all, y, random_state=0, test_size=0.3)

#%%
hist_model.fit(X=X_all_train, y=y_all_train)

#%%
y_pred_all = hist_model.predict(X_all_test)

#%%
mean_squared_error(y_true=y_all_test, y_pred=y_pred_all, squared=False)


#%%
bagg_hist_all = BaggingRegressor(base_estimator=hist_model, random_state=0)

bagg_hist_all.fit(X=X_all_train, y=y_all_train)

#%%
y_pred_bagg_hist_all = bagg_hist_all.predict(X_all_test)

#%%
mean_squared_error(y_true=y_all_test, y_pred=y_pred_bagg_hist_all, squared=False)

#%%
mean_squared_error(y_true=y_all_train, y_pred=bagg_hist_all.predict(X_all_train), squared=False)




########  Creating a composite model with imputiing missing values  ################ 
#
#
#

#%%
from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

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

#%%
# make lasso model
from sklearn.linear_model import LassoCV
lasso_pipeline = make_pipeline(linear_model_preprocess_pipeline,
                               LassoCV()
                               )

#%% make randomforest model
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=0)

rf_pipeline = make_pipeline(decision_tree_data_preprocess, rf)

#%%
from sklearn.ensemble import HistGradientBoostingRegressor
hgb = HistGradientBoostingRegressor(random_state=0)

hgb_pipeline = make_pipeline(decision_tree_data_preprocess, hgb)

#%%
# make ridgecv model and stack all models together
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import  StackingRegressor
ridge = RidgeCV()
all_models = [("Radom Forest", rf_pipeline),
              ("Lasso", lasso_pipeline),
              ("Gradient Boosting", hgb_pipeline)
              ]
stack_regressors = StackingRegressor(estimators=all_models, final_estimator=ridge)

#%%
X_all_raw = total_emission_df[['state',	'lga',	'sector',	'credit_mean',	'income_mean']]

#%%
X_raw_train, X_raw_test, y_raw_train, y_raw_test = train_test_split(X_all_raw, y, test_size=0.3, random_state=0)

#%%
stack_regressors.fit(X=X_raw_train, y=y_raw_train)

#%%
y_pred_stack = stack_regressors.predict(X_raw_test)

#%%
mean_squared_error(y_true=y_raw_test, y_pred=y_pred_stack, squared=False)



## bagging stacked regressor
#%%
#bagg_stack_regressors = BaggingRegressor(base_estimator=stack_regressors)

#%%
#bagg_stack_regressors.fit(X=X_raw_train, y=y_raw_train)


#%% measure and plot results
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_validate

#%%
def plot_regression_results(ax, y_true, y_pred, title, scores,
                            elapsed_time):
  
  ax.plot([y_true.min(), y_true.max()],
          [y_true.min(), y_true.max()]
          )
  ax.scatter(y_true, y_pred, alpha=0.2)
  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)
  ax.get_xaxis().tick_bottom()
  ax.get_yaxis().tick_left()
  ax.spines['left'].set_position(('outward',10))
  ax.spines['bottom'].set_position(('outward', 10))
  ax.set_xlim([y_true.all().min(), y_true.all().max()])
  ax.set_ylim([y_true.all().min(), y_true.all().max()])
  extra = plt.Rectangle((0, 0), 0, 0, fc='w', fill=False,
                        edgecolor='none', linewidth=0
                        )
  ax.legend([extra], [scores], loc='upper left')
  title = title + "\n Evaluation in {:.2f} seconds".format(elapsed_time)
  ax.set_title(title)
  
  
fig, axs = plt.subplots(2, 2, figsize=(9, 7))
axs = np.ravel(axs)

#%%
for ax, (name, est) in zip(axs, all_models + [('Stacking Regressor', stack_regressors)]):
  start_time = time.time()
  score = cross_validate(est, X_raw_train, y_raw_train,
                         scoring=['r2', 'neg_mean_absolute_error'],
                         n_jobs=2, verbose=0
                         )
  elapsed_time = time.time() - start_time
  
  y_pred = cross_val_predict(est, X_raw_train, y_raw_train, 
                             n_jobs=2, verbose=1)
  
  plot_regression_results(ax, y_raw_train, y_pred, name,
                          (r'$R^2={:.2f} \pm {:.2f}$' + '\n' + r'$MAE={:.2f}\pm {:.2f}$').format(
                            np.mean(score['test_r2']),
                            np.std(score['test_r2']),
                            -np.mean(score['test_neg_mean_absolute_error']),
                            np.std(score['test_neg_mean_absolute_error']),
                          ),
                          elapsed_time,
                          )

#%%
plt.suptitle('Single predictors versus stacked predictors')
plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.show()  
  


#%%  
# fit a knn regressor
from sklearn.neighbors import KNeighborsRegressor

knn = KNeighborsRegressor(n_neighbors=10)

knn_model_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)

#%%
knn_model_pipeline.fit(X=X_raw_train, y=y_raw_train)

#
y_pred_knn = knn_model_pipeline.predict(X_raw_test)

#%%
mean_squared_error(y_true=y_raw_test, y_pred=y_pred_knn, squared=False)

#%%
knn_results = []
for nn in range(1, 30):
  knn_schedule = KNeighborsRegressor(n_neighbors=nn)
  knn_schedule_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)
  knn_schedule_pipeline.fit(X=X_raw_train, y=y_raw_train)
  y_pred = knn_schedule_pipeline.predict(X_raw_test)
  rmse = mean_squared_error(y_true=y_raw_test, y_pred=y_pred, squared=False)
  knn_results.append({'k-neighbors': nn, 'rmse': rmse})
    
results = pd.DataFrame(data=knn_results) 
  
#%% lasso prediction
lasso_pipeline.fit(X_raw_train, y_raw_train)

#%%
y_pred_lasso = lasso_pipeline.predict(X_raw_test)

mean_squared_error(y_true=y_raw_test, y_pred=y_pred_lasso, squared=False)

#%% rf prediction
rf_pipeline.fit(X_raw_train, y_raw_train)

#%%
y_pred_rf = rf_pipeline.predict(X_raw_test)
mean_squared_error(y_true=y_raw_test, y_pred=y_pred_rf, squared=False)

#%% ridged model
rd = RidgeCV(cv=10)
rd_pipeline = make_pipeline(linear_model_preprocess_pipeline, rd)

rd_pipeline.fit(X=X_raw_train, y=y_raw_train)

#%%
y_pred_rd = rd_pipeline.predict(X_raw_test)
mean_squared_error(y_true=y_raw_test, y_pred=y_pred_rd, squared=False)






#%% focus on only hhid with emission data for at leats 1 fuel type that is co2 > 0
total_emission_df = emission_df[emission_df['total_CO2_kg'] > 0]


# %%
total_emission_df['income_mean'].nunique()

# %%
total_emission_df.describe()






# %%
