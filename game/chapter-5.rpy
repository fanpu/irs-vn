label Chapter5:
 image wasteland = "wasteland3.jpg"
 scene wasteland
 play music "x.mp3"
 image far_girl= "farawaygirl.gif"
 show far_girl at right

 p "(Does she know the building where Shin lives?)"
 
 image close_girl = "closegirl.gif"
 hide far_girl
 show close_girl at right
 show waifu at left

 p "Hello"
 g "Oh, a model 3.4. Were you abandoned? Thrown away for the latest model?"
 p "No"
 
 hide close_girl
 image bored_girl = "boredgirl.gif"
 show bored_girl at left
 
 g "Good for you. Now what do you want from me?"
 
 hide waifu
 image confused_waifu = "confusedwaifu.gif"
 show waifu_confused
 
 "..."
 g "No one just approaches for a friendly chat these days. Go on."
 
 hide waifu_confused
 show waifu at left
 
 p "...Do you know how to get to the Midtown Tower to from here?"
 g "What for? It's the same everywhere. Same crumbling buildings, same desolate land." 
 p "I need to get back to someone."
 g "An android, going back to someone. Who do you have?"
menu: 
 "My owner":
   jump owner5 
 "My lover":
   jump lover5

label owner5:
 hide bored_girl
 image amused_girl = "amusedgirl.gif"
 show amused_girl at right

 g "You androids, always programmed to go back."
 g "Well, at least you have a purpose"
 g "..."
 g "You know what, I'll help you, if you help me. Something simple. What'd you say to that?"
 p "...I'll help."
 jump Chapter5mid
  
label lover5:
 image laugh_girl = "laughinggirl.gif"
 hide bored_girl
 show laugh_girl at right
 
 g "You androids are so cute! The unconditional love you feel for your owners is just adorable!"
 g "Hah, I haven't laughed in a long time."
 
 hide laugh_girl
 show amused_girl
 
 g "I suppose I should help you in return."
 g "Come with me, I have a task for you first."
 p "...Fine."
 jump Chapter5mid
 
label Chapter5mid:
 image messyroom = "messyroom.jpg"
 scene messyroom
 #stop music "wasteland.mp3"
 #start music "messyroom.mp3"
 hide amused_girl
 image girl = "girl.gif"
 show girl at right
 show waifu at left
 
 
 g "I have not met another person, or anything moving for a long long time"
 g "It gets lonely sometimes"
 g "But I'm used to it"
 p "..."
 g "You androids are smart. Smarter than me, at least."
 g "So you should know how to transfer these files to my computer right?"
 p "Yes"
 
 image screen start = "computer startscreen.png"
 scene screen start
 hide waifu
 hide girl
 
 g "Get to it, then."
 g "..."
 g "..."
 g "I wonder how I lived through the bombs."
 g "Is it my curse to watch the world die around me as I waste away?"
 g "without the courage to just end it all?"
 
label filetransfer:
 menu:
  "Perform scp transfer":
   jump failcomputer3
  "Find Hard drive name":
   jump successcomputer3
    
label failcomputer3:
 image computerfail3 = "failedfiles.png"
 scene computerfail3
 g "...I assume it didn't work."
 p "Yes"
 g "It's okay, I'm used to things not working."
 p "(I really should be more careful, lest I am unable to make it back)"
 jump filetransfer
 
label successcomputer3:
 image computersuccess3 = "nameofsystem.png"
 scene successcomputer3
 g "It's succeeding?"
 p "Yes."
 jump mount

label mount:
 menu:
  "Mount drive":
   jump successcomputer4
  "Copy files":
   jump failcomputer4
   
label failcomputer4:
 image computerfail4 = "failedfiles.png"
 scene computerfail4
 g "No! Is it not working?"
 p "I just did something in the wrong order."
 p "(I better be more careful...)"
 jump mount
 
label successcomputer4:
 image computersuccess4 = "mounted.png"
 scene computersuccess4
 g "The hard drive, we can see it now? Am I finally saved?"
 p "Yes."
 image insidefolder = "insidefolder.png"
 scene insidefolder
 g "What? It's empty? How is it possible?"
 p "Not exactly."
 
label recovery:
 menu: 
  "Initiate file recovery":
   jump successcomputer2
  "Search for hidden files":
   jump failcomputer2
   
label failcomputer2:
 
 image computerfail2 = "filesfailed.png"
 scene computerfail2
 
 p "No, this must be a mistake."
 g "It better be."
 jump recovery
 
