import matplotlib.pyplot as plt

import image_ocr

# image-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = image_ocr.pipeline.Pipeline()

# Get a set of three example images
# images = [
#     image_ocr.tools.read(url) for url in [
#         'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Kali_Linux_2.0_wordmark.svg/langfr-420px-Kali_Linux_2.0_wordmark.svg.png',
#         'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Enseigne_de_pharmacie_lumineuse.jpg/180px-Enseigne_de_pharmacie_lumineuse.jpg',
#         'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Boutique_Christian_Lacroix.jpg/330px-Boutique_Christian_Lacroix.jpg',
#     ]
# ]
img= ['X:/Infosys_STMS/Smart_Traffic_Management_System/Output/Testing/noplate1.jpg']

# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
# prediction_groups = pipeline.recognize(images)

# Plot the predictions
# fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
# for ax, image, predictions in zip(axs, images, prediction_groups):
#     # image_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
#     print(predictions)

pred = pipeline.recognize(img)
for predictions in pred:
    print(predictions)