# EasyOCR - Text Extraction from Android App Screenshots

This project is a Python script that utilizes the EasyOCR library to extract text from Android app screenshots. It includes functions to process images, extract text, and display the results in a DataFrame.

## Usage

1. Ensure you have [EasyOCR](https://github.com/JaidedAI/EasyOCR) installed. If not, you can install it using pip:
   ```
   pip install easyocr
   ```

2. Run the script by executing the following command:
   ```
   python easyOCR-android.py
   ```
   
   Note: This implementation assumes you have a CUDA-enabled GPU. Set flag to `gpu=false` to run in CPU-only mode.
      ```
      reader = easyocr.Reader(['en'], gpu=False)
      ```

3. The script will process the images located in the './content' directory and display the extracted text along with the processing time for each image. The results will be saved in the ./results directory in text format, including the extracted text and processing time.

## Dependencies
- pytorch
- easyocr
- pandas

## Image Processing
- Processes `.png` images located in the `./content` directory.
- Utilizes EasyOCR to detect and extract text from these images.

## Data Handling
- Converts extracted text and its bounding box coordinates into a pandas DataFrame.
- Enhances the DataFrame by separating coordinates for the top-left and bottom-right corners of each bounding box.

## Performance Tracking
- Records the time taken for each image's OCR process, from start to finish.
- Monitors processing efficiency through recorded durations.

## Output
- Generates a text file report for each processed image in the `./results` directory.
- Each report contains the DataFrame (as a string) and the processing time.

## Author
Divya Rustagi (Supported by ChatGPT 🙂)
