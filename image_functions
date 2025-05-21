from PIL import Image
import math

# PART X================

def matrix_addition(a, b):
    for i in range(len(a)):  # checking if a is a matrix
        if len(a[i]) != len(a[0]):
            print('a not a matrix')
            return None
    for i in range(len(b)):  # checking if b is a matrix
        if len(b[i]) != len(b[0]):
            print('b not a matrix')
            return None
    if len(a) != len(b):  # checking if the amount of rows is equal
        print(f'a has {len(a)} rows and b has {len(b)} rows. incorrect')
        return None
    if len(a[0]) != len(b[0]):  # checking if the amount of columns is equal
        print(f'a has {len(a[0])} columns and b has {len(b[0])} columns. incorrect')
        return None

    c = []

    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        c.append(row)
    return c


def matrix_subtraction(a, b):
    for i in range(len(a)):  # checking if a is a matrix
        if len(a[i]) != len(a[0]):
            print('a is not a matrix')
            return None
    for i in range(len(b)):  # checking if b is a matrix
        if len(b[i]) != len(b[0]):
            print('b is not a matrix')
            return None
    if len(a) != len(b):  # checking if the amount of rows is equal
        print(f'a has {len(a)} rows and b has {len(b)} rows. incorrect')
        return None
    if len(a[0]) != len(b[0]):  # checking if the amount of columns is equal
        print(f'a has {len(a[0])} columns and b has {len(b[0])} columns. incorrect')
        return None

    c = []

    for i in range(len(a)):
        c1 = []
        for j in range(len(a[0])):
            c1.append(a[i][j] - b[i][j])
        c.append(c1)
    return c


def matrix_multiplication(a, b):
    for i in range(len(a)):  # checking if a is a matrix
        if len(a[i]) != len(a[0]):
            print('a is not a matrix')
            return None
    for i in range(len(b)):  # checking if b is a matrix
        if len(b[i]) != len(b[0]):
            print('b is not a matrix')
            return None
    if len(a[0]) != len(b):  # checking if the amount of columns of a is equal to the amount of rows of b
        print(f'a has {len(a[0])} columns and b has {len(b)} rows. incorrect')
        return None

    c = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            ab = 0
            for k in range(len(a[0])):
                ab += a[i][k] * b[k][j]
            row.append(ab)
        c.append(row)
    return c


def matrix_transpose(a):
    for i in range(len(a)):  # checking if a is a matrix
        if len(a[i]) != len(a[0]):
            print('a not a matrix')
            return None
    c = []
    for i in range(len(a[0])):
        row = []
        for j in range(len(a)):
            row.append(a[j][i])
        c.append(row)

    return c


def scalar_multiplication(a, scalar):
    for i in range(len(a)):  # checking if a is a matrix
        if len(a[i]) != len(a[0]):
            print('a not a matrix')
            return None
    c = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] * scalar)
        c.append(row)

    return c


def inverse_matrix(a): #for 2 by 2 matrix
    det = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    c = [[a[1][1], -a[0][1]],[-a[1][0], a[0][0]]]
    c = scalar_multiplication(c, 1/det)
    return c

# PART Y ================

def image_to_matrix(img):
    width, height = img.size
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(img.getpixel((x, y)))
        matrix.append(row)

    return matrix


def matrix_to_image(matrix, mode):
    height = len(matrix)
    width = len(matrix[0])
    if mode=="jpg":             #done to avoid saving RGBA images as jpgs and vice versa
        img = Image.new("RGB", (width, height))
    elif mode == "png":
        img = Image.new("RGBA", (width, height))
    for y in range(height):
        for x in range(width):
            img.putpixel((x, y), matrix[y][x])
    return img


def bilinear_interpolation(x, y, matrix):
    x0 = math.floor(x)
    if x >= (len(matrix[0]) - 1): #to make sure there are no 'list index out of range' errors
        x1 = x0
        dx = 0.5
    else:
        x1 = x0 + 1
        dx = x - x0 # distance between left pixel x0 and x
    y0 = math.floor(y)
    if y >= (len(matrix) - 1):
        y1 = y0
        dy = 0.5
    else:
        y1 = y0 + 1
        dy = y - y0

    colors1 = []
    index = len(matrix[0][0])
    for i in range(index):
        X1 = matrix[y0][x0][i] * (1 - dx) + matrix[y0][x1][i] * dx # 1st linear interpolation in x direction
        X2 = matrix[y1][x0][i] * (1 - dx) + matrix[y1][x1][i] * dx # 2nd linear interpolation in x direction
        Y = X1 * (1 - dy) + X2 * dy # linear interpolation in y direction
        colors1.append(round(Y))
    return tuple(colors1)


