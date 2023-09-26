
# Virtual Drag and Drop

This project demonstrates the capabilities of computer vision and hand tracking. It allows you to control and interact with draggable rectangles using your hand's movements, creating a fun and interactive experience on your webcam.

![Demo](https://github.com/aribzaman/VirtualDragAndDrop/blob/main/demo.gif)

## Features

- Live webcam feed
- Hand tracking for gesture recognition
- Draggable rectangles
- Interactive canvas

## Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)
- [cvzone](https://github.com/cvzone/cvzone) library (for Hand Tracking)

## How to Use

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/aribzaman/VirtualDragAndDrop.git

2. Install the required Python packages:

   ```shell
   pip install -r requirements.txt

3. Run the script:

   ```shell
   python main.py

4. Use your webcam and hands to control and interact with the draggable rectangles.

To hold a rectangle, you need to join your index finger and the middle finger - keeping the fingers in the same position, you can move the rectangles and liekwise to drop it, you separate your fingers.

5. To quit Press the 'Q' key on your keyboard.

## Customization

- You can customize the number and properties of the draggable rectangles by modifying the rectList in the main.py script.
- Comment the Solid Rectangle box Section and Uncomment the Transparent Rectangle section to decrease the Opacity of the rectangles making it transparent

## Add-Ons
- Two additional files are present to demonstrate how the application works under the hood.
   1. **HandDetector** *(To demonstarte how the entire hand is mapped)*
   2. **FingerTipTutorial** *(To display how a hand landmark is detected by changing the rectangle color when you bring your fingertip within it)*

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgment

Hand tracking functionality is powered by the [cvzone](https://github.com/cvzone/cvzone) library.
Feel free to contribute, enhance, or adapt this project for your creative needs. Have fun experimenting with computer vision and interactive art!

## Contact Information:
For any further queries, feel free to contact me at:

Email: catcharibzaman@gmail.com 

LinkedIn : [Arib Zaman](https://www.linkedin.com/in/aribzaman/)