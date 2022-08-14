#%%
from sklearn.ensemble import HistGradientBoostingRegressor
from models.preprocess_pipeline import decision_tree_data_preprocess
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error


hgb = HistGradientBoostingRegressor(random_state=0)
hgb_pipeline = make_pipeline(decision_tree_data_preprocess, hgb)


if '__name__' == '__main__':
        #%% histgradientboosting
    hgb_pipeline.fit(X_raw_train, y_raw_train)
    y_pred_hgb = hgb_pipeline.predict(X_raw_test)
    mean_squared_error(y_true=y_raw_test, y_pred=y_pred_hgb, squared=False)



