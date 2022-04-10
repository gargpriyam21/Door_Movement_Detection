import numpy as np

def feature1(window):
    """
    Function to fetch 3 featured from the given window
        Feature 1: Mean of Accelerometer x
        Feature 2: Mean of Accelerometer y
        Feature 3: Mean of Gyroscope z
    Arguments:
        window: window for the feature extraction
    """
    if len(window) == 0:
        return None
    feature = []
    mean_values = np.mean(window, axis=0)
    # print(window)
    feature.append(mean_values[1])
    feature.append(mean_values[3])
    feature.append(mean_values[5])

    return feature


def select_features_from_window(window):
    """
    Function fetch main features from the given window
    Arguments:
        window: window for the feature extraction
    """

    f = feature1(window)
    return f


def create_feature_vector(sample, splits):
    """
    Function to create the feature vector from the given data and creating the features
    Arguments:
        sample: sample data for the feature extraction
        splits: number of splits in which the data is to be splitted
    """

    feature_vector = []
    if len(sample) < splits:
        #         feature_vector.append(select_features_from_window(np.array(sample)))
        return feature_vector
    to_split_data = np.array(sample[:int(len(sample) // splits) * splits])
    splitted_samples = np.split(to_split_data, splits)
    for i, window in enumerate(splitted_samples):
        if i == len(splitted_samples) - 1 and len(sample[int(len(sample) // splits) * splits:]) > 0:
            window = np.vstack((window, sample[int(len(sample) // splits) * splits:]))
        features = select_features_from_window(window)
        if features:
            feature_vector.append(features)

    debug = ' '.join([str(len(x)) for x in feature_vector])
    #     print(len(feature_vector), " ", debug)
    return feature_vector


def create_data(samples, splits):
    """
    Function to create the data from the given samples into the required splits
    Arguments:
        samples: sample data for the feature extraction
        splits: number of splits in which the data is to be splitted
    """
    data = []
    i = 0
    for sample in samples:
        f_vector = create_feature_vector(sample, splits)
        if f_vector != []:
            data.append(f_vector)
    #     print(data)
    data = np.array(data)
    #     print(data.shape)
    data = data.reshape(data.shape[0], data.shape[1] * data.shape[2])
    #     print(data.shape)

    return data

