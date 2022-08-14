# make lasso model
from sklearn.linear_model import LassoCV
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error
from models.preprocess_pipeline import linear_model_preprocess_pipeline
import numpy as np



lasso_pipeline = make_pipeline(linear_model_preprocess_pipeline,
                               LassoCV()
                               )

#%%
#LassoCV()._get_param_names

if __name__ == '__main__':
    linear_param_set = {'alpha': np.arange(0.0001, 1, 0.001),
                        'selection': ['cyclic', 'random'],
                        'eps': np.arange(0.0001, 1, 0.001),
                        'tol': np.arange(0.0001, 1, 0.001),
                        'n_alpha': range(100, 1000, 100)
                    }

    #%% lasso prediction
    lasso_pipeline.fit(X_raw_train, y_raw_train)

    #%%
    y_pred_lasso = lasso_pipeline.predict(X_raw_test)

    mean_squared_error(y_true=y_raw_test, y_pred=y_pred_lasso, squared=False)



