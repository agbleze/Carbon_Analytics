from sklearn.linear_model import RidgeCV
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from models.preprocess_pipeline import (linear_model_preprocess_pipeline,
                                 X_train, 
                                 X_test, 
                                 y_train,
                                 y_test
                                )

#%% ridged model
rd = RidgeCV(cv=10)
rd_pipeline = make_pipeline(linear_model_preprocess_pipeline, rd)

#%%
if __name__ == '__main__':
    rd_pipeline.fit(X=X_train, y=y_train)

    #%%
    y_pred_rd = rd_pipeline.predict(X_test)
    rd_reg_rmse_test = mean_squared_error(y_true=y_test, y_pred=y_pred_rd, squared=False)
    print(f'Ridged regression test RMSE: {rd_reg_rmse_test}')



