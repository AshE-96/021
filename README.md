# 021 - Tehran District Finder

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Find the Tehran Municipality District for given geographic coordinates directly in your terminal!**

This command-line tool, `021`, helps you quickly identify the Tehran municipality district for a given latitude and longitude.  It's designed to be simple, efficient, and easy to use right from your terminal.

## Features

*   **District Identification:** Determines the Tehran municipality district containing a given latitude and longitude.
*   **User-Friendly Terminal Interface:** Clean and organized terminal output for easy interaction.
*   **Loading Animation:**  A subtle loading animation during data initialization.
*   **Instructions Menu:** Option to display clear instructions on how to use the application.
*   **Simple Menu Navigation:**  Easy-to-use numbered menu for application options.
*   **Error Handling:**  Provides informative error messages for invalid inputs and data issues.
*   **Exit Option:**  Graceful exit from the application.

## Libraries Used

This project utilizes the following Python libraries:

*   **click:**  Used for building beautiful command-line interfaces in a composable way.  It simplifies the process of creating command-line tools with options, arguments, and help text.  In this project, `click` is essential for handling user input, displaying menus, and creating a user-friendly terminal experience.
    ([https://click.palletsprojects.com/](https://click.palletsprojects.com/))

*   **shapely:** A powerful Python package for manipulation and analysis of planar geometric objects. It's used for working with geometric shapes like points and polygons.  In this project, `shapely` is crucial for:
    *   Representing Tehran district boundaries as polygons.
    *   Determining if a given point (latitude and longitude) falls within a district polygon.
    ([https://shapely.readthedocs.io/en/stable/](https://shapely.readthedocs.io/en/stable/))


## Usage

1.  **Clone the repository (if you haven't already):**

    ```bash
    git clone https://github.com/AshE-96/021
    cd 021
    ```

2.  **Install the required Python libraries:**

    This project requires the `click` and `shapely` libraries. You can install them using pip:

    ```bash
    pip install click shapely
    ```

3.  **Ensure Data Files are Present:**

    Make sure you have the district boundary data files (`district_1_boundary.json` to `district_22_boundary.json`) in the same directory as the `terminal.py` script. These files contain the geographic boundaries of each Tehran municipality district in JSON format.

4.  **Run the application:**

    ```bash
    python terminal.py
    ```

5.  **Follow the Menu:**

    Once the application starts, you will see a main menu with the following options:

    ```
    --- Main Menu ---
    ------------------------------
      1 - Show Instructions
      2 - Enter Coordinates
      3 - Exit Application
    ------------------------------
    Choose option [1-3]:
    ```

    *   **Option 1 - Show Instructions:** Displays instructions on how to use the application.
    *   **Option 2 - Enter Coordinates:** Prompts you to enter latitude and longitude to find the district.
        *   Enter the latitude when asked.
        *   Enter the longitude when asked.
        *   The application will then display the Tehran municipality district for the given coordinates.
    *   **Option 3 - Exit Application:**  Closes the Tehran District Finder application.

    At any input prompt, you can type `exit` to quit the application.

## Data Source and District Maps

The district boundary data used in this application was collected using the **Overpass API** ([http://overpass-api.de/api/interpreter](http://overpass-api.de/api/interpreter)). The Overpass API is a powerful tool that allows querying geographic information from OpenStreetMap.

This repository includes two types of files related to Tehran municipality districts:

*   **District Boundary JSON Files (`district_1_boundary.json` to `district_22_boundary.json`):** These files contain the geographic boundaries of each Tehran municipality district in **JSON format**. This data, extracted from OpenStreetMap via Overpass API queries, is used by the `021` tool to determine district membership based on coordinates.

*   **District Map HTML Files (`district_1_map.html` to `district_22_map.html`):**  Alongside the JSON boundary data, this repository also provides **graphical maps for each Tehran district in HTML format**. These HTML files are intended to visually represent the districts and may include interactive features or more detailed map information. _(Note: If these HTML maps use specific libraries or have interactive elements, you may want to describe them further here.)_

_(**Note:** For specific details about the Overpass API queries used to extract the data, or the technologies used to create the HTML maps, you may want to include further documentation in the repository for reproducibility and clarity.)_

