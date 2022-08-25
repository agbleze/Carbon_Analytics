#%%
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from models.preprocess_pipeline import (linear_model_preprocess_pipeline, 
                                        X_train, 
                                        X_test, 
                                        y_train,
                                        y_test
                                        )
import pandas as pd


svr_rbf = SVR(kernel='linear')

svr_rbf_pipeline = make_pipeline(linear_model_preprocess_pipeline,
                                 svr_rbf)

#%%

if __name__ == '__main__':
    
    #df = pd.read_csv(r'../data/total_emission_df.csv')
    
    svr_rbf_pipeline.fit(X=X_train, y=y_train)

    #%%
    y_pred_svrrbd = svr_rbf_pipeline.predict(X_test)

    rmse = mean_squared_error(y_true=y_test, y_pred=y_pred_svrrbd, squared=False)
    r2 = r2_score(y_true=y_train, y_pred=svr_rbf_pipeline.predict(X_train))
    print(f'SVR test rmse: {rmse}')
    print(f'SVR train R2: {r2}')




