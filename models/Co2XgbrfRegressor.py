from xgboost import XGBRFRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_validate, cross_val_score, cross_val_predict
import joblib 
# from models.preprocess_pipeline import (decision_tree_data_preprocess, 
#                                         X_train, 
#                                         X_test, 
#                                         y_train,
#                                         y_test
#                                         )


from preprocess_pipeline import (decision_tree_data_preprocess, 
                                        X_train, 
                                        X_test, 
                                        y_train,
                                        y_test, X, y
                                        )

xgb = XGBRFRegressor()
xgb_pipeline = make_pipeline(decision_tree_data_preprocess, xgb)
    
    
if __name__ == '__main__':
    
    xgb_pipeline.fit(X=X_train, y=y_train)

    y_pred_xgb = xgb_pipeline.predict(X_test)
    rmse = mean_squared_error(y_true=y_test, y_pred=y_pred_xgb, squared=False)
    print(f'Xggbrf test rmse: {rmse}')


    xgb_pipeline.export('xgb_model.py')
    
    

