# EasyOCR for Extracting Text from Android Mobile Screenshots
import easyocr
import pandas as pd
import time  # Import the time module

def process_image(image_path, reader):
    start_time = time.time()  # Start time before processing the image
    """
    Process an image to extract text, convert results to a DataFrame, and print.
    """
    result = reader.readtext(image_path)
    df = pd.DataFrame(result, columns=['Bounding Box', 'Text', 'Confidence'])
    # Assuming 'Bounding Box' is structured as [top-left, top-right, bottom-right, bottom-left]
    df['Bounding Box Top Left'] = df['Bounding Box'].apply(lambda x: x[0])
    df['Bounding Box Bottom Right'] = df['Bounding Box'].apply(lambda x: x[2])
    #df.drop('Bounding Box', axis=1, inplace=True)
    end_time = time.time()  # End time after processing the image
    processing_time = end_time - start_time  # Calculate processing time
    return df, processing_time  # Return the DataFrame and the processing time

def main():
    reader = easyocr.Reader(['en'])  # Load the model into memory
    image_paths = ['./content/android-sample-app.png', './content/clothes-list.png']
    
    for i, image_path in enumerate(image_paths, start=1):
        df, processing_time = process_image(image_path, reader)  # Unpack the returned values
        print(f"Result {i}")
        print(df)
        print(f"Processing time for image {i}: {processing_time:.3f} seconds")  # Print processing time

if __name__ == "__main__":
    main()
