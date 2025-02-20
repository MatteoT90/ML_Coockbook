import json
import numpy as np
import matplotlib.pyplot as plt

def main():

    # Load the camera parameters
    with open('CameraTransformations/train_camera.json') as f:
        train_data = json.load(f)
    with open('CameraTransformations/test_camera.json') as f:
        test_data = json.load(f)

    # Load the numpy data generated from Myrna, just to check what they are. REMOVE THIS LATER
    train_data_np = np.load('CameraTransformations/train_camera.npy')
    test_data_np = np.load('CameraTransformations/test_camera.npy')

    # Check the data
    print(train_data)
    
    # How to read the json data
    camera_transformations = [x['transform_matrix'] for x in train_data['frames']]
    # TODO: check which of the below lines is correct
    centers = np.array([np.array(x)[:3,3] for x in camera_transformations])
    # centers = np.array([np.linalg.inv(np.array(x))[:3,3] for x in camera_transformations])

    camera_transformations_train = [x['matrix'] for x in test_data['keyframes']]
    centers_test = np.array([np.array(json.loads(x)).reshape(4,4) for x in camera_transformations_train])[:,3,:3]

    # Do a 3D scatterplot of the numpy data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(centers[:,0], centers[:,1], centers[:,2], c='r', marker='o')
    ax.scatter(centers_test[:,0], centers_test[:,1], centers_test[:,2], c='b', marker='o')
    
    # Connect adjacent points in the sequence
    ax.plot(centers[:,0], centers[:,1], centers[:,2], color='r')
    ax.plot(centers_test[:,0], centers_test[:,1], centers_test[:,2], color='b')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

    return


if __name__ == "__main__":
    main()
