import cv2
import numpy as np
from matplotlib import pyplot as plt

# ref
# https://github.com/afikanyati/cadenCV

def match(img, templates, threshold ):
    img_width, img_height = img.shape[::-1]

    start_percent = 50
    stop_percent = 150 
    

    best_locations = []
    best_scale = 1

    for scale in [i/100.0 for i in range(start_percent, stop_percent, 5)]:
        locations = []

        for template in templates:
            if (scale*template.shape[0] > img.shape[0] or scale*template.shape[1] > img.shape[1]):
                break

            template = cv2.resize(template, None, fx = scale, fy = scale, interpolation = cv2.INTER_CUBIC)
            result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            result = np.where(result >= threshold)
            locations += [result]

        if ( len(locations)  > len(best_locations)):
            best_locations = locations
            best_scale = scale
        
    return best_locations, best_scale

def locate_templates(img, templates, threshold = 0.7):
    locations, scale = match(img, templates,threshold)
    real_locations = []

    for i in range(len(templates)):
        w = int(templates[i].shape[1] * scale)
        h = int(templates[i].shape[0] * scale)
        for pt in zip(*locations[i][::-1]):
            real_locations.append([  pt[0], pt[1], pt[0] + w, pt[1] + h])
    return real_locations


def quater_notes_match(img_gray, threshold = 0.7):
    quarter_note_imgs = [cv2.imread(quarter, 0) for quarter in ["resources/template/note/quarter.png","resources/template/note/solid-note.png"]]

    points = locate_templates(img_gray, quarter_note_imgs,threshold)

    return points
    # cv2.imwrite('res1.png',boxes)

def half_notes_match(img_gray, threshold = 0.7):
    half_note_imgs = [cv2.imread(quarter, 0) for quarter in ["resources/template/note/half-space.png","resources/template/note/half-note-line.png","resources/template/note/half-line.png","resources/template/note/half-note-space.png"]]

    points = locate_templates(img_gray, half_note_imgs, threshold)
    return points
    # cv2.imwrite('res2.png',boxes)

def whole_notes_match(img_gray, threshold = 0.7):
    whole_note_imgs = [cv2.imread(quarter, 0) for quarter in ["resources/template/note/whole-space.png","resources/template/note/whole-note-line.png","resources/template/note/whole-line.png","resources/template/note/whole-note-space.png"]]

    points = locate_templates(img_gray, whole_note_imgs,threshold)
    return points

def match_all(img_gray):
    quater_points = quater_notes_match(img)
    half_points = half_notes_match(img)
    whole_points = whole_notes_match(img)

    print(quater_points)
    print(half_points)
    print(whole_points)

    res = quater_points + half_points + whole_points
    return res



def clef_match(img_gray):
    clef_img = [cv2.imread(quarter, 0) for quarter in ["resources/template/clef/treble_1.jpg","resources/template/clef/treble_2.jpg","resources/template/clef/treble_3.jpg"]]
    point = locate_templates(img_gray, clef_img, 0.4)
    return point
        
# img_file = "/Users/ejahn1/Desktop/test9.png"
# img = cv2.imread(img_file, 0)
# print(whole_notes_match(img))
# cv2.imwrite('res.png',quarter_boxes)
