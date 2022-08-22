# make ridgecv model and stack all models together
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import  StackingRegressor
from sklearn.model_selection import train_test_split
from Co2Rfregressor import rf_pipeline
from Co2LassoRegressor import lasso_pipeline
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


#%%
# X_all_raw = total_emission_df[['state',	'lga',	'sector',	'credit_mean',	'income_mean']]

# #%%
# X_raw_train, X_raw_test, y_raw_train, y_raw_test = train_test_split(X_all_raw, y, test_size=0.3, random_state=0)

#%%
if __name__ == '__main__':
    stack_regressors.fit(X=X_train, y=y_train)

    #%%
    y_pred_stack = stack_regressors.predict(X_test)

    #%%
    rmse = mean_squared_error(y_true=y_test, y_pred=y_pred_stack, squared=False)
    print(f'Stacked models test RMSE: {rmse}')

