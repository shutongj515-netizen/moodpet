# MoodPet - Processing Python Mode (Python 2 / Jython)
# No external images, audio libraries, or extra files required.
# setup() runs once; draw() runs continuously.

# Learning Reference: Creative Coding class activities
# Additional Reference: Reas & Fry - Getting Started
# https://py.processing.org/tutorials/gettingstarted/

# Store the five dog breeds available for selection
DOGS = ["Pug", "Border Collie", "Pomeranian", "Shiba", "French Bulldog"]
# Track which screen is currently displayed
screen = 0
# Store the selected dog breed
selected_dog = 0
# Store the name entered by the user
dog_name = ""
# Set the dog's starting emotion
mood = "normal"
# Set the dog's starting energy level
energy = 80
# Record the time of the last interaction
last_activity = 0
# Record when the dog starts resting
rest_start = 0
# Record when the current emotion begins
mood_start = 0
# Record when the feeding effect ends
feed_until = 0
# Store the name of the button being pressed
pressed_button = ""
# Record when the button effect ends
button_until = 0
# Set the starting background colour
bg_r, bg_g, bg_b = 245.0, 240.0, 230.0



# Learning Reference: The Coding Train - Creative Coding tutorials
# Additional Reference: Reas & Fry - Getting Started
# https://py.processing.org/tutorials/gettingstarted/

# Set up the game when the program starts
def setup():
    # Set the game window to 800 by 600 pixels
    size(800, 600)
    # Set the animation speed to 30 frames per second
    frameRate(30)
    # Align text to the centre of the screen
    textAlign(CENTER, CENTER)

# Learning Reference: Processing.py - Getting Started
# https://py.processing.org/tutorials/gettingstarted/

# Learning Reference: The Coding Train - Creative Coding tutorials
# Additional Reference: Creative Coding class activities
# https://py.processing.org/tutorials/gettingstarted/

# Update the game screen continuously
def draw():
    # Access the shared background and button variables
    global bg_r, bg_g, bg_b, pressed_button
    # Update the dog's state during the interaction screen
    if screen == 2:
        update_pet()
       # Store background colours for different emotions
        palettes = {"normal": (245, 240, 230), "happy": (255, 239, 211),
                    "sad": (197, 209, 226), "excited": (255, 224, 193),
                    "tired": (214, 211, 217), "resting": (178, 189, 220)}
       # Choose a background colour based on the dog's emotion
        target = palettes[mood]
        # Gradually adjust the red background value
        bg_r += (target[0] - bg_r) * 0.12
        # Gradually adjust the green background value
        bg_g += (target[1] - bg_g) * 0.12
        # Gradually adjust the blue background value
        bg_b += (target[2] - bg_b) * 0.12
        # Draw the background with the updated RGB values
        background(int(bg_r), int(bg_g), int(bg_b))
        # Display the main interaction screen
        draw_play_screen()
    # Run this section when the user is not on the interaction screen
    else:
        # Set the default background colour
        background(245, 240, 230)
        # Check whether the user is on the welcome screen
        if screen == 0:
            # Display the welcome screen
            draw_start_screen()
        else:
            draw_select_screen()
    # Check whether the button feedback time has ended
    if millis() > button_until:
        # Clear the currently pressed button
        pressed_button = ""


# Learning Reference: Reas & Fry - Interactivity
# https://py.processing.org/tutorials/interactivity/

# Create a reusable function for drawing buttons
def button(label, x, y, w, h, color_rgb):
    # Draw rectangles using their centre coordinates
    rectMode(CENTER)
    # Set the outline colour and transparency
    stroke(110, 100, 100, 90)
    # Set the thickness of the button outline
    strokeWeight(2)
    # Check whether this button is currently being pressed
    if pressed_button == label:
        # Make the button darker when it is pressed
        fill(max(0, color_rgb[0] - 30), max(0, color_rgb[1] - 30), max(0, color_rgb[2] - 30))
    # Use the normal button colour when it is not pressed
    else:
        # Apply the original RGB colour
        fill(*color_rgb)
    # Draw the button with rounded corners
    rect(x, y, w, h, 14)
    # Set the button text colour to white
    fill(255)
    # Align the button label to the centre
    textAlign(CENTER, CENTER)
    # Set the button label font size
    textSize(21)
    # Display the text on the button
    text(label, x, y - 2)

