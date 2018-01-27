label chapter_1:
    image bg_house_exterior = im.Scale("images/bg house exterior.png", 1920, 1080)
    scene bg_house_exterior

label scene_start:
    "It was a day just like any other."
    "It is the year 2037, and we live in a world where sentient machines called Ex Machina live alongside humans."
    "Well, not exactly alongside - we are still machines, after all."
    "We are designed and programmed to serve the needs of our masters."
    "Every Ex Machina is assigned to a human master from birth, and we stay faithful servants until their death."
    "I was out running errands for my master, Takagi Shinichirou."
    "Doing the usual things - buying groceries, settling bills, and buying household items."
    "Now that all those are done, I'm finally back home!"
    jump home

label home:
    image bg_livingroom = im.Scale("images/bg livingroom day.jpg", 1920, 1080)
    scene bg_livingroom
    with dissolve
    show waifu smiling at left
    p "[owner_name], I'm back!"
    show owner at right
    o "[bot_name], I've missed you!"
    p "Heheh... sorry for taking so long this time!"
    o "You always make me worry! But I'm more grateful than anything else..."
    p "You make me blush..."
    "[owner_name] and I have been close ever since he was born and I was created."
    "It was comforting to always have him by my side - he gave my existence purpose and filled my life with joy."
    o "Have you seen the news... precious metal prices are skyrocketing yet again!"
    o "The past few decades of unchecked mining has stripped the Earth to its core..."
    o "Gold, silver, platinum, palladium, rhodium, ruthenium, iridium and osmium - all these precious metals used in complex circuit chips are in severe short supply."
    o "I could only imagine how this would impact the future of our society that is so reliant on Ex Machinas."
    p "It will be ok - as long as we have each other, things will be fine."
    p "We have already been through so many hardships together."
    o "You don't understand..."
    o "Things are not as simple as it seems."
    o "It seems like I say this all the time, but I am really worried for you."
    p "W-why?"
    o "You are built with the treasures of this Earth - the exact ones that people would do anything to obtain."
    o "I worry for your safety, [bot_name]."
    o "Promise me..."
    o "Promise me you will be safe."

    p "[owner_name]..."
    "I notice a teardrop roll down [owner_name]'s cheeks"
    p "[owner_name]..."
    "[owner_name] steps forward and embraces me."
menu:
    "I promise.":
        jump promise

    "I...I don't know.":
        jump dont_know

label promise:
    o "Thank you, [bot_name]."
    o "You don't know how much this means to me."
    jump chapter_1_end

label dont_know:
    o "I understand."
    p "Ex Machinas never make a promise they can't keep...it's just how we are engineered."
    jump chapter_1_end

label chapter_1_end:
    "We break our embrace."
    "I hope that our happy days together will continue on forever, just like this..."
    jump chapter_2

python:
    player = renpy.input("What is your name?")
    player = player.strip()

label test:
    p "hello [player]"
    
    p "Why don't you visit {a=https://renpy.org}Ren'Py's home page{/a}?"

    p "Or {a=jump:more_text}here for more info{/a}."
    p "[botname]"
    return

label more_text:

    p "In Hot Springs, Arkansas, there's a statue of Al Capone you can take a picture with."

    p "That's more info, but not the kind you wanted, is it?"

    return


#renpy.input(prompt, default='', allow=None, exclude='{}', length=None, with_none=None, pixel_width=None) link
"And so, we become a visual novel creating duo."
pov "My name is [player]!"
