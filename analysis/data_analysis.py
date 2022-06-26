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
petrol_data_harvet_CO2emission = (fuel_data_harvest_sum >> dplyr.select(f[0:3], f.PETROL) >>
                            dplyr.mutate(petrol_total_expend = f.PETROL,
                                         price_per_ltr = 87, 
                                         total_ltr_consumed = (f.petrol_total_expend / f.price_per_ltr), 
                                         GHG_emission_factor_CO2 = 2.31,
                                         total_CO2_produced_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2)
                                         )
                            )

#%%
### estimate co2 emission for kerosene at household level
kerosene_data_harvest_CO2emission = (fuel_data_harvest_sum >> dplyr.select(f[0:3], f.KEROSENE) >>
                          dplyr.mutate(kerosene_total_expend = f.KEROSENE,
                                       price_per_ltr = 50,
                                       total_ltr_consumed = (f.kerosene_total_expend/f.price_per_ltr),
                                       GHG_emission_factor_CO2 = 2.5,
                                       total_CO2_produced_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2)
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
                                                total_CO2_produced_kg = (f.total_ltr_consumed * f.GHG_emission_factor_CO2)
                                                )
                                )