def rotate_matrix(matrix, angle_degrees, interpolation):
    height = len(matrix)
    width = len(matrix[0])
    angle = math.pi * angle_degrees / 180  # turn degrees into radians
    transformation_matrix = [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]
    inverse_transformation_matrix = inverse_matrix(transformation_matrix)

    # height is negative to switch to cartesian coords (y-up) instead of image coords (y-down)
    corners = [[0, 0], [width, 0], [width, -height], [0, -height]]

    transformed_corners = [
        (matrix_transpose(matrix_multiplication(transformation_matrix, [[x], [y]]))[0])
        for (x, y) in corners]
    xs = [a[0] for a in transformed_corners]
    ys = [a[1] for a in transformed_corners]

    offset = [[-min(xs)], [max(ys)]]
    width2 = int(offset[0][0] + max(xs))
    height2 = int(offset[1][0] - min(ys))

    offset_rotated = matrix_multiplication(transformation_matrix, offset)

    rotated_matrix = []

    for y in range(height2):
        row = []
        for x in range(width2):
            # map new (x, y) to original image coordinates
            transformed = matrix_multiplication(inverse_transformation_matrix, [[x], [-y]])
            orig_x = transformed[0][0] - offset_rotated[0][0]
            orig_y = transformed[1][0] + offset_rotated[1][0]
            if 0 <= orig_x < width and 0 <= -orig_y < height:
                if interpolation == "nearest neighbor":
                    row.append(matrix[int(-orig_y)][int(orig_x)]) # switching back to image coords
                elif interpolation == "bilinear":
                    row.append(bilinear_interpolation(orig_x, -orig_y, matrix))
            else:
                # if original coords are out of bound of original image, set pixel to transparent
                row.append((255, 255, 255, 0))
        rotated_matrix.append(row)

    return rotated_matrix


def skew_matrix(matrix, x_skew, y_skew, interpolation):
    height = len(matrix)
    width = len(matrix[0])
    transformation_matrix = [[1, x_skew], [y_skew, 1]]
    inverse_transformation_matrix = inverse_matrix(transformation_matrix)

    corners = [[0, 0], [width, 0], [width, height], [0, height]]
    transformed_corners = [
        (matrix_transpose(matrix_multiplication(transformation_matrix, [[x], [y]]))[0])
        for (x, y) in corners]
    xs = [a[0] for a in transformed_corners]
    ys = [a[1] for a in transformed_corners]

    height2 = int(max(ys) - min(ys))
    width2 = int(max(xs) - min(xs))

    offset_x = int(min(xs))
    offset_y = int(min(ys))

    skewed_matrix = []

    for y in range(height2):  # doing inverse-lookup so there are no holes
        row = []
        for x in range(width2):
            # map new (x, y) to original image coordinates
            transformed = matrix_multiplication(inverse_transformation_matrix, [[x + offset_x], [y + offset_y]])
            x_skewed = transformed[0][0]
            y_skewed = transformed[1][0]

            if 0 <= x_skewed < width and 0 <= y_skewed < height:
                if interpolation == "nearest neighbor":
                    row.append(matrix[int(y_skewed)][int(x_skewed)])
                elif interpolation == "bilinear":
                    row.append(bilinear_interpolation(x_skewed, y_skewed, matrix))
            else:
                # if original coords are out of bound of original image, set pixel to transparent
                row.append((255, 255, 255, 0))
        skewed_matrix.append(row)

    return skewed_matrix

def scale_matrix(matrix, x_scale, y_scale, input_type, interpolation):
    height = len(matrix)
    width = len(matrix[0])

    if input_type == "set coefficients":
        height2 = math.ceil(abs(height * y_scale))
        width2 = math.ceil(abs(width * x_scale))
    elif input_type == "set dimensions":
        height2 = int(abs(y_scale))
        width2 = int(abs(x_scale))
        x_scale = width2/width
        y_scale = height2/height

    transformation_matrix = [[x_scale, 0], [0, y_scale]]
    inverse_transformation_matrix = inverse_matrix(transformation_matrix)

    scaled_matrix = []

    for y in range(height2):
        row = []
        for x in range(width2):
            # map new (x, y) to original image coordinates
            transformed = matrix_multiplication(inverse_transformation_matrix, [[x], [y]])
            if x_scale > 0:
                orig_x = transformed[0][0]
            else:
                orig_x = width2 + transformed[0][0] - 1
            if y_scale > 0:
                orig_y = transformed[1][0]
            else:
                orig_y = height + transformed[1][0] - 1

            if interpolation == "nearest neighbor":
                row.append(matrix[int(orig_y)][int(orig_x)])
            elif interpolation == "bilinear":
                row.append(bilinear_interpolation(orig_x, orig_y, matrix))

        scaled_matrix.append(row)

    return scaled_matrix

def color_matrix(matrix, value_r, value_g, value_b): #value is from -1 to +1 in percents
    height = len(matrix)
    width = len(matrix[0])

    colored_matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            # change the color of every pixel
            r, g, b = matrix[y][x][:3]
            if value_r >= 0:
                new_r = r + round((255 - r) * value_r)
            else:
                new_r = r + round(r * value_r)
            if value_g >= 0:
                new_g = g + round((255 - g) * value_g)
            else:
                new_g = g + round(g * value_g)
            if value_b >= 0:
                new_b = b + round((255 - b) * value_b)
            else:
                new_b = b + round(b * value_b)

            if len(matrix[y][x]) == 3: #if image is RGB
                row.append(tuple([new_r, new_g, new_b]))
            else: #if image is RGBA
                row.append(tuple([new_r, new_g, new_b, matrix[y][x][3]]))

        colored_matrix.append(row)

    return colored_matrix
