![Air_BnB_Console_Project](https://github.com/Ace-Quantum/atlas-AirBnB_clone/assets/144152489/0b9474e9-f3c9-4410-bec2-ed01f7ea60ba)

<p align="center">
✨Presented by <a href="https://github.com/Ace-Quantum" target="_blank">Ace</a> and  <a href="https://github.com/Srixx24/">Jackie</a> ✨
</p>

<br>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Static Badge](https://img.shields.io/badge/Queers%20Ruling-Code%20Space-purple?style=string&logoColor=purple) 

<h3><p align="center">
Directory of our <a href="https://github.com/Ace-Quantum/atlas-AirBnB_clone">Air BnB Console Project Project</a>
</p></h3>



<br>

This Air BnB Console works through a command line interpreter through the console file. It works by pulling data from the file storage system and other support system files to  allows the user to save and store relevant data. Below is a brief description of each file and its function to provide a working console.

<br>

### 🌟 [Console](https://github.com/Ace-Quantum/atlas-AirBnB_clone/blob/main/console.py)
- The console contains the entry point of the command interpreter.
-  The commad line uses the custom prompt of "(hbnb) " and uses the import module cmd
<details>
<summary>The console utilizes the following methods</summary>
<ul><li>Create: This command creates a new instance of the specified class.</li>
<li>Show: The show command prints the string representation of an instance.</li>
<li>Destroy: The destroy command deletes an instance based on the class name and ID provided.</li>
<li>All: The all command prints the string representation of all instances.</li>
<li>Update: The update command updates an instance. **IMPORTANT** The following can not be updated as the are restricted - id, created_at, and updated_at</li>
</ul></details>

<br>

### 🌟 [Models](https://github.com/Ace-Quantum/atlas-AirBnB_clone/tree/main/models)
- The model file contains many functions that support the console's functionality.
- Some of these are support classes such as the user, city, place, state, amenity, and review classes.
- Others such as the Base Model are the starting point for all other classes to function from.
<details>
<summary>Function Details</summary>
<ul><li>The User Class provides information like email, password, first and last name</li>
<li>The City class provides information like state id and name.</li>
<li>The Place class provides information like city id, user id, name, description, number of rooms, number of bathrooms, max guests, price per night, latitude, longitude, and amenity ids.</li>
<li>The State class provides information like name.</li>
<li>The Amenity class provides information like name.</li>
<li>The Review class provides information like place id, user id, and text.</li></ul></details>

<br>

### 🌟 [Engine](https://github.com/Ace-Quantum/atlas-AirBnB_clone/tree/main/models/engine)
- The Engine file contains the storage files that help store and save data for the console system. This system is a file storage engine that provides methods for JSON serialization and deserialization
-  The main file storage system in this file is the file storage class, which serves as the main engine for storing and retrieving data. It works by using several methods to save, return, override, and load data from the console classes
<details>
<summary>Function Details</summary>
<ul><li>The file path class attribute is set to the path of the JSON file used for data storage.</li
<li>The objects dictionary is used to hold instances of various classes.</li>
<li>The all method returns the objects dictionary.</li>
<li>The new method adds a new object to the objects dictionary.</li>
<li>The save method serializes the objects in the objects dictionary and saves them to the JSON file specified by file path.</li>
<li>The reload method loads the instances from the JSON file and populates the objects dictionary.</li></ul></details>

<br>

### 🌟 [Tests](https://github.com/Ace-Quantum/atlas-AirBnB_clone/tree/main/tests)
- If we got tests they're [here](https://github.com/Ace-Quantum/atlas-AirBnB_clone/tree/main/tests) and they're unittests!

  
<br>
<br>
<br>

![carbon (1)](https://github.com/Ace-Quantum/atlas-AirBnB_clone/assets/144152489/97979d52-43e1-4870-b1bd-587473983153)


<br>

![Thank_you_for_visiting_our_repo! (1)](https://github.com/Ace-Quantum/atlas-AirBnB_clone/assets/144152489/350533bf-aeb3-408c-a7f0-726021f58b1d)

<p align="center">
  <img width="350" src="https://github.com/Ace-Quantum/atlas-AirBnB_clone/assets/144152489/a851c145-5431-4629-9493-d32e3d0232e8">
</p>


