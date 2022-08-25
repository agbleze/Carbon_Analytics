from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from models.preprocess_pipeline import (decision_tree_data_preprocess,
                                 X_train, 
                                 X_test, 
                                 y_train,
                                 y_test
                                )

rf = RandomForestRegressor(random_state=0)
rf_pipeline = make_pipeline(decision_tree_data_preprocess, rf)



if __name__ == '__main__':
        #%% rf prediction
    rf_pipeline.fit(X_train, y_train)

    #%%
    y_pred_rf = rf_pipeline.predict(X_test)
    rf_rmse_test = mean_squared_error(y_true=y_test, y_pred=y_pred_rf, squared=False)
    print(f'Random forest test RMSE: {rf_rmse_test}')





