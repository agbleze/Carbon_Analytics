from Co2KnnRegressor import knn_rmse_test
# make ridgecv model and stack all models together
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import  StackingRegressor
from sklearn.model_selection import train_test_split
from Co2Rfregressor import rf_pipeline
from Co2LassoRegressor import lasso_pipeline
from Co2KnnRegressor import knn_pipeline
from Co2RidgeRegressor import rd_pipeline

from Co2HistgradientImputed import hgb_pipeline
from sklearn.metrics import  mean_squared_error, r2_score
from preprocess_pipeline import (X_train, 
                                X_test, 
                                y_train,
                                y_test
                                )


ridge = RidgeCV()
all_models = [("Radom Forest", rf_pipeline),
              ("Lasso", lasso_pipeline),
              ("Gradient Boosting", hgb_pipeline)
              ]
stack_regressors = StackingRegressor(estimators=all_models, final_estimator=ridge)


print(knn_rmse_test)