#%% import packages
import pandas as pd
import datar as dr
from datar import dplyr, f
from datar import tidyr
import datar.all as all
import datar.base as base


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






#%% focus on only hhid with emission data for at leats 1 fuel type that is co2 > 0
total_emission_df = emission_df[emission_df['total_CO2_kg'] > 0]


# %%
total_emission_df['income_mean'].nunique()

# %%
total_emission_df.describe()






# %%
