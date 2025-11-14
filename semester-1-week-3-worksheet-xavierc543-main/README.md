[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21161138)
# COMP1850 Worksheet 1.3

You should complete and upload the Portfolio task
to Gradescope for grading. 

Please make sure to add your name and the date to the file. 

## `Practice task - Recaman Sequence`

The template file recaman.py contains brief instructions for completing the task.

You can find further details on the sequence on the Worksheet and via Wikipedia.

Hint: Use methods available for the built in data structures to simplify the implementation.

## `Portfolio task - Traffic light`

This task is a simple example of a 'state-machine'. You will cover this topic in more
detail in COMP1860. As an introduction you will implement a simple model that cycles
through several lighting 'states': red -> red-amber -> green -> amber -> red -> ...

Hint: you need an overall clock for the simulation and a separate timer for each light stage

The autograder will incrementally test each transition: red -> red-amber, then red -> red-amber -> green, etc.
