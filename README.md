# FRC Event Visualizer

This is a simple application that scrapes the event data for qualifier matches from any give FRC event and puts that information into a database. It then simply creates an image using that information to populate it.

### Image

The image is divided between the top and the bottom. The upper part of the image shows the red alliances and their scores, the bottom shows the blue alliances and their scores.

### Alliance "Colors"

The colors that denote each alliance for each match are gotten from each team number. The team number is divided by 24.5 (because it's RGB values, 255 is the highest, so take the highest rookie number, divide by 255 to get the value to divide by for everyone else). Then the numbers are passed into (R, G, B) based on their position on field (eg: red 1, red 2, red 3).

The darker an alliance is, the older the teams are as a whole. The lighter it is, the more rookie the teams are.

### Scores

The values that are displayed for the scores will not be exact in the code's current run state. This is in order to get better looking visuals, though all the scores are still correct relative to each other.

### Example:

This is the image that was created using the data from the Qualifiers at the Palmetto Regional 2016.

![alt tag](https://raw.githubusercontent.com/alicen6/frc_visualizer/master/2016scmb.jpeg)
