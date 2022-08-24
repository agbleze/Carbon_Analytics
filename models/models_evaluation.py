
#%%
#from Co2KnnRegressor import knn_rmse_test
# make ridgecv model and stack all models together
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import  StackingRegressor
from sklearn.model_selection import train_test_split
from Co2Rfregressor import rf_pipeline
from Co2LassoRegressor import lasso_pipeline
from Co2KnnRegressor import knn_pipeline
from Co2RidgeRegressor import rd_pipeline
from Co2Svr import svr_rbf_pipeline
from Co2XgbrfRegressor import xgb_pipeline

from Co2HistgradientImputed import hgb_pipeline
from sklearn.metrics import  mean_squared_error, r2_score
from preprocess_pipeline import (X_train, 
                                X_test, 
                                y_train,
                                y_test,
                                X, y
                                )

import pandas as pd

#from sklearn.metrics import cross_validation
from sklearn.model_selection import cross_validate, cross_val_score, cross_val_predict

ridge = RidgeCV()
all_models = [("Radom Forest", rf_pipeline),
              ("Lasso", lasso_pipeline),
              ("Hist Gradient Boosting", hgb_pipeline),
              ("Extreme Gradient Boosting Random Forest", xgb_pipeline),
              ("KNN k=5", knn_pipeline),
              #("Ridge", rd_pipeline),
              ("SVR rbf", svr_rbf_pipeline)
              ]
stack_regressors = StackingRegressor(estimators=all_models, final_estimator=ridge)

candidate_models = all_models.copy()

candidate_models.extend([("Ridge", rd_pipeline), ('stacked_models', stack_regressors)])
import math 
if __name__ == '__main__':
    test_score_dict = []
    for model_name, mod_pipeline in all_models:              
        score = cross_validate(estimator=mod_pipeline,
                               X=X, y=y, cv=10,
                        scoring=('neg_mean_squared_error'),
                        return_train_score=False)
        test_score_dict = {'model': model_name, 'test_score': -(score['test_score'])}
        # test_score_dict['model'] = model_name
        # test_score_dict['test_score'] =  -(score['test_score'])
        #test_score_dict.append({'model': 'KNN', 'test_score': -(score['test_score'])})
    df = pd.DataFrame(data=test_score_dict)
    #df['test_RMSE'] = df['test_score'].apply(lambda x: math.sqrt(x))
    #df.drop(columns='test_score', inplace=True)
    print(df)
    #    print(model_name, mod_pipeline)
    #print(candidate_models)
        
        

# %%
#%%
# for ax, (name, est) in zip(axs, all_models + [('Stacking Regressor', stack_regressors)]):
#   start_time = time.time()
#   score = cross_validate(est, X_train, y_train,
#                          scoring=['r2', 'neg_mean_absolute_error'],
#                          n_jobs=2, verbose=0
#                          )
#   elapsed_time = time.time() - start_time
  
#   y_pred = cross_val_predict(est, X_train, y_train, 
#                              n_jobs=2, verbose=1)
  