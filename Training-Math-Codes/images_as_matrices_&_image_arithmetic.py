import matplotlib.pyplot as plt
import skimage.io


def get_image_from_url(url):
    image = skimage.io.imread(url)
    return image


def get_image_rgb_channels(image):
    image_red, image_green, image_blue = [image[:, :, i] for i in range(3)]
    return image_red, image_green, image_blue


def get_image_rgb_normalizations(image_red_ch, image_green_ch, image_blue_ch):
    image_red_ch_norm, image_green_ch_norm, image_blue_ch_norm = [
        channel / 255 for channel in [image_red_ch, image_green_ch, image_blue_ch]
    ]
    return image_red_ch_norm, image_green_ch_norm, image_blue_ch_norm


def get_image_average_grayscale(image_red_ch_norm, image_green_ch_norm, image_blue_ch_norm):
    image = (image_red_ch_norm+image_green_ch_norm+image_blue_ch_norm) / 3
    return image


def get_image_gamma_correction(image_red_ch_norm, image_green_ch_norm, image_blue_ch_norm, red_c, green_c, blue_c):
    image = red_c * image_red_ch_norm+green_c * image_green_ch_norm+blue_c * image_blue_ch_norm
    return image


def plot_original_image(image, axis_mode):
    plt.imshow(image)
    plt.axis(axis_mode)
    plt.title("Original image")
    plt.show()


def plot_image_rgb_channels(image_red, image_green, image_blue, image_red_color, image_green_color, image_blue_color):
    fig, (ax_red, ax_green, ax_blue) = plt.subplots(1, 3, figsize=(10, 10))
    ax_red.imshow(image_red, cmap=image_red_color)
    ax_red.set_title("Red channel")
    ax_green.imshow(image_green, cmap=image_green_color)
    ax_green.set_title("Green channel")
    ax_blue.imshow(image_blue, cmap=image_blue_color)
    ax_blue.set_title("Blue channel")
    plt.setp([ax_red, ax_green, ax_blue], xticks=[], yticks=[])
    plt.show()


def plot_average_grayscale_image(image, axis_mode, color):
    plt.imshow(image, cmap=color)
    plt.axis(axis_mode)
    plt.title("Average grayscale image")
    plt.show()


def plot_gamma_corrected_image(image, axis_mode, color):
    plt.imshow(image, cmap=color)
    plt.axis(axis_mode)
    plt.title("Gamma-corrected grayscale image")
    plt.show()


def plot_single_image_histogram(image, title, color):
    plt.hist(image.ravel(), bins=256, color=color)
    plt.title(title)
    plt.show()


def plot_images_histograms_comparison(*args):
    images = args[0]
    labels = args[1]
    colors = args[2]
    histograms = zip(images, labels, colors)
    for images, labels, colors in histograms:
        plt.hist(images.ravel(), bins=256, alpha=0.5, color=colors, label=labels)
    plt.xlim(0, 1)
    plt.title("Images histograms comparison")
    plt.legend()
    plt.show()


def plot_rgb_images_and_their_histograms(images, titles, hist_colors, images_colors):
    image_red, image_green, image_blue = images
    image_red_title, image_green_title, image_blue_title = titles
    hist_red_color, hist_green_color, hist_blue_color = hist_colors
    image_red_color, image_green_color, image_blue_color = images_colors
    fig, ((image_r, image_g, image_b), (red_hist, green_hist, blue_hist)) = plt.subplots(2, 3, figsize=(10, 10))
    image_r.imshow(image_red, cmap=image_red_color)
    image_r.set_title(image_red_title)
    red_hist.hist(image_red.ravel(), bins=256, color=hist_red_color)
    red_hist.set_title(image_red_title)
    image_g.imshow(image_green, cmap=image_green_color)
    image_g.set_title(image_green_title)
    green_hist.hist(image_green.ravel(), bins=256, color=hist_green_color)
    green_hist.set_title(image_green_title)
    image_b.imshow(image_blue, cmap=image_blue_color)
    image_b.set_title(image_blue_title)
    blue_hist.hist(image_blue.ravel(), bins=256, color=hist_blue_color)
    blue_hist.set_title(image_blue_title)
    plt.show()


image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVMwhaWZiz7O7sh396Sx-1fsSomLbyKhBGIw&usqp=CAU"

dog_image = get_image_from_url(image_url)
dog_red_ch, dog_green_ch, dog_blue_ch = get_image_rgb_channels(dog_image)
dog_red_ch_norm, dog_green_ch_norm, dog_blue_ch_norm = \
    get_image_rgb_normalizations(dog_red_ch, dog_green_ch, dog_blue_ch)
dog_average_grayscale = get_image_average_grayscale(dog_red_ch_norm, dog_green_ch_norm, dog_blue_ch_norm)
dog_gamma_corrected_grayscale = \
    get_image_gamma_correction(dog_red_ch_norm, dog_green_ch_norm, dog_blue_ch_norm, 0.299, 0.587, 0.114)

plot_original_image(dog_image, "on")
plot_image_rgb_channels(dog_red_ch, dog_green_ch, dog_blue_ch, "gray", "gray", "gray")
plot_average_grayscale_image(dog_average_grayscale, "on", "gray")
plot_gamma_corrected_image(dog_gamma_corrected_grayscale, "on", "gray")
plot_single_image_histogram(dog_average_grayscale, "Average grayscale image\nUncorrected image", "blue")
plot_single_image_histogram(dog_gamma_corrected_grayscale, "Gamma-corrected image", "orange")
plot_images_histograms_comparison(
    [dog_average_grayscale, dog_gamma_corrected_grayscale],
    ["Average grayscale image", "Gamma-corrected image"],
    ["blue", "orange"]
)
plot_rgb_images_and_their_histograms(
    [dog_red_ch_norm, dog_green_ch_norm, dog_blue_ch_norm],
    ["Red channel", "Green channel", "Blue channel"],
    ["red", "green", "blue"],
    ["Reds_r", "Greens_r", "Blues_r"]
)
plot_images_histograms_comparison(
    [dog_red_ch_norm, dog_green_ch_norm, dog_blue_ch_norm],
    ["Red channel", "Green channel", "Blue channel"],
    ["red", "green", "blue"]
)

