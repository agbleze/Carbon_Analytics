
#%% fit a knn regressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, r2_score
from models.preprocess_pipeline import (linear_model_preprocess_pipeline, 
                                        X_train, 
                                        X_test, 
                                        y_train,
                                        y_test
                                        )
import pandas as pd
import numpy as np
import math

from sklearn.model_selection import cross_validate

knn = KNeighborsRegressor(n_neighbors=10)

knn_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)

#%%
# knn_pipeline.fit(X=X_train, y=y_train)

# #
# y_pred_knn = knn_pipeline.predict(X_test)

#%%
#mean_squared_error(y_true=y_test, y_pred=y_pred_knn, squared=False)

#%%
# knn_results = []
# for nn in range(1, 30):
#   knn_schedule = KNeighborsRegressor(n_neighbors=nn)
#   knn_schedule_pipeline = make_pipeline(linear_model_preprocess_pipeline, knn)
#   knn_schedule_pipeline.fit(X=X_train, y=y_train)
#   y_pred = knn_schedule_pipeline.predict(X_test)
#   rmse = mean_squared_error(y_true=y_test, y_pred=y_pred, squared=False)
#   knn_results.append({'k-neighbors': nn, 'rmse': rmse})
    
# results = pd.DataFrame(data=knn_results)
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
  
  for count, value in [(12, 'eg'), (1, 'testcase')]:
    print(count, value) 
    
  test_score_dict = {}
  score = cross_validate(estimator=knn_pipeline, X=X_train, y=y_train, cv=10,
                 scoring=('neg_mean_squared_error'),
                 return_train_score=False)
  #test_score_dict = {'model': 'KNN', 'test_score': -(score['test_score'])}
  test_score_dict['model'] = 'KNN'
  test_score_dict['test_score'] =  -(score['test_score'])
  df = pd.DataFrame(data=test_score_dict)
  df['test_RMSE'] = df['test_score'].apply(lambda x: math.sqrt(x))
  df.drop(columns='test_score', inplace=True)
  print(df)
  #print(score['test_score'])
  
  
  