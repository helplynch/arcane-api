import requests,colorama,sys,certifi,hashlib,binascii,time
from colorama import*
just_fix_windows_console()
def encode(input_string):encoded_hex=binascii.hexlify(input_string.encode()).decode();return encoded_hex
def decode(hex_string):decoded_string=binascii.unhexlify(hex_string).decode();return decoded_string
def content(url):
	try:
		response=requests.get(url)
		if response.status_code==200:return response.text
		else:print(f"Failed to retrieve content. Status code: {response.status_code}");return
	except requests.RequestException as e:print(f"An error occurred: {e}");return
keysystemkey=input(Fore.GREEN+'  Enter your spec.lol software key: '+Fore.WHITE)
print(Fore.BLUE+'  Checking key...')
getcontent=content(decode('68747470733a2f2f737065636c6f6c2e303030776562686f73746170702e636f6d2f636865636b2e7068703f6b65793d')+str(keysystemkey))
if getcontent=='valid':keyactive='yes';print(Fore.GREEN+'  Your key is correct!')
else:keyactive='no'
if keyactive=='no':print(Fore.RED+'  Your key is invalid. Closing in 2 seconds.');time.sleep(2);sys.exit()
textsend=input(Fore.CYAN+'  Enter your Auth Token: '+Fore.WHITE)
amt=input(Fore.CYAN+'  How many trophies do you want added?: '+Fore.WHITE)
url='https://us-central1-justbuild-cdb86.cloudfunctions.net/v459_player/updateProgressAndStats'
data={'skinUsed':'lol.1v1.playerskins.pack.244','matchSummary':'{"ModeName":"1v1_Clash","MatchResult":"win","KillCount":'+str(amt)+',"DeathCount":0,"IsComp":true,"RankType":0,"Placement":1,"PlayerCount":2,"GameModeMaxPlayers":2,"LeftMidGame":false,"ShouldGetTrophiesForKills":true,"TeamKills":0,"IsAccountRoadActive":true,"DidRankUp":false,"ShouldUpdateBattlePass":true}'}
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0','Accept':'*/*','Accept-Language':'en-US,en;q=0.5','Content-Type':'application/x-www-form-urlencoded','firebase-config-ids':'{"VersionID":"default","BattlePassID":"Nov2023_EconomyTest_Control","DailyRewardsID":"default","GameModesID":"default","RankXPGainPerGameModeId":"default","StoreSettingsID":"Nov2023_EconomyTest_Control","SubscriptionsId":"default","ProductsID":"default","GeneralConfigID":"web","AdsSettingsID":"default","ChallengesID":"default","TrophyRoadID":"default","RankRoadID":"default","LootBoxesId":"default","DailySpinsId":"Nov2023_EconomyTest_Control","GameplaySettingsID":"default","FTUEConfigID":"default","LimitedLockerSpinID":"default","XPBankID":"default","LeaderboardsID":"default","EquipmentID":"default","LootBoxesGachaId":"default","ProgressionEventsID":"Nov2023_EconomyTest_Control"}','auth-token':str(textsend)}
if keyactive=='yes':
	x=requests.get(url,params=data,headers=head)
	if x.status_code==200:print('  Added '+str(amt)+' trophies!')
	else:print('  Error');print('  Code: '+str(x.status_code)+' | Response: '+x.text)
else:print(Fore.RED+'  Couldnt add trophies, your key was incorrect.'+Fore.WHITE)
