import requests,time,csv
header=["id","symbol","platform","contracts"]

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
        time.sleep(1.25)



        try:
            print(len(need)-j)

            data2.append([abc["id"],abc["symbol"],abc["platforms"]])
        except Exception as e:
            print(e,"No data")
            try:
                data2.append([abc["id"],None,None])
            except:
                print("no id")
                pass


            pass
        j+=1
        with open("data.csv", 'w') as csvfile: 
                    csvwriter = csv.writer(csvfile)         
                    csvwriter.writerow(header) 
                    csvwriter.writerows(data2)
p1 = allData(requests.get(url = "https://api.coingecko.com/api/v3/coins/list").json())
p1.contractAddresses(p1.coin())