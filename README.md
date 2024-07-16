# Automated Image Quote Generator In Python
A hobby project that reads random quotes from free quote API and generates quote images based on the provided image

# Requirements
Install the required libraries using
<pre>pip install Pillow requests</pre>

# How it works
It reads an image from the "images" folder that is passed in the code. It calls a random quote API and generates a quote with the author's name. Then it generates the final image by adding some overlay to make the text look easier to read by darkening the original image. The font file, font size, text opacity, and overlay amount can be adjusted in the code. 

# Potential Use Cases and Expansion Ideas
This code can be used as a base to
* Develop a web app powered by Django/Flask that allows visitors to upload their image and custom quote list and bulk generate multiple quote images on the fly.
* Create bulk quote image generator software
* Make it more random by allowing it to read more images randomly and more random quotes to increase the number of randomly generated quote

# Original Image Sample
<img src="https://raw.githubusercontent.com/TufayelLUS/Automated-Image-Quote-Generator-In-Python/main/images/wallpaper.jpg" />

# Image After Generating Quote with the Script
<img src="https://raw.githubusercontent.com/TufayelLUS/Automated-Image-Quote-Generator-In-Python/main/output.png" />

# Loved this?
Star this project and share it with your friends!
