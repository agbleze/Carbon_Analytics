#%%
from sklearn.ensemble import HistGradientBoostingRegressor
from models.preprocess_pipeline import decision_tree_data_preprocess
from sklearn.pipeline import make_pipeline


hgb = HistGradientBoostingRegressor(random_state=0)
hgb_pipeline = make_pipeline(decision_tree_data_preprocess, hgb)





