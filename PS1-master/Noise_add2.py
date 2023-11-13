# extract green and blue channels
    temp_image = image.astype('float64')
    green_channel = temp_image[:,:,1]
    blue_channel = temp_image[:,:,0]
    #temp_image = np.copy(image)
    #temp_image = image.copy()
    #temp_image = image.astype('float64')

    #Generate random Gaussian noise
    mean = 0
    
    if channel == 1:
        noise_g = np.zeros(green_channel.shape, np.float64)
        cv2.randn(noise_g, mean, sigma)
        noisy_green = cv2.add(green_channel, noise_g)
        #noisy_green = cv2.addWeighted(green_channel, 1, noise_g, 1, 0.0)
        #noisy_green = green_channel + noise_g
        temp_image [:, :, 1] = noisy_green

    if channel == 0:
        noise_b = np.zeros(blue_channel.shape, np.float64)
        cv2.randn(noise_b, mean, sigma)
        noisy_blue = cv2.add(blue_channel, noise_b)
        #noisy_blue = cv2.addWeighted(blue_channel, 1, noise_b, 1, 0.0)
        #noisy_blue = blue_channel + noise_b
        temp_image [:, :, 0] = noisy_blue

    return temp_image