import numpy as np

def is_dirt_detected(output_data):
    # Example logic for dirt detection using ACIN model
    return output_data[0] > 0.5  # Threshold for dirt detection

def is_trash_detected(output_data):
    # Example logic for trash detection using TrashNet model
    return np.argmax(output_data) != 0  # Assume 0 is 'no trash'
