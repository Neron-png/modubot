import json
import time


async def pr(message, prefix):
    
    #################################
    ranking = open('commands/ranking.txt', 'r+')
    ranking_data = ranking.readlines()
    
    
            
        
    #ranking.close()
    
    a = 0
    for i in ranking_data:
        ranking_data[a] = i.replace("\n", "")
        a += 1
    # returns list in ranking_data ['5 draziotis', '4 tsitsas', '3 vrakas', '2 thrasivoulos', '1 katsanos', '0 tiakas']
    
    if not (message.content == prefix + "pr" or message.content == prefix + "power-ranking"):
    
        # !pr vrakas +5
        victim = message.content.split(" ")[1] # vrakas
        change = message.content.split(" ")[2] # +5
        
        change = int(change) * 1
        
        for i in ranking_data:
            if victim in i:
                victim_index = ranking_data.index(i)
        
        #victim_index = ranking_data.index(victim)
        ranking_data[victim_index] = str(int(ranking_data[victim_index].split(' ')[0]) + change) + " " + ranking_data[victim_index].split(' ')[1]
        
        print(ranking_data)
        
        for i in range(0, 6):
            for j in range(5, i, -1):
                if int(ranking_data[j].split(' ')[0]) < int(ranking_data[j-1].split(' ')[0]):
                    temp = ranking_data[j]
                    ranking_data[j] = ranking_data[j-1]
                    ranking_data[j-1] = temp
          
          
    ranking_string = ranking_data[0]
    for i in range(1, 6):
        ranking_string = ranking_string + "\n" + ranking_data[i]
    
    

    
    await message.channel.send('**Power Ranking:**\n```\n' + ranking_string.capitalize() + '```')
    
   # ranking = open('ranking.txt', 'w')
    ranking.seek(0)
    ranking.truncate()
    ranking.write(ranking_string)
    ranking.close()
    
    