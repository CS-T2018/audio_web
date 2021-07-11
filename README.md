# audio_web
 
# Audio Source Separator Design Specification

## User Interface
The webapp will have a *single* page with a simple audio player with a *play* and a *pause* button.
This will require some JavaScript to allow support for in-browser audio playing.
There will also be two buttons. One button is to select a file from the PC directory. This button should open an explorer window to select a mixture file in **WAV** format. Must also show the file name when upload is complete beside the *select file* button.
The second button is to perform the actual separation. Ideally, this button's functionality will be to type the relevant command in *XShell* to perform the separation on the GPU workstation. The command includes the file name as well as a location to store the separated files *(also WAV format)*.
> Maybe (TBD), we can add a third button to select a file from the output directory to play one of the separated files. This button can be positioned somewhere close to the *play/pause* button.
> Another possibility for the **maybe** pile is that, since we already have a few pretrained models, we can try to figure out how to implement them in the GPU workstation then we can provide a *drop-down menu* to give the user two or three options to perform the separation so that we can compare results. The logic here is that if we are able to implement one model, it shouldn't be too hard to add a second or third.

## Project Steps
> Maybe not in this particular order
> - ~~Design the user interface~~
> - ~~Add action listeners for the buttons~~
> - ~~Figure out how to connect the *webapp* to the *workstation*~~ 
> - Add additional trained models
> - ~~Obtain short (prefarably less than 10s *wav* files)~~
> - Test the webapp
> - Record demo video
> - Prepare for the presentation
> - Ace the presentation
> - Write the reports
> - **GO FOR VACATION**

## Key Problems
> - How to connect the *Django App* to the *GPU Workstation*
> - How to open an audio file in the browser and play it

## Languages
> - Python
> - HTML
> - JavaScript

*Can use any text editor **Recommend VSCode***
