from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from models.preprocess_pipeline import decision_tree_data_preprocess

rf = RandomForestRegressor(random_state=0)
rf_pipeline = make_pipeline(decision_tree_data_preprocess, rf)



if __name__ == '__main__':
    pass




