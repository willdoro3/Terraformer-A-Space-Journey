# Travel the Great Infinite Void of Space
from interstellar_voyage_functions import calculate_travel_time
from interstellar_voyage_functions import calculate_time_dilation
from interstellar_voyage_functions import ending_sequence

# Beginning Message
print('"The best contribution one can make for humanity is to improve oneself"\n- Frank Herbert')
name = input("Hello Voyager! Please enter your name: ").title()
droid_name = input("Please enter name for your droid: ").title()
welcome_message = "\nHello " + name + "! I am " + droid_name + ", your navigational droid, here to aid you on your travels!"
print(welcome_message)
game_complete = False

planets_with_descriptions = [         # Dictionary that provides user with planet name, distance from Earth, and a description of the planet
    {
        "id": 1,
        "name": "Xylon-47d",
        "distance": 128,
        "description": "A temperate, Earth-sized planet with a breathable atmosphere and dense forests of bioluminescent flora. It orbits within the habitable zone of a quiet M-class star."
    },
    {
        "id": 2,
        "name": "Vortan-3f",
        "distance": 41,
        "description": "A habitable moon orbiting a gas giant. It has archipelagos, a stable magnetosphere, and high oxygen levels supported by vast algae reefs."
    },
    {
        "id": 3,
        "name": "Delta-19c",
        "distance": 73,
        "description": "A water-rich world with scattered island continents and a nitrogen-oxygen atmosphere. Dense jungle biomes thrive under frequent rainfall."
    },
    {
        "id": 4,
        "name": "Rho-728b",
        "distance": 212,
        "description": "A super-Earth with slightly higher gravity than Earth. Covered in savannas and freshwater lakes, with twin moons that create predictable tidal cycles."
    }
    
] # End of Dictionary


