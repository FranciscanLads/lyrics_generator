from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

links = [
"https://www.azlyrics.com/lyrics/twentyonepilots/implicitdemandforproof.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/fallaway.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/thepantaloon.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/addictwithapen.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/friendplease.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/marchtothesea.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/johnnyboy.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/ohmsbeliever.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/aircatcher.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/trapdoor.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/acaratorchadeath.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/taxicab.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/beforeyoustartyourday.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/isleofflightlessbirds.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/gunsforhands.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/holdingontoyou.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/odetosleep.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/slowtown.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/carradio.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/forest.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/glowingeyes.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/kitchensink.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/anathema.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/lovely.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/ruby.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/trees.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/beconcerned.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/clear.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/odetosleep.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/holdingontoyou.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/migraine.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/houseofgold.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/carradio.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/semiautomatic.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/screen.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/therunandgo.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/fakeyouout.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/gunsforhands.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/trees.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/truce.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/heavydirtysoul.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/stressedout.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/ride.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/fairlylocal.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/tearinmyheart.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/laneboy.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/thejudge.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/doubt.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/polarize.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/wedontbelievewhatsontv.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/messageman.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/hometown.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/nottoday.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/goner.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/jumpsuit.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/levitate.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/morph.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/myblood.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/chlorine.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/smithereens.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/neongravestones.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/thehype.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/nicoandtheniners.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/cutmylip.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/bandito.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/petcheetah.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/legend.html",

"https://www.azlyrics.com/lyrics/twentyonepilots/leavethecity.html"
]


driver = None
try:
	driver = webdriver.Chrome()
	action = ActionChains(driver)
	for link in links:
		driver.get(link)
		driver.implicitly_wait(2)
		content = driver.find_element_by_css_selector('body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > div:nth-child(8)').text
		with open("top_lyrics"+".txt", "a", encoding="utf8") as f:
			f.write("\n"+content)
finally:
	if driver is not None:
		driver.close




	