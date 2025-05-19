1.Create a virtual environment:
python3 -m venv venv

Activate the virtual environment:
.\venv\Scripts\activate

2.Install Dependencies
Inside the virtual environment, install the required libraries:
pip install numpy matplotlib scipy

Freeze the dependencies to a requirements.txt:
pip freeze > requirements.txt

3.Project Structure
Folder name : MOBIUS_PROJECT
INSIDE THE FOLDER 
├── venv
├── mobius_strip.py
├── requirements.txt

4.Then simply run : mobius_strip.py

5. You will obtain 
Approximated Surface Area: 1.88673
Approximated Edge Length: 12.60154 with 3D Plot at a time