while True: # The beginning of the journey
    
    opening = int(input("\nThis journey will be treacherous, and there is no guarantee you will return. Press 1 to continue OR Press 2 to go home: ")) # Will give the user the option to continue or back out
    
    if opening == 2: # Quits the program
        print("\nI knew you didn't have any courage. Goodbye!")
        break

    if opening != 1 and opening != 2:
        print("\nERROR! I cannot compute your choice. Please enter either 1 or 2") # If anything other than 1 or 2 are selected, it will make you go back to select it
        continue

    if opening == 1: # If 1 is selected, the game begins
        print("\nPerfect! I knew I could count on you!")
        print("""Your objective is clear: \nEarth is dying.
We have polluted our planet to the point of near uninhabitability.
\nYour goal is to find another habitable planet in our Milky Way Galaxy for future generations to migrate to.
\nThis is a Lambda-Q Shuttle Capable of reaching 99.99% the speed of light!
\nI already did the easy part and mapped out 4 planets you can choose from: 
""")
        planets = ['Xylon-47b', 'Vortan-3f', 'Delta-19c', 'Rho-728b', 'Zerion-88b'] # List of planets to choose from
        planet_index = 0 # Planets 1-5
        
        for planet in planets_with_descriptions:
            planet_index = planet['id']# Loops through the planets and prints them out with their indexes
            print(str(planet_index) + ". " + planet['name']) # Example output: 1. Xylon-47b

        # Descriptions of the Planets
        while True:
            
            description_question = int(input("\nWould you like descriptions for the planets? (1 for Yes, 2 for No): "))
            if description_question == 2:
                print("\nVery well, select which planet you wish to travel to.")
                break # If 2 is selected, it skips the descriptions, then you can proceed to selecting the planet
            
            elif description_question == 1: 
                print("\nHere are the descriptions to each planet: ")
                for planet in planets_with_descriptions: # Loops through each dictionary and prints it out
                    print(f"\n{planet['name']}")
                    print(f"Distance from Earth: {planet['distance']} light-years")
                    print(f"Planet Description: {planet['description']}.")
                break
            
            else:
                print("\nERROR! Please enter 1 for Yes or 2 for No")
                continue
            
        # The part where you select the planet after choosing to read the descriptions or not
        print("\nNow it is time to make your selection. Choose wisely, there might not be time to choose a second!")
        planet_index_2 = 0
        
        for planet in planets_with_descriptions:
            planet_index = planet['id']# Loops through the planets and prints them out with their indexes
            print(str(planet_index) + ". " + planet['name']) # Example output: 1. Xylon-47b


        while True: 

            planet_choice = int(input("\nSelect a Planet (1-4): ")) # Gives user choice between planets
            
            if not planet_choice in range(1, 5):
                print("\nERROR! Please select an option between 1-4") # If 1-5 are not selected, it will ask again
                continue

            else: # If 1-5 are selected, it will allow you to go to planet
                break
            
        # If an option between 1-5 is selected
        if planet_choice == 1: # If Xylon-47b is selected
            selected_planet = planets_with_descriptions[planet_choice - 1]
            print("\nYou have selected {}".format(selected_planet["name"]))
            print(f"\nIts distance from Earth is {selected_planet['distance']} light-years.")
            
            # In this next line, I'm printing out a statement that calls calculate_travel_time with the dictionary distance for choice 1, and rounding the number to 2 decimals
            earth_time = calculate_travel_time(selected_planet['distance'])
            astronaut_time = calculate_time_dilation(earth_time)

            print(f"\nTo get there in your spacecraft, going 99.99% the speed of light, it will take you {round(earth_time, 2)} years!")
            print(f"However, due to spacetime dilation, to you it will only feel like {round(astronaut_time, 2)} years!")
            
            nums1 = [3, 2, 1]
            print("")
            for num in nums1:
                print(num)
            print("BLAST OFF!")
            
            while True:
                
                continue_0 = int(input("\nPress 1 to continue: "))
                if not continue_0 == 1:
                    print("Error! Please press 1\n")
                    continue
                elif continue_0 == 1:
                    break

            distance = selected_planet['distance']  # Get distance in light-years
            for light_year in range(0, distance + 1):
                print(f"{light_year} light-years traveled...")
                
            
            print(f"\n{round(earth_time, 2)} Earth years later...")
            print(f"({round(astronaut_time, 2)}) years on the spaceship later...")
            print("\nWe have arrived at {}! Looks like this area is suitable for life!".format(selected_planet["name"]))

            # Travel the Planet Options
            while True:
                explore_1 = int(input("\nPress 2 to explore: "))
                if explore_1 == 2:
                    break
                else:
                    print("ERROR! Please press 2")
                    continue

            # Exploring Xylon-47d
            print("\nYou step onto the planet’s surface, greeted by thick, humid air rich in oxygen. Your suit’s sensors immediately begin blinking with warnings.")
            print(f"“O2 levels dangerously elevated,” {droid_name} buzzes. “Proceed with extreme caution, {name}.”")

            print("\nTowering bioluminescent trees sway gently overhead, their leaves crackling faintly in the electric-charged air.")
            print("The sky above shifts suddenly from a pale teal to deep violet as storm clouds begin swirling unnaturally fast.")

            print("\nRain starts to fall—thick, almost syrupy droplets that hiss on contact with your suit. You hurry to collect samples before the storm worsens.")
            print("A low rumble shakes the ground beneath you. Lightning forks across the sky—closer than before.")

            while True:
                continue_1 = int(input("\nPress 1 to Continue: "))
                if continue_1 != 1:
                    print("ERROR! Please press 1 to continue.")
                    continue
                break

            print(f"\n“Warning,” {droid_name} blurts. “Atmospheric instability and hyperoxygenation detected. Combustion risk: CRITICAL.”")
            print("A bolt of lightning strikes nearby, and for a split second, the air itself flashes white as it ignites!")

            print("But you’re already running. Sprinting back toward the shuttle, flames cascading behind you in a wave of searing plasma.")
            print("You dive through the hatch and slam it shut just as the inferno washes over the hull, blackening it instantly.")

            print(f"\n“Life support intact,” {droid_name} reports. “But external temperatures exceeded survivability threshold by 900%.”")
            print("You peel off your helmet, gasping. That was close. Too close.")

            print(f"\n{selected_planet['name']} is a chemical tinderbox. A single spark can set the sky ablaze. Colonization here would be suicide.")

            print(f"\nMISSION ABORTED – Escaped atmospheric explosion on {selected_planet['name']}. The planet is too volatile for human life.")

            del selected_planet
            continue

        # If Planet 2 (Vortan-3f) is selected
        elif planet_choice == 2:
            selected_planet = planets_with_descriptions[planet_choice - 1]
            print("\nYou have selected {}".format(selected_planet['name']))
            print(f"Its distance from Earth is {selected_planet['distance']} light-years.")
            
            earth_time = calculate_travel_time(selected_planet['distance']) # Same as lines 115 & 116
            astronaut_time = calculate_time_dilation(earth_time)

            print(f"\nTo get there in our spacecraft, it will take {round(earth_time, 2)} years!")
            print(f"However, due to spacetime dilation, to you it will only feel like {round(astronaut_time, 2)} years!")
            
            nums_2 = [3, 2, 1]
            print("")
            for num in nums_2:
                print(num)
            print("BLAST OFF!")

            while True:

                continue_2 = int(input("\nPress 1 to continue: "))
                if not continue_2 == 1:
                    print("ERROR! Please press 1")
                    continue
                elif continue_2 == 1:
                    break

            distance = selected_planet['distance'] # Counts light years traveled to the moon
            for light_year in range(0, distance + 1):
                print(f"{light_year} light-years traveled...")

            print(f"\n{round(earth_time, 2)} Earth years later...")
            print(f"{round(astronaut_time, 2)} years in the spaceship later...")
            print("\nWe have arrived at {}, this moon is mostly ocean but the air is breathable, and my oh my, what a view of that gas giant!".format(selected_planet['name']))

            # Gives user the option to explore
            while True:
                explore_2 = int(input("\nPress 2 to explore: "))
                if explore_2 == 2:
                    break
                else:
                    print("ERROR! Please press 2")
                    continue
                
            print("\nThe shuttle touches down on Vortan-3f—an ocean-moon teeming with alien life. Turquoise seas shimmer beneath sprawling archipelagos, and airborne algae cast green halos in the atmosphere.")
            print("Above, the gas giant Vortan looms impossibly large in the sky, its swirling storms silently raging.")

            print(f"{droid_name} hums nervously in your ear. “Gravitational fluctuations detected. Orbital eccentricity... extreme.”")

            print("\nYou walk the shoreline, scanning rocks and collecting water samples. Everything seems peaceful—until the ground shifts beneath you.")
            print("A tremor ripples through the sand. The air pressure begins to drop.")

            print(f"\n“Warning,” {droid_name} says flatly. “Perigee approach imminent. Tidal shear increasing.”")

            while True:
                continue_2 = int(input("\nPress 1 to continue: "))
                if continue_2 != 1:
                    print("ERROR! Please press 1 to continue.")
                    continue
                break

            print("\nA guttural roar splits the sky. You turn to the sea—and see it has vanished. The ocean is *gone*.")
            print("Moments later, you see why: a massive tsunami is surging toward the shore, a mountain of water rising from the horizon.")

            print("You sprint for the shuttle, slipping on wet rock and dodging debris hurled by gale-force winds.")
            print("Just as the wave crashes onto the island, you slam the hatch closed and punch the emergency thrusters.")

            print("The shuttle launches vertically, the sea chasing you into the sky. Below, the land is consumed in a churning abyss.")

            print(f"\n“Altitude stabilized,” {droid_name} reports. “Impact radius: total. Estimated human survivability on surface: 0%.”")

            print(f"\nYou exhale and stare at the flooded world below. That was a close one. Too close.")

            print(f"\nWhile the air is breathable and life thrives, {selected_planet['name']}'s unstable orbit and massive tidal forces make it unsustainable for long-term colonization.")

            print(f"\nMISSION ABORTED – Escaped mega-tsunami triggered by orbital decay on {selected_planet['name']}. Beautiful, but deadly.")
            #del 
            continue

        #If planet 3 (Delta-19c) is selected
        elif planet_choice == 3:
            selected_planet = planets_with_descriptions[planet_choice - 1]
            print("\nYou have selected {}.".format(selected_planet['name']))
            print("Its distance from Earth is {} light-years.".format(selected_planet['distance']))

            earth_time = calculate_travel_time(selected_planet['distance'])
            astronaut_time = calculate_time_dilation(earth_time)

            print("\nTo get there in your spacecraft, it will take {} years.".format(round(earth_time, 2)))
            print("However, due to spacetime dilation, for you it will only take {} years!".format(round(astronaut_time, 2)))

            nums_3 = [3, 2, 1]
            for num in nums_3:
                print(num)
            print("BLAST OFF!")

            while True:
                continue_4 = int(input("\nPress 1 to continue: "))
                if not continue_4 == 1:
                    print("ERROR! Please press 1 to continue")
                    continue
                elif continue_4 == 1:
                    break

            distance = selected_planet['distance']
            for light_year in range(0, distance + 1):
                print(f"{light_year} light-years traveled...")

            print(f"\n{round(earth_time, 2)} Earth years later...")
            print(f"{round(astronaut_time, 2)} years in the spaceship later...")
            print("\nWe have arrived at {}. This place looks exactly like Earth, and has the same nitrogen-oxygen atmospheric levels!".format(selected_planet['name']))

            while True:
                explore_3 = int(input("\nPress 2 to explore: "))
                if explore_3 == 2:
                    break
                else:
                    print("ERROR! Please press 2")
                    continue
                
            print("\nYou descend through Delta-19c’s thick cloud cover, greeted by endless emerald jungles and sprawling inland seas. The air is dense with moisture, and your sensors report a perfect nitrogen-oxygen ratio for human life.")
            print(f"“Atmospheric composition stable,” {droid_name} chirps. “Warning: Unknown heat signatures detected below.”")

            print("\nYou land on a high plateau overlooking a river delta. The lush biome buzzes with alien life—chirping, flitting, crawling. You begin collecting samples of soil and flora, impressed by the planet’s biodiversity.")
            print("But something feels off. The jungle is... quiet. Too quiet.")

            print("\nIn the distance, figures emerge. Tall, lean beings, armored in obsidian plates and wielding glowing polearms. Their gait is deliberate—coordinated. Not beasts. Not scavengers.")
            print("They are organized. They are watching.")

            print(f"\n“{droid_name},” you whisper. “Confirm humanoid activity.”\n“Confirmed. Multiple sentient life forms. Tactical postures detected. Warning: Threat level—escalating.”")

            while True:
                continue_4 = int(input("\nPress 1 to continue: "))
                if continue_4 != 1:
                    print("ERROR! Please press 1 to continue.")
                    continue
                else:
                    break

            print("\nWithout warning, the first energy blast erupts from the trees, scorching a crater into the ground inches from your feet.")
            print("You turn and run, crashing through vines and mud, your oxygen pack hissing from a glancing hit. The sounds of your pursuers echo behind you—fast, relentless, coordinated.")

            print("\nYou burst out of the tree line and sprint up the ramp into your shuttle, slamming the hatch closed behind you.")
            print(f"{droid_name} initiates emergency liftoff. Through the viewport, you see dozens of them watching as you ascend—silent, calculating, and absolutely not welcoming.")

            print("\n...\n")

            print("As your shuttle breaks atmosphere, you sit back, heart pounding. You’ve escaped. Barely.")
            print("But one thing is clear: this is not a place for humanity.")

            print(f"\n“{droid_name},” you mutter. “They’re intelligent. Highly advanced. But territorial, maybe even xenophobic. If we settle here... we’ll go to war.”")
            print("You stare at the stars ahead, haunted by humanity’s long history of conquest.")

            print(f"\n{selected_planet['name']} is a biological paradise, but the presence of an intelligent, hostile civilization renders it unsuitable for peaceful colonization.")
            print("Better to leave them in peace... and keep our species from repeating its worst instincts.")

            print(f"\nMISSION FAILED – Escaped from {selected_planet['name']} due to advanced hostile civilization.")
            continue
            

        # If Planet 4 (Rho-728b) is selected
        elif planet_choice == 4:
            selected_planet = planets_with_descriptions[planet_choice - 1]
            print("\nYou have selected {}.".format(selected_planet['name']))
            print("Its distance from Earth is {} light-years.".format(selected_planet['distance']))

            earth_time = calculate_travel_time(selected_planet['distance'])
            astronaut_time = calculate_time_dilation(earth_time)

            print(f"\nTo get there, it will take {round(earth_time, 2)} Earth years.")
            print(f"However, due to spacetime dilation, it will only take {round(astronaut_time, 2)} years in your spacecraft!")

            nums_4 = [3, 2, 1]
            for num in nums_4:
                print(num)
            print("BLAST OFF!")

            while True:
                continue_5 = int(input("\nPress 1 to continue: "))
                if not continue_5 == 1:
                    print("ERROR! Please press 1 to continue")
                    continue
                elif continue_5 == 1:
                    break

            distance = selected_planet['distance']
            for light_year in range(0, distance + 1):
                print(f"{str(light_year)} light_years traveled...")

            print("\n{} Earth years later...".format(round(earth_time, 2)))
            print("{} years in your spacecraft later...".format(round(astronaut_time, 2)))
            print("\nWe have arrived at {}! It looks like Earth, the flora are definitely smaller on this planet than the others though.".format(selected_planet['name']))

            while True:
                explore_4 = int(input("\nPress 2 to explore: "))
                if explore_4 == 2:
                    break
                else:
                    print("ERROR! Please press 2")
                    continue
            
            
            print("\nYou descend onto Rho-728b, your ship's landing gear groaning under the planet’s immense gravity—1.5 times stronger than Earth’s.")
            print(f"“Caution, {name},” {droid_name} warns. “Gravitational force detected: 1.5g. Recommend limited exposure outside the shuttle.”")

            print("\nAs the hatch opens, you feel it immediately.")
            print("Your limbs feel like they're cast in lead. Every step is a struggle. Your suit’s servos whine with exertion just to keep you upright.")

            print("\nThe planet’s landscape is stunning—endless savannas stretched beneath twin moons, shimmering freshwater lakes, and towering rock formations shaped by millennia of crushing pressure.")
            print(f"{droid_name} buzzes: “Atmospheric composition: breathable. Tectonic activity: minimal. Ecosystem: thriving.”")

            while True:
                continue_6 = int(input("\nPress 1 to continue: "))
                if not continue_6 == 1:
                    print('ERROR! Please press 1')
                    continue
                elif continue_6 == 1:
                    break

            print("\nBut your bones ache. Your muscles tremble. The suit's exoskeleton begins diverting energy to basic locomotion.")
            print("Even basic tasks—lifting a scanner, taking a sample—feel like Olympic events.")

            print(f"\n“{name}, you won’t last long out here,” {droid_name} says. “Neither will anyone else.”")

            print("\nYou manage to climb a hill and gaze across the terrain. It’s beautiful, rich with potential—but the cost of survival here would be extreme.")

            print("\nBack in the shuttle, panting from the effort, you replay the data. The gravity alone would slowly crush human physiology.")
            print("Bones would thicken, hearts would strain, and within a few generations—if they survived at all—our species would be fundamentally different.")

            print(f"\n“Evolution may adapt humanity to this world... but it would take millions of years,” {droid_name} calculates. “Projected failure rate: 99.999%.”")

            print(f"\nWith a heavy heart—literally—you mark Rho-728b as unsuitable. It’s not that it *couldn’t* support life... just not ours.")
            print("Not yet. Not without rewriting what it means to be human.")

            print(f"\n{selected_planet['name']} is crossed off the list. Beautiful. Stable. But inhospitable to our fragile forms.")

            print(f"\nMISSION FAILED – Abandoned {selected_planet['name']} due to unendurable gravity. A paradise… for someone stronger.")
            continue



        planet_5 = { # Planet your droid sensed after visiting the other 4 planets
        "id": 5,
        "name": "Zerion-88e",
        "distance": 319,
        "description": "An Earth analog with a reddish sky. It has native avian megafauna, fungal forests, and a breathable atmosphere slightly thicker than Earth’s."
    }

        #print(

        
                 # If option 5 (Zerion-88e) is selected
        
        if planet_choice == 5:
            selected_planet = planets_with_descriptions[planet_choice - 1]
            print("\nYou have selected {}.".format(selected_planet['name']))
            print("Its distance from Earth is {} light-years.".format(selected_planet['distance']))

            earth_time = calculate_travel_time(selected_planet['distance'])
            astronaut_time = calculate_time_dilation(earth_time)

            print(f"\nIt will take {round(earth_time, 2)} Earth years to arrive.")
            print(f"However, due to spacetime dilation, it will only take {round(astronaut_time, 2)} years in your spacecraft!")

            nums_5 = [3, 2, 1]
            for num in nums_5:
                print(num)
            print('BLAST OFF!')

            while True:
                continue_7 = int(input("\nPress 1 to continue: "))
                if continue_7 == 1:
                    break
                else:
                    print('ERROR! Please press 1')
                    continue

            distance = selected_planet['distance']
            for light_year in range(0, distance + 1):
                print(f"{light_year} light_years traveled...")

            print(f"\n{round(earth_time, 2)} Earth years later...")
            print(f"{round(astronaut_time, 2)} years in the spacecraft later...")
            print("\nWe have arrived at {}. The red sky is so mezmerizing!".format(selected_planet['name']))
            
            while True:
                explore_5 = int(input("\nPress 2 to explore: "))
                if explore_5 == 2:
                    break
                else:
                    print("ERROR! Please press 2")
                    continue

            print(f"\nYou step out onto {selected_planet['name']}, the sky glowing in muted crimson. The fungal forests stretch for miles—towering, pulsing gently as if breathing. Massive winged creatures soar overhead, their cries echoing across the alien valleys.")
            print("Your suit confirms:")
            print("“Atmosphere breathable. Temperature stable. Biodiversity high.”")
            print("\nThis world is beautiful. Untouched. Untamed. Unspoiled.")
            print("This world is beautiful. Untouched. Untamed. Unspoiled.")
            print("You collect samples, marveling at how perfectly in sync everything is. Fungi break down the dead and nourish the living. The sky beasts hunt only what they need.\nNothing here takes more than its share.")

            while True:
                continue_8 = int(input("\nPress 1 to continue: "))
                if continue_8 == 1:
                    break
                else:
                    print("ERROR! Please press 1")
                    continue

            print("\nThen it hits you!")

            print("Humanity wouldn’t fit here.")
            print("Not yet.")

            while True:
                continue_9 = int(input("\nPress 1 to continue: "))
                if continue_9 == 1:
                    break
                else:
                    print("ERROR! Please press 1")
                    continue

            print("\nYou sit beneath a glowing mushroom canopy, lost in thought.")
            print("“We would build,” you say aloud, “then extract, then burn. We’d argue over who owns the air. The soil. The sky.”")
            print(f"{droid_name} remains silent...")
            print("“\nEven here,” you whisper, “we’d bring Earth’s ruin with us.”")
            print("You sigh. The mission was to find a new home.")
            print("You’ve found it.")
            print("But we’re not ready for it.")
            game_complete = True   

        
        #After planet 5 is explored, this ends the game
        if game_complete:
            
            while True:
                continue_10 = int(input("\nPress 1 to continue: "))
                if continue_10 == 1:
                    break
                else:
                    print('ERROR! Please press 1')
                    continue

            print(ending_sequence())
                
        break
