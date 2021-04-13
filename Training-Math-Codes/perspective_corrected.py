import cv2 as cv
import numpy as np


def get_perspective_transformation(img, src, dst, size):
    source_coord = np.float32(src)
    destination_coord = np.float32(dst)
    map_matrix = cv.getPerspectiveTransform(source_coord, destination_coord)
    img_result = cv.warpPerspective(img, map_matrix, size)
    return img_result


def show_img(original_img, transformed_img, original_name, transformed_name):
    cv.imshow(original_name, original_img)
    cv.imshow(transformed_name, transformed_img)
    cv.waitKey(0)


img1 = cv.imread("softuni.jpg")
src1 = [(209, 260), (407, 161), (418, 438), (605, 270)]
dst1 = [(0, 0), (500, 0), (0, 500), (500, 500)]
size1 = 500, 500
perspective_corrected_img = get_perspective_transformation(img1, src1, dst1, size1)
show_img(img1, perspective_corrected_img, "Original", "Perspective Corrected")

img2 = cv.imread("card.jpg")
src2 = [(292, 2), (445, 270), (43, 135), (256, 349)]
dst2 = [(0, 0), (400, 0), (0, 250), (400, 250)]
size2 = 400, 250
perspective_corrected_img = get_perspective_transformation(img2, src2, dst2, size2)
show_img(img2, perspective_corrected_img, "Original", "Perspective Corrected")

