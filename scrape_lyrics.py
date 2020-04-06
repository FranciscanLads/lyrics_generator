from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

links = [
"https://www.azlyrics.com/lyrics/coldplay/biggerstronger.html",

"https://www.azlyrics.com/lyrics/coldplay/dontpanic.html",

"https://www.azlyrics.com/lyrics/coldplay/seeyousoon.html",

"https://www.azlyrics.com/lyrics/coldplay/highspeed295959.html",

"https://www.azlyrics.com/lyrics/coldplay/sucharush.html",

"https://www.azlyrics.com/lyrics/coldplay/dontpanic.html",

"https://www.azlyrics.com/lyrics/coldplay/shiver.html",

"https://www.azlyrics.com/lyrics/coldplay/spies.html",

"https://www.azlyrics.com/lyrics/coldplay/sparks.html",

"https://www.azlyrics.com/lyrics/coldplay/yellow.html",

"https://www.azlyrics.com/lyrics/coldplay/trouble.html",

"https://www.azlyrics.com/lyrics/coldplay/parachutes.html",

"https://www.azlyrics.com/lyrics/coldplay/highspeed.html",

"https://www.azlyrics.com/lyrics/coldplay/weneverchange.html",

"https://www.azlyrics.com/lyrics/coldplay/everythingsnotlost.html",

"https://www.azlyrics.com/lyrics/coldplay/lifeisforliving.html",

"https://www.azlyrics.com/lyrics/coldplay/politik.html",

"https://www.azlyrics.com/lyrics/coldplay/inmyplace.html",

"https://www.azlyrics.com/lyrics/coldplay/godputasmileuponyourface.html",

"https://www.azlyrics.com/lyrics/coldplay/thescientist.html",

"https://www.azlyrics.com/lyrics/coldplay/clocks.html",

"https://www.azlyrics.com/lyrics/coldplay/daylight.html",

"https://www.azlyrics.com/lyrics/coldplay/greeneyes.html",

"https://www.azlyrics.com/lyrics/coldplay/warningsign.html",

"https://www.azlyrics.com/lyrics/coldplay/awhisper.html",

"https://www.azlyrics.com/lyrics/coldplay/arushofbloodtothehead.html",

"https://www.azlyrics.com/lyrics/coldplay/amsterdam.html",

"https://www.azlyrics.com/lyrics/coldplay/squareone.html",

"https://www.azlyrics.com/lyrics/coldplay/whatif.html",

"https://www.azlyrics.com/lyrics/coldplay/whiteshadows.html",

"https://www.azlyrics.com/lyrics/coldplay/fixyou.html",

"https://www.azlyrics.com/lyrics/coldplay/talk.html",

"https://www.azlyrics.com/lyrics/coldplay/xy.html",

"https://www.azlyrics.com/lyrics/coldplay/speedofsound.html",

"https://www.azlyrics.com/lyrics/coldplay/amessage.html",

"https://www.azlyrics.com/lyrics/coldplay/low.html",

"https://www.azlyrics.com/lyrics/coldplay/thehardestpart.html",

"https://www.azlyrics.com/lyrics/coldplay/swallowedinthesea.html",

"https://www.azlyrics.com/lyrics/coldplay/twistedlogic.html",

"https://www.azlyrics.com/lyrics/coldplay/tilkingdomcome.html",

"https://www.azlyrics.com/lyrics/coldplay/howyouseetheworld.html",

"https://www.azlyrics.com/lyrics/coldplay/cemeteriesoflondon.html",

"https://www.azlyrics.com/lyrics/coldplay/lost.html",

"https://www.azlyrics.com/lyrics/coldplay/42.html",

"https://www.azlyrics.com/lyrics/coldplay/loversinjapanreignoflove.html",

"https://www.azlyrics.com/lyrics/coldplay/yes.html",

"https://www.azlyrics.com/lyrics/coldplay/chinesesleepchant.html",

"https://www.azlyrics.com/lyrics/coldplay/vivalavida.html",

"https://www.azlyrics.com/lyrics/coldplay/violethill.html",

"https://www.azlyrics.com/lyrics/coldplay/strawberryswing.html",

"https://www.azlyrics.com/lyrics/coldplay/deathandallhisfriends.html",

"https://www.azlyrics.com/lyrics/coldplay/theescapist.html",

"https://www.azlyrics.com/lyrics/coldplay/lifeintechnicolorii.html",

"https://www.azlyrics.com/lyrics/coldplay/glassofwater.html",

"https://www.azlyrics.com/lyrics/coldplay/rainyday.html",

"https://www.azlyrics.com/lyrics/coldplay/prospektsmarchpoppyfields.html",

"https://www.azlyrics.com/lyrics/coldplay/nowmyfeetwonttouchtheground.html",

"https://www.azlyrics.com/lyrics/coldplay/hurtslikeheaven.html",

"https://www.azlyrics.com/lyrics/coldplay/paradise.html",

"https://www.azlyrics.com/lyrics/coldplay/charliebrown.html",

"https://www.azlyrics.com/lyrics/coldplay/usagainsttheworld.html",

"https://www.azlyrics.com/lyrics/coldplay/everyteardropisawaterfall.html",

"https://www.azlyrics.com/lyrics/coldplay/majorminus.html",

"https://www.azlyrics.com/lyrics/coldplay/ufo.html",

"https://www.azlyrics.com/lyrics/coldplay/princessofchina.html",

"https://www.azlyrics.com/lyrics/coldplay/upinflames.html",

"https://www.azlyrics.com/lyrics/coldplay/dontletitbreakyourheart.html",

"https://www.azlyrics.com/lyrics/coldplay/upwiththebirds.html",

"https://www.azlyrics.com/lyrics/coldplay/alwaysinmyhead.html",

"https://www.azlyrics.com/lyrics/coldplay/magic.html",

"https://www.azlyrics.com/lyrics/coldplay/ink.html",

"https://www.azlyrics.com/lyrics/coldplay/truelove.html",

"https://www.azlyrics.com/lyrics/coldplay/midnight.html",

"https://www.azlyrics.com/lyrics/coldplay/anothersarms.html",

"https://www.azlyrics.com/lyrics/coldplay/oceans.html",

"https://www.azlyrics.com/lyrics/coldplay/askyfullofstars.html",

"https://www.azlyrics.com/lyrics/coldplay/o.html",

"https://www.azlyrics.com/lyrics/coldplay/allyourfriends.html",

"https://www.azlyrics.com/lyrics/coldplay/ghoststory.html",

"https://www.azlyrics.com/lyrics/coldplay/aheadfullofdreams.html",

"https://www.azlyrics.com/lyrics/coldplay/birds.html",

"https://www.azlyrics.com/lyrics/coldplay/everglow.html",

"https://www.azlyrics.com/lyrics/coldplay/adventureofalifetime.html",

"https://www.azlyrics.com/lyrics/coldplay/kaleidoscope.html",

"https://www.azlyrics.com/lyrics/coldplay/armyofone.html",

"https://www.azlyrics.com/lyrics/coldplay/xmarksthespot.html",

"https://www.azlyrics.com/lyrics/coldplay/amazingday.html",

"https://www.azlyrics.com/lyrics/coldplay/upup.html",

"https://www.azlyrics.com/lyrics/coldplay/allicanthinkaboutisyou.html",

"https://www.azlyrics.com/lyrics/coldplay/aliens.html",

"https://www.azlyrics.com/lyrics/coldplay/somethingjustlikethistokyoremix.html",

"https://www.azlyrics.com/lyrics/coldplay/hypnotised.html",

"https://www.azlyrics.com/lyrics/coldplay/church.html",

"https://www.azlyrics.com/lyrics/coldplay/troubleintown.html",

"https://www.azlyrics.com/lyrics/coldplay/broken.html",

"https://www.azlyrics.com/lyrics/coldplay/daddy.html",

"https://www.azlyrics.com/lyrics/coldplay/wotwpotp.html",

"https://www.azlyrics.com/lyrics/coldplay/arabesque.html",

"https://www.azlyrics.com/lyrics/coldplay/whenineedafriend.html",

"https://www.azlyrics.com/lyrics/coldplay/guns.html",

"https://www.azlyrics.com/lyrics/coldplay/orphans.html",

"https://www.azlyrics.com/lyrics/coldplay/eko.html",

"https://www.azlyrics.com/lyrics/coldplay/crycrycry.html",

"https://www.azlyrics.com/lyrics/coldplay/oldfriends.html",

"https://www.azlyrics.com/lyrics/coldplay/championoftheworld.html",

"https://www.azlyrics.com/lyrics/coldplay/everydaylife.html",

"https://www.azlyrics.com/lyrics/coldplay/136.html",

"https://www.azlyrics.com/lyrics/coldplay/aghost.html",

"https://www.azlyrics.com/lyrics/coldplay/aspellarebelyell.html",

"https://www.azlyrics.com/lyrics/coldplay/amorargentina.html",

"https://www.azlyrics.com/lyrics/coldplay/animals.html",

"https://www.azlyrics.com/lyrics/coldplay/brotherssisters.html",

"https://www.azlyrics.com/lyrics/coldplay/bucketforacrown.html",

"https://www.azlyrics.com/lyrics/coldplay/carefulwhereyoustand.html",

"https://www.azlyrics.com/lyrics/coldplay/christmaslights.html",

"https://www.azlyrics.com/lyrics/coldplay/christmaswiththekangaroos.html",

"https://www.azlyrics.com/lyrics/coldplay/crestofwaves.html",

"https://www.azlyrics.com/lyrics/coldplay/deathwillneverconquer.html",

"https://www.azlyrics.com/lyrics/coldplay/donquixote.html",

"https://www.azlyrics.com/lyrics/coldplay/easytoplease.html",

"https://www.azlyrics.com/lyrics/coldplay/everglowsingleversion.html",

"https://www.azlyrics.com/lyrics/coldplay/foryou.html",

"https://www.azlyrics.com/lyrics/coldplay/gonebutnotfcotton.html",

"https://www.azlyrics.com/lyrics/coldplay/goodbyeandgoodnight.html",

"https://www.azlyrics.com/lyrics/coldplay/gravity.html",

"https://www.azlyrics.com/lyrics/coldplay/harmless.html",

"https://www.azlyrics.com/lyrics/coldplay/helpisroundthecorner.html",

"https://www.azlyrics.com/lyrics/coldplay/houston.html",

"https://www.azlyrics.com/lyrics/coldplay/howyouseetheworldno2.html",

"https://www.azlyrics.com/lyrics/coldplay/ibloomblaum.html",

"https://www.azlyrics.com/lyrics/coldplay/iranaway.html",

"https://www.azlyrics.com/lyrics/coldplay/idiot.html",

"https://www.azlyrics.com/lyrics/coldplay/laddertothesun.html",

"https://www.azlyrics.com/lyrics/coldplay/moses.html",

"https://www.azlyrics.com/lyrics/coldplay/movingtomars.html",

"https://www.azlyrics.com/lyrics/coldplay/murder.html",

"https://www.azlyrics.com/lyrics/coldplay/nomorekeepingmyfeetontheground.html",

"https://www.azlyrics.com/lyrics/coldplay/odetodeodorant.html",

"https://www.azlyrics.com/lyrics/coldplay/oneilove.html",

"https://www.azlyrics.com/lyrics/coldplay/onlysuperstition.html",

"https://www.azlyrics.com/lyrics/coldplay/pourme.html",

"https://www.azlyrics.com/lyrics/coldplay/proof.html",

"https://www.azlyrics.com/lyrics/coldplay/sleepingsun.html",

"https://www.azlyrics.com/lyrics/coldplay/thegoldrush.html",

"https://www.azlyrics.com/lyrics/coldplay/themanwhoswears.html",

"https://www.azlyrics.com/lyrics/coldplay/theworldturnedupsidedown.html",

"https://www.azlyrics.com/lyrics/coldplay/thingsidontunderstand.html",

"https://www.azlyrics.com/lyrics/coldplay/yourlovemeanseverythingpart2.html"
]




driver = None
try:
	driver = webdriver.Chrome()
	action = ActionChains(driver)
	for link in links:
		driver.get(link)
		driver.implicitly_wait(2)
		content = driver.find_element_by_css_selector('body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > div:nth-child(8)').text
		with open("coldplay_lyrics"+".txt", "a", encoding="utf8") as f:
			f.write(content)
finally:
	if driver is not None:
		driver.close




	