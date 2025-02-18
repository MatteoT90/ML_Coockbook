from transformers import pipeline
import torch
from accelerate.test_utils.testing import get_backend
from PIL import Image
import matplotlib.pyplot as plt


def main():
    # automatically detects the underlying device type (CUDA, CPU, XPU, MPS, etc.)
    device, _, _ = get_backend()
    checkpoint = "depth-anything/Depth-Anything-V2-base-hf"
    pipe = pipeline("depth-estimation", model=checkpoint, device=device)

    image = Image.open('/home/mtoso/Documents/Code/CV_CoockBook/DepthEstimation/example_image.png')
    plt.imshow(image)
    plt.show()
    plt.close()

    predictions = pipe(image)
    depthmap = predictions["depth"]
    plt.imshow(depthmap, cmap='viridis')
    plt.imsave('/home/mtoso/Desktop/depthmap.png', depthmap, cmap='viridis')
    # plt.show()


    return

if __name__ == "__main__":
    main()
