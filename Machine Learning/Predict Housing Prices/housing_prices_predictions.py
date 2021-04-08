import logging # print out logs to file
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Configure olog output
logging.basicConfig(format= '%(asctime)s %(message)s', filename='housing_prices_predictions.log', level=logging.INFO)

# Load dataset into Dataframe
home_data = pd.read_csv(r'housing_prices_Iowa.csv')

# Filter rows with missing values
# home_data = home_data.dropna(axis=0) NOT NEEDED - clean dataset

# Set target prediction (saleprice = y)  (get the exact name of columns first)
y = home_data.SalePrice

# set the features list X (Check log file housing_prices_predictions.txt for detailed log of feature testing)
features = ['MSSubClass','LotArea', 'OverallQual', 'OverallCond','YearBuilt','1stFlrSF', '2ndFlrSF',
            'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
logging.info(f'Features Used: {features}')
X = home_data[features]

# Split data for testing and validation (Set random state to a number)
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify model
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit model
iowa_model.fit(train_X, train_y)

# Make validation prediction and calculate mean absolute error MAE
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
logging.info(f'Initial Mean_Absolute_Error: {val_mae}')

# Write a get_mae function to calculate the optimum max_leaf_nodes for the best mae
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_value = model.predict(val_X)
    mae = mean_absolute_error(preds_value, val_y)
    return mae

# Call the get_mae function on each value of max_leaf_nodes. Store the output in some way that allows you to select the
# value of max_leaf_nodes that gives the most accurate model on your data.
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
values = {node: get_mae(node, train_X, val_X, train_y, val_y) for node in candidate_max_leaf_nodes}
best_tree_size = min(values, key=values.get)
logging.info(f'best tree size: {best_tree_size}')

# Edit the model with the new best_tree_size parameter
best_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=1)
best_model.fit(X, y)

# Predict with the new model
best_predict = best_model.predict(X)

# Get the new MAE
logging.info(f'Lowest Mean_absolute_error: {mean_absolute_error(y, best_predict)}')

# Now try the model with RandomForest module
from sklearn.ensemble import RandomForestRegressor

# Define the model
rf_model = RandomForestRegressor(random_state= 1)

# fit the data
rf_model.fit(train_X, train_y)

# Predict the data
rf_model_predictions = rf_model.predict(val_X)

# get the mean absolute error of the new model
rf_model_mae = mean_absolute_error(rf_model_predictions, val_y)
logging.info(f'Mean_absolute_error of RandomForest model: {rf_model_mae}')
logging.info('-'*20+'END OF THIS TRIAL'+'-'*20)

