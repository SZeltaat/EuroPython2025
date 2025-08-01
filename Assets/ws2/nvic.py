import nvidia.nvimgcodec as nvic
import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor

batch_size = 48
max_workers = 8
encoded_image = np.fromfile("res/grand_piano.jpg", np.uint8)
encoded_batch = np.stack([encoded_image] * batch_size)
test_image_shape = (2763, 4912, 3)

from multiprocessing import get_context

spawn_ctx = get_context("spawn")


def decode_image_nvic_to_numpy(encoded_image):
    img = nvic_decoder.decode(encoded_image)
    return np.array(img.cpu())


def _init_nvic_worker():
    global nvic_decoder
    nvic_decoder = nvic.Decoder()


def parallel_decoding_nvic(encoded_batch):
    result = []
    with ProcessPoolExecutor(
        max_workers=max_workers,
        initializer=_init_nvic_worker,
        mp_context=spawn_ctx,
    ) as executor:
        for dec in executor.map(decode_image_nvic_to_numpy, encoded_batch):
            result.append(dec)
    return result


def test():
    decoded_images_nvic = parallel_decoding_nvic(encoded_batch)
    for img in decoded_images_nvic:
        assert img.shape == test_image_shape
    print("Test passed!")


def time():
    parallel_decoding_nvic(encoded_batch)


if __name__ == "__main__":
    test()
