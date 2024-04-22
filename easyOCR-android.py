# EasyOCR for Extracting Text from Android Mobile Screenshots
import easyocr
import pandas as pd
import time  # Import the time module
import os  # Add this import at the top of your file

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
    image_paths = [os.path.join('./content', f) for f in os.listdir('./content') if f.endswith('.png')]  # Read all image files in the ./content folder

    result_dir = './results'
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)

    for i, image_path in enumerate(image_paths, start=1):
        df, processing_time = process_image(image_path, reader)  # Unpack the returned values
        image_name = os.path.basename(image_path)  # Get the image file name
        print(f"Result {i} - {image_name}")
        print(df)
        print(f"Processing time for image {i}: {processing_time:.3f} seconds")  # Print processing time
        
        # Set display options to show all rows and columns
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        
        # Write the DataFrame, image name, and processing time to a text file
        output_file = os.path.join(result_dir, f"result_{i}.txt")
        with open(output_file, 'w') as file:
            file.write(f"Result {i} - {image_name}\n\n")
            file.write(df.to_string() + '\n\n')
            file.write(f"Processing time for image {i}: {processing_time:.3f} seconds")

        print(f"Report for image {i} ({image_name}) saved to {output_file}")

if __name__ == "__main__":
    main()
