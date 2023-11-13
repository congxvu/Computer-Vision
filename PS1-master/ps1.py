import math
import numpy as np
import cv2

# # Implement the functions below.


def extract_red(image):
    """ Returns the red channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the red channel.
    """
    # extract red channel from image
    red_channel = image[:,:,2]

    # coppy to a temp_image as 2D array
    temp_image = np.copy(red_channel)
    
    # return to 2D array
    # return temp_image
    return red_channel

    raise NotImplementedError


def extract_green(image):
    """ Returns the green channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the green channel.
    """
    
    # extract green channel from image
    green_channel = image[:,:,1]

    # coppy to a temp_image as 2D array
    temp_image = np.copy(green_channel)
    
    # return to 2D array
    return temp_image

    raise NotImplementedError


def extract_blue(image):
    """ Returns the blue channel of the input image. It is highly recommended to make a copy of the
    input image in order to avoid modifying the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 2D array containing the blue channel.
    """
    
    # extract blue channel from image
    blue_channel = image[:,:,0]

    # coppy to a temp_image as 2D array
    temp_image = np.copy(blue_channel)
    
    # return to 2D array
    return temp_image

    raise NotImplementedError


def swap_green_blue(image):
    """ Returns an image with the green and blue channels of the input image swapped. It is highly
    recommended to make a copy of the input image in order to avoid modifying the original array.
    You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input RGB (BGR in OpenCV) image.

    Returns:
        numpy.array: Output 3D array with the green and blue channels swapped.
    """
    # extract blue channel from image
    blue_channel = image[:,:,0]

    # extract green channel from image
    green_channel = image[:,:,1]

    # extract red channel from image
    red_channel = image[:,:,2]

    # create empty image with same shape of original image
    empty_img = np.zeros(image.shape)

    # copy thoses channel back to empty image with swapt B&G
    empty_img[:,:,0] = green_channel
    empty_img[:,:,1] = blue_channel
    empty_img[:,:,2] = red_channel

    return empty_img

    raise NotImplementedError


def copy_paste_middle(src, dst, shape):
    """ Copies the middle region of size shape from src to the middle of dst. It is
    highly recommended to make a copy of the input image in order to avoid modifying the
    original array. You can do this by calling:
    temp_image = np.copy(image)

        Note: Assumes that src and dst are monochrome images, i.e. 2d arrays.

        Note: Where 'middle' is ambiguous because of any difference in the oddness
        or evenness of the size of the copied region and the image size, the function
        rounds downwards.  E.g. in copying a shape = (1,1) from a src image of size (2,2)
        into an dst image of size (3,3), the function copies the range [0:1,0:1] of
        the src into the range [1:2,1:2] of the dst.

    Args:
        src (numpy.array): 2D array where the rectangular shape will be copied from.
        dst (numpy.array): 2D array where the rectangular shape will be copied to.
        shape (tuple): Tuple containing the height (int) and width (int) of the section to be
                       copied.

    Returns:
        numpy.array: Output monochrome image (2D array)
    """
    
    # Height and width of copied area
    h_rect = shape[0]
    w_rect = shape[1]
    
    # Location of coppied image
    y_src = src.shape[0]  # height of src image
    x_src = src.shape[1]  # width

    cs1 = int(x_src/2 - w_rect/2)
    cs2 = int(x_src/2 + w_rect/2)
    rs1 = int(y_src/2 - h_rect/2)
    rs2 = int(y_src/2 + h_rect/2)

    # area is coppied
    img2 = src[rs1 : rs2 , cs1 : cs2]


    # Location of pasted image
    y_dst = dst.shape[0]    # height of dst image
    x_dst = dst.shape[1]    # width

    cd1 = int(x_dst/2 - w_rect/2)
    cd2 = int(x_dst/2 + w_rect/2)
    rd1 = int(y_dst/2 - h_rect/2)
    rd2 = int(y_dst/2 + h_rect/2)
    
    # copy image in mask area
    temp_image = np.copy(dst)
    temp_image[rd1 : rd2 , cd1 : cd2] = img2
    
    return temp_image


    raise NotImplementedError



def copy_paste_middle_circle(src, dst, radius):
    """ Copies the middle circle region of radius "radius" from src to the middle of dst. It is
    highly recommended to make a copy of the input image in order to avoid modifying the
    original array. You can do this by calling:
    temp_image = np.copy(image)

        Note: Assumes that src and dst are monochrome images, i.e. 2d arrays.

    Args:
        src (numpy.array): 2D array where the circular shape will be copied from.
        dst (numpy.array): 2D array where the circular shape will be copied to.
        radius (scalar): scalar value of the radius.

    Returns:
        numpy.array: Output monochrome image (2D array)
    """
    # Height and width of source images
    src_height = src.shape[0]
    src_width = src.shape[1]

    # Center of src image
    #y_src = math.floor(src.shape[0]/2) # height of src image
    #x_src = math.floor(src.shape[1]/2) # width
    y_src = src.shape[0]//2 # height of src image
    x_src = src.shape[1]//2 # width

    # Center of dst image
    #y_dst = math.floor(dst.shape[0]/2) # height of dst image
    #x_dst = math.floor(dst.shape[1]/2) # width
    y_dst = dst.shape[0]//2 # height of dst image
    x_dst = dst.shape[1]//2 # width

    # test diameter
    test_diameter = radius*2 + 1

    # Make a copy dst to temp_image
    temp_image = dst.copy()

    # Find all pixels within the radius at src image and then copy to dst image
    for x in range(src_width):
        for y in range(src_height):
            # find distance from the center
            distance = math.sqrt((x - x_src)**2 + (y - y_src)**2)
            # copy pixel from src to dst if (x,y) within the circle
            if (distance <= radius) :
                dx = int(x_dst + (x - x_src))
                dy = int(y_dst + (y - y_src))
                temp_image[dy, dx] = src[y, x]


    return temp_image

    raise NotImplementedError


def image_stats(image):
    """ Returns the tuple (min,max,mean,stddev) of statistics for the input monochrome image.
    In order to become more familiar with Numpy, you should look for pre-defined functions
    that do these operations i.e. numpy.min.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.

    Returns:
        tuple: Four-element tuple containing:
               min (float): Input array minimum value.
               max (float): Input array maximum value.
               mean (float): Input array mean / average value.
               stddev (float): Input array standard deviation.
    """
    # compute min, max, mean, and std of image
    min_value = float(np.min(image))
    max_value = float(np.max(image))
    mean_value = float(np.mean(image))
    std_value = image.std()

    return min_value, max_value, mean_value, std_value

    raise NotImplementedError


def center_and_normalize(image, scale):
    """ Returns an image with the same mean as the original but with values scaled about the
    mean so as to have a standard deviation of "scale".

    Note: This function makes no defense against the creation
    of out-of-range pixel values.  Consider converting the input image to
    a float64 type before passing in an image.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.
        scale (int or float): scale factor.

    Returns:
        numpy.array: Output 2D image.
    """
    
    # convert image type to float64
    temp_image = image.astype('float64')

    # find values of image
    image_min, image_max, image_mean, image_stddev = image_stats(image)

    # normalize center
    temp_image = (((image - image_mean) / image_stddev) * scale) + image_mean
    
    return temp_image    

    raise NotImplementedError


def shift_image_left(image, shift):
    """ Outputs the input monochrome image shifted shift pixels to the left.

    The returned image has the same shape as the original with
    the BORDER_REPLICATE rule to fill-in missing values.  See

    http://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/copyMakeBorder/copyMakeBorder.html?highlight=copy

    for further explanation.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): Input 2D image.
        shift (int): Displacement value representing the number of pixels to shift the input image.
            This parameter may be 0 representing zero displacement.

    Returns:
        numpy.array: Output shifted 2D image.
    """
    temp_image =cv2.copyMakeBorder(image[:, shift:], 0, 0, 0, shift, cv2.BORDER_REPLICATE)

    return temp_image

    raise NotImplementedError


