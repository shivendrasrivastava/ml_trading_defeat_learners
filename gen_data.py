"""Generate data to fool learners"""

import numpy as np


def best4LinReg(seed=np.random.randint(1000000)):
    """This function should return a dataset (X and Y) that will work
    better for linear regression than decision trees

    Parameters: 
    seed: Random integer used to initialize the pseudo-random number generator. 
    Whenever the seed is the same, the same data set will be returned. 
    Different seeds should result in different data sets.

    Returns: 
    X: A numpy ndarray of X values
    Y: A numpy 1D array of Y values
    """

    np.random.seed(seed)

    # X and Y should each contain from 10 to 1000 rows
    num_rows = np.random.randint(10, 1001)

    # X should have from 2 to 1000 columns
    num_X_cols = np.random.randint(2, 1001)

    X = np.random.normal(size=(num_rows, num_X_cols))
    Y = np.zeros(num_rows)
    for col in range(num_X_cols):
        Y += X[:, col]

    return X, Y


def best4DT(seed=np.random.randint(1000000)):
    """This function should return a dataset (X and Y) that will work
    better for decision trees than linear regression

    Parameters: 
    seed: Random seed used to initialize the pseudo-random number generator. 
    Whenever the seed is the same, the same data set will be returned. 
    Different seeds should result in different data sets.

    Returns: 
    X: A numpy ndarray of X values
    Y: A numpy 1D array of Y values
    """

    np.random.seed(seed)
    
    # X and Y should each contain from 10 to 1000 rows
    num_rows = np.random.randint(10, 1001)

    # X should have from 2 to 1000 columns
    num_X_cols = np.random.randint(2, 1001)

    X = np.random.normal(size=(num_rows, num_X_cols))
    Y = np.zeros(num_rows)
    for col in range(num_X_cols):
        Y += X[:, col] ** 2
    
    return X, Y


if __name__=="__main__":
    print ("Generate data that works better for one learner than the other")