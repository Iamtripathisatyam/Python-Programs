from plyer import notification
with open('trial.txt') as f:
    a = f.readlines()
dict = {}
sict = {}
notification.notify(title="Offline E-book Dictionary Made by : Satyam Tripathi & Company", message="Using Python & Python Plyer",
                      app_icon="C:/Users"
                               "/Dell/Downloads/body.ico", timeout=5)
if __name__ == '__main__':
 while 1:
  for i in a:
    parsed = i.split(":")
    dict[parsed[0]] = parsed[1]
    sict[parsed[0]]=parsed[2].capitalize()


  c=input("\n Please Enter any word : ")
  b=c.capitalize()
  if b not in dict.keys():
      notification.notify(title="Error !!", message=f"\'{c}\' is not found in the dictionary !!",
                          app_icon="C:/Users"
                                   "/Dell/Downloads/err.ico", timeout=10)
  else:

      notification.notify(title=f" {b.upper()} : ", message=f"\nMeaning of {b} : {dict[b]}\n\nExample-{sict[b]}",
                          app_icon="C:/Users"
                                   "/Dell/Downloads/noerr.ico", timeout=10)


  sat=input("Do you Want to Search more words : Press[y/n]")
  sat.lower()
  if sat=="n":
    exit()
  elif sat=="y":
      continue
      
      
      
      
Abnormal:Not normal:The child displayed abnormal behavior in class by suddenly shouting out loudly.
Elucidate:To make clear:The scholarly speaker elucidated on the topic in great details.
Pacify:To calm:The wise man tried to pacify both the warring parties, but they were hell bent on going ahead with their fight.
Query:Question:The teacher could not think of a suitable reply to Neha's query.
Queue:Line:As soon as the teacher announced that she would be giving a chocolate to each of the boys, they quickly queued up.
Quiet:Making no noise:I told them to be quiet and go to sleep.
Rapid:Having great speed:He walked at a rapid pace along the street when it became dark.
Stationary:Unchanging:A stationary object, if propelled with a force, will move in proportion to the force you apply on it.
Uproarious:Noisy:entered the market to find out that it was completely chaotic and uproarious.
Urgent:Required immediately:This task requires your urgent attention as tomorrow is the last day to finish it.
Abject:Miserable:The abject condition in which Gulzari Lal lived in his last days was testimony to the fact that despite being the P.M. twice, he had hardly made any money for himself in his political career.
Abrade:Wear away:The long drawn-out war abraded the army's morale and ultimately led to its dismal surrender.
Formidable:Overwhelming, alarming, dreadful:Considering his formidable fan following in the city, it is no surprise that he has won with a huge margin of 3 lakh votes.
Knotty:Puzzling:Whether the hen came first or the egg has been one of the knottiest problems facing our scientists for long.
Nullify:Make void:The Sukhigeeli Party, by going back on its election-time promises, has nullified the entire goodwill and support it enjoyed at the time of coming to power.
Oust:To eject:He was oust from his community due to his different ideological thought process.
Palatial:Like a palace:The palatial Maharaja’s Haveli, comprising 300 rooms, 5 banquet halls and 3 swimming pools, was auctioned last week.
Radical:Extreme:Osho Rajneesh’s radical ideas, which were in direct opposition to those of prevailing and popular religions, obviously gave rise to lots of criticism.
Rampage:Violence:The frenzied mob, enraged by the police excesses, went on a rampage and set ablaze several government buildings.
Wry:Twisted:His wry face was testimony to his contemptuous feelings towards the fellow.
Zombie:A frightening person:He was sleep walking and looked like a zombie.
Callous:Insensitive:Such a callous government, which is not moved even by the plight of a pregnant woman being slit open in her stomach, ought to go instantly.
Cantankerous:Quarrelsome, irascible:A candidate having even a shade of cantankerous nature in her is a strict no-no for a receptionist's job.
Fastidious:Careful in all details, meticulous, very difficult to please:A fastidious film-maker as he was, Ronu Sen sometimes did not okay a shot despite 50 re-takes.
Forsake:To abandon:Though Piyush was getting a private-sector job worth Rs. 50000/- a month, he was not ready to forsake the security of his government job.
Gauche:Tactless:Narendra Modi's gauche and childish handling of the Gujarat riots has deservedly earned him a dubious distinction.
Haughty:Proud:The late actor Raj Kumar was well-known for the haughty way in which he used to treat other co-stars on and off-screen.
Inextricable:Cannot be taken out, irredeemable:Had the government intervened earlier, the situation could have been salvaged, but right now it seems we are caught in an inextricable diplomatic crisis.
Macabre:Horrible:The scene of mass killings in the village presented a macabre sight to the visitors, enough to scare even the brave-hearted.
Ostensible:Apparent:The ostensible reason given for the boss' absence from the meeting was his ill health, while everybody knew deep down the heart that the boss had absented himself because of his differences with the management.
Overt:In the open:In an overt move against the CEO, the GM put the blame of failure on his head.
Quip:Witty remark:When confronted with this question "Do you like e-mail?", he quipped, " No, I like female".
Rapport:Harmony:Kavi Rakesh was appointed to the post of Chairman, Sahitya Academy because he enjoyed a close rapport with the members of the selection panel.
Recalcitrant:Obstinately defiant of authority, difficult to manage:His recalcitrant refusal to step down from the Chief Ministership of the state, despite all-round demand for his dismissal, only indicates his disregard for public sentiments.
Stealth:Secret:The thief moved about stealthily around the house, so as to get an idea about a safe entry and exit route.
Urbane:Courteous:He was a very polished, soft spoken and urbane speaker.
Wretchedness:Extreme misery or unhappiness:They lived in a wretched state and had to work hard to meet their daily requirements.
Wrought:Worked into shape by artistry or effort, fashioned, formed:The heated iron is wrought into different beautiful shapes by the workmen who must know the appropriate temperature needed for an article to get its proper shape.
Zany:Silly, crazy:The zany expression on her face belied her intellectual core.
Zenith:Peak:Today’s newcomers in the film industry are charging prices, which Amitabh Bachchan could never think of, even at the zenith of his career in the late 1970s and early 1980s.
    
     
     