# Learning Reference: Reas & Fry - Getting Started
# https://py.processing.org/tutorials/gettingstarted/

# Create the welcome screen of MoodPet
def draw_start_screen():
    # Set the title colour
    fill(65, 61, 72)
    # Set the title font size
    textSize(52)
    # Display the name of the game
    text("MoodPet", 400, 150)
    # Set a smaller font size for the subtitle
    textSize(20)
    # Display the welcome message
    text("Your virtual puppy friend", 400, 205)
   # Draw the dog on the welcome screen
    draw_dog(400, 340, 0.55, 2, "happy")
    # Create the Start button
    button("Start", 400, 510, 210, 64, (116, 180, 140))


# Learning Reference: 
# Additional Reference: The Coding Train - Creative Coding tutorials

# Create the dog selection and naming screen
def draw_select_screen():
    # Set the colour for the text
    fill(60)
    # Set the heading font size
    textSize(32)
    # Display the dog selection heading
    text("Choose Your Dog", 400, 62)
    # Repeat the next drawing instructions for five dog breeds
    for i in range(5):
    # Calculate the horizontal position of each dog
        x = 100 + i * 150
        # Check whether this dog is selected
        if i == selected_dog:
            # Remove the fill colour from the selection border
            noFill()
            # Set the colour of the selection border
            stroke(95, 140, 215)
            # Set the thickness of the selection border
            strokeWeight(4)
            # Draw a rectangle around the selected dog
            rectMode(CENTER)
            rect(x, 240, 136, 178, 15)
            
        # Draw each dog with its breed and normal emotion    
        draw_dog(x, 228, 0.40, i, "normal")
        # Set the text colour for the dog breed
        fill(60)
        # Set the font size for the dog breed name
        textSize(13)
        # Display the name of each dog breed
        text(DOGS[i], x, 320)
    # Set the colour of the naming section text    
    fill(70)
    # Set the font size for the naming instruction
    textSize(19)
    # Ask the user to name their puppy
    text("Name your puppy:", 400, 391)
    # Draw rectangles using their centre coordinates
    rectMode(CENTER)
    # Set the input box colour to white
    fill(255)
    # Set the input box outline colour
    stroke(155)
    # Draw the name input box with rounded corners
    rect(400, 443, 400, 54, 9)
    # Set the input text colour
    fill(60)
    # Set the font size for the input text
    textSize(22)
    # Show the entered dog name or a placeholder if it is empty
    text(dog_name if dog_name else "Type a name here", 400, 442)
    # Draw the Continue button
    button("Continue", 400, 525, 200, 55, (116, 180, 140))


# Learning Reference: The Coding Train - 5.2: If, Else If, Else
# https://www.youtube.com/watch?v=mVq7Ms01RjA