def difference_image(img1, img2):
    """ Returns the difference between the two input images (img1 - img2). The resulting array must be normalized
    and scaled to fit [0, 255].

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        img1 (numpy.array): Input 2D image.
        img2 (numpy.array): Input 2D image.

    Returns:
        numpy.array: Output 2D image containing the result of subtracting img2 from img1.
    """
    # convert image type to float64
    #temp_image = image.astype('float64')

    # copy 2 images and convert to float64
    temp_img1 = img1.astype('float64')
    temp_img2 = img2.astype('float64')
    
    # subtract 2 images
    temp_diff = temp_img1 - temp_img2
    
    # read images value
    min_value, max_value, mean_value, std_value = image_stats(temp_diff)
    
    # find distance
    distance = max_value - min_value
    distance = distance or float(distance)
    
    temp_image = (temp_diff - min_value) * np.divide(255, distance)
    
    # convert image NaN to 0
    temp_image[np.isnan(temp_image)] = 0
    
    return temp_image

    raise NotImplementedError


def add_noise(image, channel, sigma):
    """ Returns a copy of the input color image with Gaussian noise added to
    channel (0-2). The Gaussian noise mean must be zero. The parameter sigma
    controls the standard deviation of the noise.

    The returned array values must not be clipped or normalized and scaled. This means that
    there could be values that are not in [0, 255].

    Note: This function makes no defense against the creation
    of out-of-range pixel values.  Consider converting the input image to
    a float64 type before passing in an image.

    It is highly recommended to make a copy of the input image in order to avoid modifying
    the original array. You can do this by calling:
    temp_image = np.copy(image)

    Args:
        image (numpy.array): input RGB (BGR in OpenCV) image.
        channel (int): Channel index value.
        sigma (float): Gaussian noise standard deviation.

    Returns:
        numpy.array: Output 3D array containing the result of adding Gaussian noise to the
            specified channel.
    """
    # coppy image with float 64
    temp_image = image.astype('float64')
    
    # generate random Gaussian noise
    G_noise = np.random.randn(*image.shape) * sigma
    
    # add noise to specific channel
    temp_image[:, :, channel] += G_noise[:, :, channel]
    
    return temp_image

    raise NotImplementedError


def build_hybrid_image(image1, image2, cutoff_frequency):
    """ 
    Takes two images and creates a hybrid image given a cutoff frequency.
    Args:
        image1: numpy nd-array of dim (m, n, c)
        image2: numpy nd-array of dim (m, n, c)
        cutoff_frequency: scalar
    
    Returns:
        hybrid_image: numpy nd-array of dim (m, n, c)

    Credits:
        Assignment developed based on a similar project by James Hays. 
    """

    filter = cv2.getGaussianKernel(ksize=cutoff_frequency*4+1, sigma=cutoff_frequency)
    filter = np.dot(filter, filter.T)
    
    low_frequencies = cv2.filter2D(image1,-1,filter)

    high_frequencies = image2 - cv2.filter2D(image2,-1,filter)
    
    raise NotImplementedError


def vis_hybrid_image(hybrid_image):
    """ 
    Tools to visualize the hybrid image at different scale.

    Credits:
        Assignment developed based on a similar project by James Hays. 
    """


    scales = 5
    scale_factor = 0.5
    padding = 5
    original_height = hybrid_image.shape[0]
    num_colors = 1 if hybrid_image.ndim == 2 else 3

    output = np.copy(hybrid_image)
    cur_image = np.copy(hybrid_image)
    for scale in range(2, scales+1):
      # add padding
      output = np.hstack((output, np.ones((original_height, padding, num_colors),
                                          dtype=np.float32)))

      # downsample image
      cur_image = cv2.resize(cur_image, (0, 0), fx=scale_factor, fy=scale_factor)

      # pad the top to append to the output
      pad = np.ones((original_height-cur_image.shape[0], cur_image.shape[1],
                     num_colors), dtype=np.float32)
      tmp = np.vstack((pad, cur_image))
      output = np.hstack((output, tmp))

    return output
