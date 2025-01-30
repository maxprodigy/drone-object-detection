# -*- coding: utf-8 -*-

def visualize_annotations(image_path, annotation_path, save_path=None):
    """
    Visualizes bounding boxes on images and optionally saves the result.

    Args:
        image_path (str): Path to the image file.
        annotation_path (str): Path to the COCO-format JSON annotation file.
        save_path (str, optional): Path to save the visualized image. If None, the image is not saved.
    """
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for matplotlib

    # Load the annotations
    with open(annotation_path, 'r') as f:
        annotations = json.load(f)

    # Draw bounding boxes on the image
    for ann in annotations['annotations']:
        bbox = ann['bbox']  # COCO format: [x_min, y_min, width, height]
        x, y, w, h = map(int, bbox)
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle

    # Display the image with bounding boxes
    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    plt.axis('off')
    plt.show()

    # Save the image if save_path is provided
    if save_path:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert back to BGR for saving
        cv2.imwrite(save_path, image)

    # Define save path
    save_path = '/content/drive/MyDrive/drone-object-detection/visualized_images/sample_visualized.jpg'

  # Visualize and save the image
    visualize_annotations(image_path, annotation_path, save_path)
