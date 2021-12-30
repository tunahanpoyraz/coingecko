import requests,time,csv
header=["id","symbol","asset_platform_id","contracts"]
class allData:
  def __init__(self, coins):
    self.coins = coins
  def coin(abc):
    data =list()
    for i in abc.coins:
        data.append(i["id"])
    print(len(data))
    return data
  def contractAddresses(self,need):
      j=0    
      data2=list()
      while j<len(need):
        abc = requests.get(url = "https://api.coingecko.com/api/v3/coins/"+need[j]).json()
        time.sleep(1.2)
        list(abc["id"])       
        print(j)
        a=abc["asset_platform_id"]
        try:
          if a==None:
            a=="None"
        except Exception as e:
          print(e)
          j+=1
        try:
          if abc["id"]=="":
            abc["id"]== "None"
        except Exception as e:
          print(e)
          j+=1
        try:
          if abc["symbol"]=="":
            abc["symbol"]== "None"
        except Exception as e:
          print(e)
          j+=1
        try:
          if abc["platforms"][a]=="":
            abc["platforms"][a]=="None"
        except Exception as e:
          print(e)
          j+=1
        try:
            data2.append([abc["id"],abc["symbol"],a,abc["platforms"][a]])
            j+=1
        except Exception as e:
            print(e)
            data2.append("None") 
            j+=1   
        with open("data.csv", 'w') as csvfile: 
                    csvwriter = csv.writer(csvfile)         
                    csvwriter.writerow(header) 
                    csvwriter.writerows(data2)
p1 = allData(requests.get(url = "https://api.coingecko.com/api/v3/coins/list").json())
p1.contractAddresses(p1.coin())