# muisc_sheet_to_MIDIFile

Problem description
- Try to read the music notes from muisc sheets and converts it to MIDI (digital interface)

Previous work (including what you used for your method i.e. pretrained models)
- https://sourceforge.net/projects/openomr/
- https://docs.opencv.org/3.4/dd/dd7/tutorial_morph_lines_detection.html
- there are many ways to match the notes by using Machine Learning or using traditional CV ways(template matching and hough detection, etc.)


Your approach
- My approch is to use "fature mathcing" and "template matching" algorihtm to match the note and pitch and transfer it to MIDI format  
- Therefore, my aprocah is to clean the image first and tranfer it to grayscale and canny 
- I extracted the notes and clef from the staff 
- Try to find clef by template matching
- And find quarter, half, and whole notes by template matching
- Clean up the data and sort the notes by its positions 
- Use the positions of clef and notes to find the pitch 
- Use the pitches and notes, we can transfer those dat into MIDI 

Datasets
- https://sourceforge.net/projects/openomr/files/latest/download


Results

Here is the Jupyter Notebook including the main code and result 

Demo:
 [![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/X2hmlZn_jmc/0.jpg)](https://youtu.be/X2hmlZn_jmc)



Discussion

What problems did you encounter?
- I spend many times to understand how to read music sheet lmao 
- Although the algorithm is not really difficult, I need to learn many different part to bring the whole piece togehter 
- Learning how to transfter code to MIDI format to save music 
Are there next steps you would take if you kept working on the project?
- Yea... I spend too much time on caculating the picths and learning OpenCV. Therefore, I didn't have time to try ML for finding the pitches 
  Maybe using ML, I can get a more accurate result. 
- Also, there are many things that I can do in the future. Ex. Do multiple staffs... Find the rest symbol...  
How does your approach differ from others? Was that beneficial?
- Many people solved the problem by ML. However, I think the music sheets are simple to read. Therefore, we should jusst use feature matching 
and we can lower down the caculation time. I think I get a good result from feature matching to find the notes and its positions. Also, I try to 
use the relative positions of clef and notes to find the pitch. It is quit different them other people do( they like to use staffs). I think my algo 
is more simple and faster.  