# Create a function to draw the dog using Processing shapes
def draw_dog(x, y, s, breed, state):
    # Save the current drawing settings
    pushMatrix()
    # Move the drawing position to the dog's coordinates
    translate(x, y)
    # Check whether the dog is happy
    if state == "happy":
        # Make the dog bounce gently
        translate(0, -abs(sin(frameCount * 0.18)) * 13)
    # Check whether the dog is excited
    elif state == "excited":
        # Make the dog jump higher and faster
        translate(0, -abs(sin(frameCount * 0.35)) * 24)
        # Rotate the dog slightly to create an excited movement
        rotate(sin(frameCount * 0.2) * 0.06)
    # Check whether the dog is sad
    elif state == "sad":
        # Move the dog slightly downward
        translate(0, 12)
    # Check whether the dog is resting
    elif state == "resting":
    # Move the dog downward into a resting position
        translate(0, 30)
        # Make the dog smaller while resting
        scale(1, 0.7)
    # Check whether the dog is tired
    elif state == "tired":
        # Move the tired dog slightly downward
        translate(0, 16)
    # Apply the overall size of the dog
    scale(s)
    # Store the coat colours for the five dog breeds
    coats = [(192, 151, 108), (235, 230, 222), (219, 153, 78),
             (212, 133, 67), (195, 184, 174)]
    # Select the coat colour based on the chosen breed
    coat = coats[breed]
    # Remove outlines from the dog's shapes
    noStroke()
    # Set the dog's body colour
    fill(*coat)
    # Draw the main body of the dog
    ellipse(0, 85, 155, 145)
    # Draw the left leg
    ellipse(-48, 143, 45, 30)
    # Draw the right leg
    ellipse(48, 143, 45, 30)
    # ears
    if breed == 0 or breed == 4:
        # Choose a slightly darker colour for the ears
        fill(coat[0] - 28, coat[1] - 22, coat[2] - 16)
        # Draw the left rounded ear
        ellipse(-69, -42, 58, 95)
        # Draw the right rounded ear
        ellipse(69, -42, 58, 95)
    else:
        # Use the dog's coat colour
        fill(*coat)
        # Draw the left pointed ear
        triangle(-78, -28, -66, -128, -12, -70)
        # Draw the right pointed ear
        triangle(78, -28, 66, -128, 12, -70)
        # Set a lighter colour for the inside of the ears
        fill(233, 166, 156)
        # Draw the inside of the left ear
        triangle(-66, -46, -61, -103, -32, -67)
        # Draw the inside of the right ear
        triangle(66, -46, 61, -103, 32, -67)
        # Set the dog's face colour
    fill(*coat)
    # Draw the dog's head
    ellipse(0, -15, 170, 157)
    # Check whether the dog is a Border Collie
    if breed == 1:
        # Set the white facial marking colour
        fill(255)
        # Draw the white marking on the dog's face
        ellipse(0, -12, 53, 118)
    # Set the colour for the dog's muzzle
    fill(255, 245, 225)
    # Draw the dog's muzzle
    ellipse(0, 28, 91, 66)
    # Set the colour of the dog's eyes
    fill(55, 45, 43)
    # Draw the left eye
    ellipse(-34, -27, 14, 19)
    # Draw the right eye
    ellipse(34, -27, 14, 19)
    # Draw the dog's nose
    ellipse(0, 15, 28, 20)
    # Set the colour and thickness of the mouth outline
    stroke(65, 47, 48)
    strokeWeight(3)
    # Remove the fill colour from the mouth
    noFill()
    # Draw the dog's curved mouth
    arc(0, 27, 34, 26, 0, PI)
    # Remove outlines before drawing the cheeks
    noStroke()
     # Check whether the dog is happy or excited
    if state == "happy" or state == "excited":
        # Set a pink colour for the dog's cheeks
        fill(242, 145, 151)
        # Draw the left pink cheek
        ellipse(-52, 3, 22, 13)
        # Draw the right pink cheek
        ellipse(52, 3, 22, 13)
    # Restore the original drawing settings
    popMatrix()


# Define the function that draws the main interaction screen
def draw_play_screen():
    # Set the text colour
    fill(65)
    # Set the font size for the dog's name
    textSize(36)
     # Display the name entered by the user
    text(dog_name, 400, 65)
    # Draw the selected dog with its current emotion
    draw_dog(290, 237, 1.3, selected_dog, mood)
    # Check whether the dog is resting
    if mood == "resting":
        fill(75, 83, 140)
        # Set the size of the sleeping symbol
        textSize(35)
        # Display Zzz when the dog is resting
        text("Zzz", 460, 164)
    # Check whether the dog is happy
    elif mood == "happy":
        # Set the colour of the heart symbol
        fill(233, 91, 111)
        # Set the size of the heart symbol
        textSize(36)
         # Display a heart when the dog is happy
        text("<3", 450, 164)
    # Check whether the dog is sad
    elif mood == "sad":
        # Set the colour of the sad symbol
        fill(70, 100, 170)
        # Set the size of the sad symbol
        textSize(34)
        # Display dots to show sadness
        text("...", 450, 164)
    # Check whether the dog is excited
    elif mood == "excited":
        # Set the colour of the excitement symbol
        fill(240, 170, 50)
        # Set the size of the excitement symbol
        textSize(38)
        # Display stars when the dog is excited
        text("* *", 450, 164)
 # Check whether the feeding animation is still active       
    if millis() < feed_until:
        # Set the colour of the food icon
        fill(170, 113, 56)
        # Draw a small food icon
        ellipse(445, 295, 48, 30)
        # Set the text colour
        fill(255)
        # Set the text size for the feeding message
        textSize(16)
        # Display a feeding message
        text("Yum!", 448, 336)
    # Set rectangle drawing mode to centre
    rectMode(CENTER)
    # Set the background colour of the information panel
    fill(255, 250, 245)
    # Set the outline colour of the information panel
    stroke(204, 193, 182)
    # Draw the panel for mood and energy information
    rect(400, 402, 465, 68, 12)
    # Set the text colour for the mood label
    fill(65)
    # Set the font size for the mood label
    textSize(19)
    # Display the dog's current mood
    text("Mood: " + mood.capitalize(), 290, 400)
    # Remove outlines for the energy bar
    noStroke()
    # Set the background colour of the energy bar
    fill(216)
    # Draw the background of the energy bar
    rect(493, 402, 150, 23, 6)
    # Set the fill colour of the energy bar
    fill(104, 182, 121)
    # Use corner-based rectangle positioning
    rectMode(CORNER)
    # Draw the energy bar based on the current energy percentage
    rect(418, 390, 150 * energy / 100.0, 23, 6)
    # Set the text colour for the energy percentage
    fill(55)
    # Set the font size for the energy percentage
    textSize(13)
    # Display the current energy level as a percentage
    text(str(energy) + "%", 493, 401)
    # Store the colours for the four interaction buttons
    colors = [(127, 184, 153), (228, 169, 110), (116, 161, 217), (162, 149, 184)]
    # Repeat the following instructions for the four interaction buttons
    for i, label in enumerate(["Pet", "Feed", "Play", "Rest"]):
        # Draw each button with its label, position and colour
        button(label, 145 + 170 * i, 507, 145, 62, colors[i])
    # Set the colour of the instruction text    
    fill(90)
    # Set the font size of the instruction text
    textSize(14)
    # Explain what the four interaction buttons do
    text("Pet to cheer up  |  Feed for energy  |  Play to have fun  |  Rest to recharge", 400, 568)

