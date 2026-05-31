import cv2

def show_difference(original, encoded):

    img1 = cv2.imread(original)
    img2 = cv2.imread(encoded)

    difference = cv2.absdiff(img1, img2)

    # cv2.imshow("Difference", difference)
    cv2.imwrite('images/output/difference.png', difference)
    cv2.waitKey(0)