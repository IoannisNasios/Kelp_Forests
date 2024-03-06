import os
def create_dir(path):
    if os.path.isdir(path)==False:
        os.makedirs(path)
        
        
# CONFIGURE 

# Set Data Paths
test_path='test_satellite/'
train_path='train_satellite/'
labels_path='train_kelp/'


# Create directories
# test_predmask_path='test_kelp/'
# create_dir(test_predmask_path)

# set weights directory for new training saving
weights_path='weights/'
# create_dir(weights_path)


RETRAIN= False # if true retrain else use trained weights for inference
trained_weights = 'trained_weights/' # meaningful only when RETRAIN=False


# directory for prediction probabilities 
test_preds_dir = 'test_preds/'
# create_dir(test_preds_dir)

test_predmask_path='test_kelp/'
# create_dir(test_predmask_path)
