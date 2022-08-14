# fit a knn regressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

import pandas as pd

from models.preprocess_pipeline import linear_model_preprocess_pipeline



knn = KNeighborsRegressor(n_neighbors=10)

knn_model_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)

#%%
knn_model_pipeline.fit(X=X_raw_train, y=y_raw_train)

#
y_pred_knn = knn_model_pipeline.predict(X_raw_test)

#%%
mean_squared_error(y_true=y_raw_test, y_pred=y_pred_knn, squared=False)

#%%
knn_results = []
for nn in range(1, 30):
  knn_schedule = KNeighborsRegressor(n_neighbors=nn)
  knn_schedule_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)
  knn_schedule_pipeline.fit(X=X_raw_train, y=y_raw_train)
  y_pred = knn_schedule_pipeline.predict(X_raw_test)
  rmse = mean_squared_error(y_true=y_raw_test, y_pred=y_pred, squared=False)
  knn_results.append({'k-neighbors': nn, 'rmse': rmse})
    
results = pd.DataFrame(data=knn_results