label successcomputer2:
 image computersuccess2 ="filesappeared.png"
 scene computersuccess2
 
 g "..Thank you. I still have a chance."
 p "...Why don't you leave Earth, if you think this place offers nothing?"
 g "You think I don't want to? Interplanetary travel isn't cheap, and I can never afford it even if I live to 80. You actually think anyone would voluntarily stay in this godforsaken land?"
 p "..."
 g "This land is dead. It's inhabitants are withering, abandoned. The population dwindles every year. Soon, there will be nothing left."
 g "We will all return to dust as Earth dies."
 g "..."
 g "What now?"
 p "I need to decrypt the files."
 g "So it will work?"
 p "Almost garuanteed."
 g "...You know how torturous it is, knowing the key to your happiness is locked behind something you cannot access?"
 g "Everyday the hard drive is just there, taunting me with memories of a happier time."
 g "...I would have gone crazy if I never learnt not to care, to surpress my desires and emotions."

label decryption:
 scene screen start
 
 menu: 
  "Decrypt base64":
   jump failcomputer
  "Decrypt MD5":
   jump successcomputer
  "Decrypt SHA-384":
   jump failcomputer
   
label failcomputer: 
 image failedcom = "computerfailed.png"
 scene failedcom
 
 g "Is it all lost?"
 p "I must have guessed wrong."
 g "I want to feel truly happy again instead of wallowing in a pit of apathy. I was only ever happy in old Earth."
 p "..."
 g "Please succeed."
 jump retrycomputer
 
label retrycomputer:
 p "(That took some energy, I better not fail again)"
 jump decryption

label successcomputer:
 image successcom = "computersuccess.png"
 scene successcom

 p "It's almost done."
 g "...I don't know what to feel."
 p "Happy? You get to experience your best memories again."
 g "It rings so hollow. Masquerading and pretending the world we live in doesn't exist, escaping into past happier times."
 g "...I always wanted to ask an android, do you ever feel like shutting down...forever?"
 p "No, androids do not have such a function."
 g "...Must be great being an android."
 p "Only humans 'shut down' in such great quantities because of their feelings. Other creatures, they usually want to survive. Why?"
 g "Humans are the only creatures who question life. Ask whether it's worth living."
 menu:
  "Copy files":
   jump successcomputer5
   
label successcomputer5: 
 #stop music "filetransfer.mp3"
 #start music "done.mp3"
 image computersuccess5 = "copied.png"
 scene computersuccess5
 image girl_relieved = "relievedgirl.gif"
 show girl_relieved at right
 show waifu at left 

 p "It's done."
 g "...Thank you.Thank you kindly."
 g "Ah, my old photos."
 g "They are all I have now. My only way to escape the chasm of apathy I had fallen in."
 g "Have you ever tried so hard to feel something? Feel something real?"
 p "...No"
 g "...Of course, an android will not know."
 g "Do you even know what Earth was like?"
 p "No"
 g "It wasn't perfect, but it was real. It was warm. It was alive."
 g "Nothing like what the world is now."
 p "..."
 g "..."
 g "So...the directions to Midtown Tower, am I right?"
 p "Yes."
 g "Go straight north until you see the giant fountain, you can't miss it. There, turn right. You should reach the building within two days."
 p "Thank you"
 p "...Those photos...will they make your life worth living?"
 g "No. No for long."
 p "What will?"
 g "Something real to care about. Like you, you care about your owner right?"
 p "But..."
 menu:
  "It might not be real":
   jump real5
  "Nothing.":
   jump nothing5
   
label real5:
 hide girl_relieved 
 show girl_amused at right
 show waifu at left
 
 g "Hah, never knew an android could think of that."
 g "Does it matter if the feelings are real or not?"
 p "..."
 g "At least you do feel care, feel for something real and tangible."
 g "I wish I could do that"
 jump chapter5ending
 
label nothing5:
 hide girl_relieved
 show girl at right
 show waifu at left
 
 g "...Hold on to that care."
 g "Don't let it slip away like I did."
 g "It makes all the difference."
 jump chapter5ending
 
label chapter5ending:
 hide girl_relieved
 hide waifu
 #stop music "end.mp3"
 #start music "chap5end.mp3"
 scene wasteland
 
 p "(I would wish her all the best, but I feel that wish will be wasted)"
                 
    
return