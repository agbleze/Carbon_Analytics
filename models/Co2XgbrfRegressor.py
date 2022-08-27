#%%
from xgboost import XGBRFRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_validate, cross_val_score, cross_val_predict
import joblib 
from models.preprocess_pipeline import (decision_tree_data_preprocess, 
                                        X_train, 
                                        X_test, 
                                        y_train,
                                        y_test
                                        )


# from preprocess_pipeline import (decision_tree_data_preprocess, 
#                                         X_train, 
#                                         X_test, 
#                                         y_train,
#                                         y_test, X, y
#                                         )

xgb = XGBRFRegressor()
xgb_pipeline = make_pipeline(decision_tree_data_preprocess, xgb)
    
    
if __name__ == '__main__':
    
    xgb_pipeline.fit(X=X_train, y=y_train)

    y_pred_xgb = xgb_pipeline.predict(X_test)
    rmse = mean_squared_error(y_true=y_test, y_pred=y_pred_xgb, squared=False)
    print(f'Xggbrf test rmse: {rmse}')
    
    joblib.dump(value=xgb_pipeline, filename='model_used.model')


    #xgb_pipeline('xgb_model.py')
    
    
#%%
import pandas as pd
dat = {'state_name': 'kano', 'lga': 123, 'sector': 'RURAL', 'credit_mean': 123, 'income_mean': 120}
input_pred = pd.DataFrame(data=dat, index=[0])
#pd.DataFrame.from_dict(data=dat)

# %%
xgb_pipeline.predict(input_pred)[0]










# %%
