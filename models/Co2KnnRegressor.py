
#%% fit a knn regressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from preprocess_pipeline import (linear_model_preprocess_pipeline, 
                                        X_train, 
                                        X_test, 
                                        y_train,
                                        y_test
                                        )
import pandas as pd

knn = KNeighborsRegressor(n_neighbors=10)

knn_model_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)

#%%
knn_model_pipeline.fit(X=X_train, y=y_train)

#
y_pred_knn = knn_model_pipeline.predict(X_test)

#%%
mean_squared_error(y_true=y_test, y_pred=y_pred_knn, squared=False)

#%%
knn_results = []
for nn in range(1, 30):
  knn_schedule = KNeighborsRegressor(n_neighbors=nn)
  knn_schedule_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)
  knn_schedule_pipeline.fit(X=X_train, y=y_train)
  y_pred = knn_schedule_pipeline.predict(X_test)
  rmse = mean_squared_error(y_true=y_test, y_pred=y_pred, squared=False)
  knn_results.append({'k-neighbors': nn, 'rmse': rmse})
    
results = pd.DataFrame(data=knn_results)
#print(results)


if __name__ == '__main__':
  
  knn = KNeighborsRegressor(n_neighbors=5)
  knn_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)
  knn_pipeline.fit(X=X_train, y=y_train)
  y_pred = knn_pipeline.predict(X_test)
  knn_rmse_test = mean_squared_error(y_true=y_test, y_pred=y_pred, squared=False)
  knn_r2_train = r2_score(y_true=y_train, y_pred=knn_pipeline.predict(X_train))
  
  print(f'KNN Test RMSE: {knn_rmse_test}')
  print(f'KNN train R2: {knn_r2_train}')
  
  
  