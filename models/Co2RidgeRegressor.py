from sklearn.linear_model import RidgeCV
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

from models.preprocess_pipeline import linear_model_preprocess_pipeline

#%% ridged model
rd = RidgeCV(cv=10)
rd_pipeline = make_pipeline(linear_model_preprocess_pipeline, rd)

#%%
if '__name__' == '__main__':
    rd_pipeline.fit(X=X_raw_train, y=y_raw_train)

    #%%
    y_pred_rd = rd_pipeline.predict(X_raw_test)
    mean_squared_error(y_true=y_raw_test, y_pred=y_pred_rd, squared=False)