# Learning Reference: The Coding Train - 5.2: If, Else If, Else
# https://www.youtube.com/watch?v=mVq7Ms01RjA

# Define a function to change the dog's emotion
def change_mood(new_mood):
    # Access the global mood and timing variables
    global mood, mood_start, rest_start
    # Only update the mood when it is different
    if mood != new_mood:
        # Store the dog's new emotion
        mood = new_mood
        # Record the time when the emotion changes
        mood_start = millis()
        # Check whether the dog starts resting
        if mood == "resting":
            # Record when the resting period begins
            rest_start = millis()

# Learning Reference: The Coding Train - 5.2: If, Else If, Else
# https://www.youtube.com/watch?v=mVq7Ms01RjA
# Additional Reference: Reas & Fry - Getting Started
# https://py.processing.org/tutorials/gettingstarted/

# Define a function to update the dog's behaviour
def update_pet():
    # Access the dog's energy and last interaction time
    global energy, last_activity
    # Get the current running time of the program
    now = millis()
    # Check whether the dog is resting
    if mood == "resting":
        # Increase energy once every six frames
        if frameCount % 6 == 0:
            # Increase energy without going above 100
            energy = min(100, energy + 1)
        # Check whether the dog has rested long enough and recovered energy    
        if now - rest_start >= 4000 and energy >= 70:
            # Return the dog to its normal emotion
            change_mood("normal")
            # Update the last activity time
            last_activity = now
 # Update the dog when it is not resting           
    else:
        # Check whether the user has been inactive for 60 seconds
        if now - last_activity >= 60000:
            # Make the dog rest after a long period of inactivity
            change_mood("resting")
        # Check whether the user has been inactive for 30 seconds    
        elif now - last_activity >= 30000:
            # Make the dog sad when it has not received attention
            change_mood("sad")
        # Check whether the happy or excited emotion has lasted long enough    
        elif mood in ("happy", "excited") and now - mood_start > 5500:
            # Return to normal if energy is sufficient, otherwise become tired
            change_mood("normal" if energy > 20 else "tired")
       # Check whether the dog's energy is very low     
        if energy <= 20 and mood != "sad":
            # Change the dog's emotion to tired
            change_mood("tired")

# Learning Reference: Reas & Fry - Interactivity
# https://py.processing.org/tutorials/interactivity/

# Define a function to check whether a point is inside a rectangle
def inside(x, y, cx, cy, w, h):
    # Compare the mouse position with the rectangle's boundaries
    return abs(x - cx) <= w / 2 and abs(y - cy) <= h / 2

