#%%
from sklearn.ensemble import HistGradientBoostingRegressor
from models.preprocess_pipeline import decision_tree_data_preprocess
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from models.preprocess_pipeline import (X_train, 
                                 X_test, 
                                 y_train,
                                 y_test
                                )


hgb = HistGradientBoostingRegressor(random_state=0)
hgb_pipeline = make_pipeline(decision_tree_data_preprocess, hgb)


if __name__ == '__main__':
        #%% histgradientboosting
    hgb_pipeline.fit(X_train, y_train)
    y_pred_hgb = hgb_pipeline.predict(X_test)
    rmse = mean_squared_error(y_true=y_test, y_pred=y_pred_hgb, squared=False)
    print(f'Histgradientboosting with mean imputed values RMSE: {rmse}')



