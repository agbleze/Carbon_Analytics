from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from models.preprocess_pipeline import decision_tree_data_preprocess

rf = RandomForestRegressor(random_state=0)
rf_pipeline = make_pipeline(decision_tree_data_preprocess, rf)



if __name__ == '__main__':
        #%% rf prediction
    rf_pipeline.fit(X_raw_train, y_raw_train)

    #%%
    y_pred_rf = rf_pipeline.predict(X_raw_test)
    mean_squared_error(y_true=y_raw_test, y_pred=y_pred_rf, squared=False)





