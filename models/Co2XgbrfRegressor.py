from xgboost import XGBRFRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from preprocess_pipeline import (decision_tree_data_preprocess, 
                                    X_train, 
                                    X_test, 
                                    y_train,
                                    y_test
                                )

if __name__ == '__main__':
    xgb = XGBRFRegressor()
    xgb_pipeline = make_pipeline(decision_tree_data_preprocess, xgb)
    xgb_pipeline.fit(X=X_train, y=y_train)

    y_pred_xgb = xgb_pipeline.predict(X_test)
    rmse = mean_squared_error(y_true=y_test, y_pred=y_pred_xgb, squared=False)
    print(f'Xggbrf: {rmse}')

