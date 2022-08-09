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
                                       ) >>
                     all.replace_na(dict(CHARCOAL = 0, KEROSENE = 0, GAS = 0, 
                                         ELECTRICITY = 0,FIREWOOD = 0, 
                                         PETROL = 0, DIESEL = 0
                                         )
                                    )
                    )


#%%
fuel_data_harvest_sum = (fuel_data_harvest.groupby(by=['state', 'lga', 'hhid'])
                         ["CHARCOAL", "DIESEL", "ELECTRICITY",
                         "KEROSENE","GAS", "PETROL"]
                         .agg('sum')
                         .reset_index()
                        )

#%%
### estimate co2 emission for petrol at household level
petrol_data_harvet_CO2emission = (fuel_data_harvest_sum >> 
                                  dplyr.select(f[0:3], f.PETROL) >>
                                    dplyr.mutate(petrol_total_expend = f.PETROL,
                                                price_per_ltr = 87, 
                                                total_ltr_consumed = (f.petrol_total_expend / f.price_per_ltr), 
                                                GHG_emission_factor_CO2 = 2.31,
                                                petrol_total_CO2_emitted_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2)
                                                )
                            )

#%%
### estimate co2 emission for kerosene at household level
kerosene_data_harvest_CO2emission = (fuel_data_harvest_sum >> dplyr.select(f[0:3], f.KEROSENE) >>
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
                                  dplyr.select(f[0:3], f.GAS) >>
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
                                        dplyr.select(f[0:3], f.ELECTRICITY) >>
                                        dplyr.mutate(electricity_total_expend = f.ELECTRICITY, 
                                                    price_per_KWh = 29, 
                                                    total_KWh_consumed = (f.electricity_total_expend/f.price_per_KWh),
                                                    GHG_emission_factor_CO2 = 0.4034043, 
                                                    electricity_total_CO2_emitted_kg = (f.total_KWh_consumed * f.GHG_emission_factor_CO2)
                                                    )
                                     )

#%%
## estimate co2 emission for charcoal at household level
charcoal_data_harvest_co2emission = (fuel_data_harvest_sum >> dplyr.select(f[0:3], f.CHARCOAL) >>
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
                                   dplyr.select(f[0:3], f.DIESEL) >>
                                    dplyr.mutate(diesel_total_expend = f.DIESEL, 
                                                price_per_ltr = 145, 
                                                total_ltr_consumed = (f.diesel_total_expend / f.price_per_ltr),
                                                GHG_emission_factor_CO2kg_per_ltr = 2.676492,
                                                diesel_total_CO2_emitted_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2kg_per_ltr)
                                            )
                                 )



#%%
# ASSIGN FUEL name to fuel eg df['PETRO'] = 'petrol'
# Rename fuel to 'fuel_type' eg df.rename(columns='fuel_type')

#%%
df_merge = pd.concat([petrol_data_harvet_CO2emission,kerosene_data_harvest_CO2emission, lpgas_data_harvest_CO2emission,
           electricity_data_harvest_CO2emission, charcoal_data_harvest_co2emission, diesel_data_harvest_co2emission
           ])

# %%
#df_merge['PETROL'] = 'petrol'

###
'''
TO DO:
1. Find sum of total co2
2. format emission base on fuel type

'''