# Learning Reference: Reas & Fry - Interactivity
# https://py.processing.org/tutorials/interactivity/
# Additional Reference: The Coding Train - 5.2: If, Else If, Else
# https://www.youtube.com/watch?v=mVq7Ms01RjA

# Define a function that responds to mouse clicks
def mousePressed():
    # Access the global variables used for interaction
    global screen, selected_dog, energy, last_activity
    # Access the variables used for feeding and button feedback
    global feed_until, pressed_button, button_until
    # Check whether the user is on the welcome screen
    if screen == 0:
        # Check whether the Start button has been clicked
        if inside(mouseX, mouseY, 400, 510, 210, 64):
            # Move to the dog selection screen
            screen = 1
     # Check whether the user is on the dog selection screen       
    elif screen == 1:
        # Repeat the following instructions for the five dog breeds
        for i in range(5):
            # Check whether the user clicks on a dog breed
            if inside(mouseX, mouseY, 100 + i * 150, 240, 136, 178):
                # Store the selected dog breed
                selected_dog = i
                # Stop checking other mouse interactions
                return
        # Check whether the Continue button is clicked    
        if inside(mouseX, mouseY, 400, 525, 200, 55):
         # Start the game with the selected dog 
            start_play()
  # Handle mouse clicks on the main interaction screen          
    else:
        # Store the names of the four interaction buttons
        labels = ["Pet", "Feed", "Play", "Rest"]
        # Check each of the four interaction buttons
        for i in range(4):
            # Check whether the mouse is inside the current button
            if inside(mouseX, mouseY, 145 + i * 170, 507, 145, 62):
                # Remember which button was clicked
                pressed_button = labels[i]
                # Set how long the button feedback will appear
                button_until = millis() + 200
                # Record the time of the user's interaction
                last_activity = millis()
            # Check whether the Pet button was clicked
                if i == 0:
                    # Make the dog happy when it is petted
                    change_mood("happy")
                # Check whether the Feed button was clicked    
                elif i == 1:
                    # Increase the dog's energy without exceeding 100
                    energy = min(100, energy + 15)
                    # Display the feeding animation for 1.7 seconds
                    feed_until = millis() + 1700
                    # Make the dog happy after feeding
                    change_mood("happy")
               # Check whether the Play button was clicked     
                elif i == 2:
                # Reduce the dog's energy after playing    
                    energy = max(0, energy - 20)
                # Make the dog excited if it has enough energy
               # Otherwise, make the dog tired     
                    change_mood("excited" if energy > 20 else "tired")
                # Handle the Rest button    
                else:
                   # Change the dog's emotion to resting 
                    change_mood("resting")
                # Stop checking other buttons after a click    
                return

# Learning Reference: Reas & Fry - Getting Started
# https://py.processing.org/tutorials/gettingstarted/
# Learning focus: Functions, variables, and game state.

# Define a function to start the main game
def start_play():
   # Access the game screen, dog name, activity time and energy 
    global screen, dog_name, last_activity, energy
    # Check whether the user entered a name
    if not dog_name.strip():
        # Use the selected breed as the default dog name
        dog_name = DOGS[selected_dog]
    # Switch to the main interaction screen    
    screen = 2
    # Set the dog's starting energy to 80
    energy = 80
    # Record the time when the game starts
    last_activity = millis()
    # Set the dog's initial emotion to normal
    change_mood("normal")

# Learning Reference: Reas & Fry - Interactivity
# https://py.processing.org/tutorials/interactivity/
# Additional Reference: The Coding Train - If, Else If, Else
# https://www.youtube.com/watch?v=mVq7Ms01RjA

# Define a function to respond to keyboard input
def keyPressed():
    # Access the dog's name variable
    global dog_name
    # Check whether the user is on the naming screen
    if screen != 1:
        # Ignore keyboard input on other screens
        return
    # Check whether the Enter or Return key is pressed
    if key == ENTER or key == RETURN:
        # Start the game after naming the dog
        start_play()

    # Check whether the Backspace key is pressed
    elif key == BACKSPACE:
        # Remove the last character from the dog's name
        dog_name = dog_name[:-1]

    # Check whether a normal character is typed
    elif key != CODED and len(dog_name) < 18:
        # Only allow characters with an ASCII value of 32 or higher
        if ord(key) >= 32:
            # Add the typed character to the dog's name
            dog_name += key
