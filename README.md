# The SARB
We created a bin, known as the SARB(self automated recycling bin), using the raspberry pi, that sorts out different types of waste materials automatically. The person has to put the item in the bin and then it will land on a slab of wood inside the bin. The item will be detected at first by a PIR sensor attached to our Raspberry PI. This sends a notification to the Camera Module(v2), which scans the object and then uses an image recognition software known as tensorflow (coded into our raspberry pi 4b) to work out whether the item is recyclable or not. A motor attached to the raspberry pi is instructed to move a lever, which is connected to a pivot, towards the required side of the right bin. Then the slab of wood collapses to put the item in its respective bin. We aim to reduce the amount of waste sent to landfills and incinerators and conserve natural resources. As recycling saves energy it also reduces greenhouse gas emissions, which helps to tackle climate change. Our automated recycling bin could be a step in the right direction to solve climate change. The items we used will be explained in detail next. 

# Step 1: Getting the code
Clone the GitHub onto a raspberry pi, using 'git clone ' on the raspberry pi terminal. 

# Step 2: Make the relevant folders.
First, make a folder called 'processed_datasets' in the current directory.

# Step 3:
