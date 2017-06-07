-- phpMyAdmin SQL Dump
-- version 3.5.6
-- http://www.phpmyadmin.net
--
-- Host: mysql-limdialect.science.ru.nl
-- Generation Time: Jun 07, 2017 at 07:51 PM
-- Server version: 5.5.55-0ubuntu0.14.04.1-log
-- PHP Version: 5.3.10-1ubuntu3.26

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `limdialect`
--

-- --------------------------------------------------------

--
-- Table structure for table `sentences_test`
--

CREATE TABLE IF NOT EXISTS `sentences_test` (
  `sentenceid` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(100) NOT NULL,
  `sentencedutch` varchar(200) NOT NULL,
  `sentenceenglish` varchar(200) NOT NULL,
  `sentencemaas` varchar(200) NOT NULL,
  `sentenceeijsden` varchar(200) NOT NULL,
  `nrofrecordings` int(11) NOT NULL,
  PRIMARY KEY (`sentenceid`),
  UNIQUE KEY `sentencedutch_UNIQUE` (`sentencedutch`),
  UNIQUE KEY `sentenceenglish_UNIQUE` (`sentenceenglish`),
  UNIQUE KEY `sentencemaas_UNIQUE` (`sentencemaas`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=71 ;

--
-- Dumping data for table `sentences_test`
--

INSERT INTO `sentences_test` (`sentenceid`, `category`, `sentencedutch`, `sentenceenglish`, `sentencemaas`, `sentenceeijsden`, `nrofrecordings`) VALUES
(1, 'handig', 'Maandag, Dinsdag, Woensdag, Donderdag, Vrijdag, Zaterdag, Zondag', 'Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday', 'Maondag, Dinsdag, Goonsdag, Donderdag, Vriedag, Zaoterdag, Zoondag', 'Maondig, Daènsjdig, Goonsjtig, Donderdig, Vriedig, Zaoterdig, Zoeëngdig', 0),
(2, 'getallen', 'een, twee, drie, vier, vijf, zes, zeven, acht, negen, tien, elf, twaalf, dertien, veertien, vijftien, twintig, eenentwintig, tweeentwintig, dertig, veertig, vijftig, honderd, duizend, miljoen', 'one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, twenty, twenty-one, twenty-two, thirty, fourty, fifty, hundred, one-thousand, one-million', 'ein, twie, drei, veer, vijf, zès, zeve, ach, nege, tien, èlf, twaalf, dertien, veertien, vieftien, twinteg, einentwinteg, twieëntwinteg, derteg, veerteg, viefteg, hoonderd, doezend, miljoen', 'Èèn, twie, drèij, veer, vijf, zis, zieëve, aach, nuëge, tien, ellef,  twellef, dartien, virtien, vieftien, zesjtien, Twiengtig, èènentwiengtig, twieentwiengtig, dartig, firtig, fieftig, Hoengderd, doe', 0),
(3, 'getallen', 'elfde van de elfde', 'The eleventh of the eleventh', 'èlfde vaan d’n èlfde', 'Ellefde van de ellefde', 0),
(4, 'praktische zaken', 'Waar is hier ergens een bank of een geldautomaat?', 'Where can I find a bank or ATM?', 'Boe is hei örges ’n baank of ‘ne geldotomaat?', 'Oe is hie uërges een baank of ene gèldotomaat', 0),
(5, 'praktische zaken', 'Wat is het wachtwoord om internettoegang te krijgen?', 'What is the password to get internet access?', 'Wat is ’t wachwoord um internèttouwgaank te kriege?', 'Wat is het wachwoerd um internettowgaank te kriege?', 0),
(6, 'praktische zaken', 'Weet iemand ergens een internetcafé?', 'Does anyone know where I can find an internet cafe?', 'Wèt iemes örges ’n internètcafé?', 'Wir èène uërges e internetcafé', 0),
(7, 'praktische zaken', 'Hoeveel foto’s kan ik met deze geheugenkaart maken?', 'How many pictures can I take with this memory card?', 'Wieväöl foto’s kin iech mèt dees geheugekaart make?', 'Wievaöl foto’s kin iech mit dies gehuëgekaoërt maoëke', 0),
(8, 'praktische zaken', 'Waar kan ik rustig een goede brief schrijven?', 'Where can I write a complicated letter in a quiet environment?', 'Boe kin iech rösteg ‘ne gooje breef sjrieve?', 'Oe kin iech rusjtig ene gooje breef sjrieve?', 0),
(9, 'weer', 'Gaat het vandaag regenen?', 'Is it going to rain today?', 'Geit ’t vendaog regene?', 'Gèèt ’t huij raègene?', 0),
(10, 'weer', 'Wat voor ’n weer wordt het morgen?', 'What kind of weather is expected tomorrow?', 'Wat veur e weer weurt ’t mörge?', 'Wat vuur e waer wurd ’t murrege?', 0),
(11, 'transport', 'Hoeveel kilometer heb je vandaag gefietst?/gewandeld?', 'How many kilometres did you bike/hike today?', 'Wieväöl kilometer höbste vendaog gefiets?/gewandeld?', 'Wievaöl kilometer heb ste huij gefïtst/gewaandeld?', 0),
(12, 'transport', 'Hoe ver is het naar de parkeergarage?', 'How far is the distance to the parking garage?', 'Wie wied is ’t nao de parkeergraasj?', 'Wie wied is ’t nao de parkeergraasj', 0),
(13, 'transport', 'Ik heb het leren zadel van de fiets kapot.', 'My leather saddle of the bike is broken', 'Iech höb ’t lere zadel vaan m’ne fiets kepot.', 'Iech heb de laere zaol van miene fits kapot', 0),
(14, 'transport', 'Hoe kan ik al lopend het station vinden?', 'How can I find the railway station by foot?', 'Wie kin iech al loupentere de statie vinde?', 'Wie kin iech laopenterre de sjtaoësie viengde?', 0),
(15, 'transport', 'Waar in Eijsden is het goed koffie met vlaai eten na het wandelen?', 'Where in Eijsden can one have a good cup of coffee with pie after a long walk?', 'Boe in Eijsde is ’t good koffie mèt vlaoj ete nao ’t wandele?', 'Oe ien Eèsjde kin ste good koffie mit vlaoj aète nao ’t waandele?', 0),
(16, 'ontmoetingen', 'Gefeliciteerd met uw verjaardag!', 'Congratulations on your birthday!', 'Perficia mèt eure verjaordaag!', 'Perfisiat mit eure verjaordig', 0),
(17, 'ontmoetingen', 'Waar woont Andre Rieu en Beppie Kraft?', 'Where do Andre Rieu and Beppie Kraft live?', 'Boe woent André Rieu en Beppie Kraft?', 'Oe woene André Rieu en Beppie Kraft?', 0),
(18, 'ontmoetingen', 'Goeiemorgen, Hoi, Dag, Tot ziens, Welterusten, Gezondheid', 'Good morning, Hello, Bye, See you later, Sleep well, Bless you', 'Goojemörge, Haije, Dag, Tot zeens, Welteröste, Gezoondheid', 'Gooje mörrege, Hoi, Daag, v’r zien oes, Gooje naach, Gezoengdhèèd', 0),
(19, 'Iemand versieren', 'Wat kan ik hier doen?', 'What can I do here?', 'Wat kin iech hei doen?', 'Wat kin iech hie doen?', 0),
(20, 'Iemand versieren', 'Geef me eens een zoen', 'Give me a kiss', 'Geef miech ‘ns ‘ne poen', 'Gaèf miech es ene poen', 0),
(21, 'Iemand versieren', 'Wat denk je, zijn zij verliefd aan het praten?', 'What do you think, are they talking in a romantic way?', 'Wat dinkste, zien zie verleef aon ’t praote?', 'Wat dienks diech? Zien die verleef aon ’t kalle?', 0),
(22, 'Iemand versieren', 'Je bent een schatje', 'You are so sweet', 'De bis ‘ne sjat', 'Diech bies ene sjat', 0),
(23, 'Iemand versieren', 'Wanneer zien we elkaar weer?', 'When do we see each other again?', 'Wienie zien v’r us weer?', 'Wienie zien v’r oes weer', 0),
(24, 'Iemand versieren', 'Ik weet zeker dat ik lang over je gedroomd hebt', 'I know for certain that I''ve dreamed about you', 'Iech wèt zeker tot iech lang euver d’ch gedruimp höb', 'Iech wèèt zieëker dat iech lang uëver diech gedruijmp heb', 0),
(25, 'Iemand versieren', 'Mijn mannetje, wat ben je mooi!', 'My man, what a beauty you are!', 'Mie menneke, wat biste sjoen!', 'Mie menneke, wat bies ste Sjoen', 0),
(26, 'Iemand versieren', 'Zij zien elkaar in de grote spiegel', 'They see each other in the large mirror', 'Zie zien z’ch in de groete spiegel', 'Die zien ziech ien de groete sjpiegel', 0),
(27, 'Iemand versieren', 'Je hebt een mooie jas, een mooie broek en een mooi hemd aan', 'You wear a beautiful coat, trousers and shirt.', 'De höbs ‘ne sjoene jas, ’n sjoen brook en e sjoen humme aon', 'Diech hebs ene sjoene jas, een sjoen brook en e sjoen himd aon', 0),
(28, 'hotel, winkel en cafe', 'Kan ik mijn mooie hemden hier laten stomen?', 'Can I dryclean my beautiful shirts here?', 'Kin iech mien sjoen hummes hei laote stome?', 'Kin iech mie sjoen himde hie laote sjtome', 0),
(29, 'hotel, winkel en cafe', 'Mag je hond mee naar onze kamer?', 'Are dogs allowed in our room?', 'Maag dienen hoond mèt nao us kamer?', 'Maog diene hoengd mit nao oos kaoëmer', 0),
(30, 'hotel, winkel en cafe', 'Heeft u vier grote glazen sjoes voor me?', 'Four large pints of beer, please', 'Höb g’r veer groete glazer sjoes veur m’ch?', 'Heb dier veer groete glaoëzer sjoes vuur miech', 0),
(31, 'hotel, winkel en cafe', 'Hun kinderen spelen vals bij het kaarten', 'Their children cheat at card games', 'Hun kinder speule vals bij ’t kaarte', 'Hun kiengder sjpuële vaals bie ’t kaoërte', 0),
(32, 'hotel, winkel en cafe', 'Heeft u een tasje voor mijn boodschappen? Het regent buiten', 'Do you have a bag for my groceries? It''s raining outside!', 'Höb g’r e tuutsje veur m’n kemissies? ’t Regent boete', 'Heb d’r mesjiens e tuutsje vuur m’n kemíssies? ’t raegent boete', 0),
(33, 'hotel, winkel en cafe', 'Wat ’n gedoe en toestanden in het restaurant', 'What a hassle in the restaurant', 'Wat ‘nen ambras en elend in ‘t restaurant', 'Wat e gedoons en èèlend ien ’t restaurant', 0),
(34, 'hotel, winkel en cafe', 'We gaan een vaatdoek, een stropdas, dropjes, schoenveters en andere prullaria kopen', 'We are going to buy a dishcloth, a tie, liqorice, shoelaces and other stuff', 'V’r goon ‘ne potdook, ’n krevat, krissiekes, rijstartele en aander kiksjozerije koupe', 'V’r geun ene sjoeëtelsplak,’n  kervat, bulkes, raèsjtartele en aandere pröl gaèle', 0),
(35, 'hotel, winkel en cafe', 'Waar kan mijn moeder zich de handen wassen?', 'Where can my mother wash her hands', 'Boe kin mien ma ziech de han wasse?', 'Oe kint mie ma haör han waasse?', 0),
(36, 'hotel, winkel en cafe', 'Zijn er hier mooie schoenen te koop?', 'Are there nice shoes for sale here?', 'Zien hei sjoen sjeun te koup?', 'Zien hie sjoen sjoon te kaòòp', 0),
(37, 'hotel, winkel en cafe', 'Waar denk je dat ik gele kaarsen kan krijgen?', 'Where do you think I can get yellow candles?', 'Boe dinkste tot iech geel bougies kin kriege?', 'Oe dienk ste dat iech gael kieëtse kin kriege?', 0),
(38, 'hotel, winkel en cafe', 'Ik lik me de lippen af van de dorst, ik moet wat water drinken', 'I am thirsty, I need some water', 'Iech lek m’ch de lippe aof vaan d’n doors, iech moot get water drinke', 'Ieh lekg miech de lieppe aof van d’n doeësj; iech mót get wotter drienke?', 0),
(39, 'menu', 'We lusten geen eieren, heeft u wat extra’s?', 'We don''t like eggs, do you have something special?', 'Veer löste gein eier, höb g’r get extra’s?', 'Vier aète geng èjer, heb d’r get extra’s?', 0),
(40, 'menu', 'Heeft u ook zuurkool en druiven op het menu?', 'Are sauerkraut and grapes on the menu as well?', 'Höb g’r ouch zoermoos en droeve op ’t menu?', 'Heb dier òòch zoermoos en droeve op ’t menu?', 0),
(41, 'menu', 'Heb je een leesbril om de kaart te lezen?', 'Do you have reading glasses to read the menu?', 'Höbste ‘ne leesbrèl um de kaart te leze?', 'Heb ste ene laèsbreel um de kaoeërt te laèze?', 0),
(42, 'menu', 'We hebben heerlijk gegeten, Kan ik afrekenen svp?', 'The dinner was delicious, may I have the bill, please?', 'V’r höbbe heerlek gegete. Kin iech aofrekene ezzebleef?', 'V’r hebbe heerlijk gegaète, kin iech aofrèkene estebleef?', 0),
(43, 'menu', 'Mogen wij de uitgebreide wijnkaart?', 'Can you show me the extensive wine list?', 'Mage veer de oetgebreide wienkaart?', 'Maoge vier de oetgebraèjde wienkaoërt?', 0),
(44, 'menu', 'Weet u al wat u ons kan aanbevelen?', 'What do you recommend?', 'Wèt g’r al wat g’r us kint aonrikkemendere?', 'Wit g’r al wat d’r oes kint aonraoje?', 0),
(45, 'menu', 'Ik lust een sneetje brood met donkere appelstroop', 'I like a slice of bread with dark apple syrup', 'Iech lös e snijke broed mèt duustere appelsjroep', 'Iech haw gaere e sjnaèjke broed mit duusjtere appelsjróp', 0),
(46, 'menu', 'Wij drinken ons het biertje op', ' We finish our beer', 'V’r drinke us ’t pèlske op', 'Vier drienke oes ’t beer op', 0),
(47, 'menu', 'Smakelijk eten!', 'Enjoy your meal!', 'Smakelek ete!', 'Sjmaoëkelik aète', 0),
(48, 'menu', 'Waar op het vrijthof kunnen we friet met zuurvlees eten?', ' Where can we order stew (local dish) at the Vrijthof?', 'Boe op ’t Vriethof kinne v’r friet mèt zoervleis ete?', 'Oe op ’t Vriethof kin v’r frítte mit zoervlèès aète?', 0),
(49, 'Elkaar begrijpen', 'Kunt u wat langzamer praten? ', 'Can you talk more slowly?', 'Kint g’r get lankzamer praote?', 'Kin steg et laansemer kalle?', 0),
(50, 'Elkaar begrijpen', 'Hoe moet ik dat woord begrijpen? 	', 'What is the meaning of this word?', 'Wie moot iech dat woord begriepe?', 'Wie moot iech dat woerd begriepe?', 0),
(51, 'Elkaar begrijpen', 'Hoe zeg je dat in je dialect? ', 'How do you say that in your dialect?', 'Wie zègkste dat in dien dialek?', 'Wie zegk ste dat ien dien dialek?', 0),
(52, 'Elkaar begrijpen', 'Ik zeg omdat het buiten stormt, ik blijf! 	', 'I''m staying inside! The weather is too bad outside.', 'Iech zègk umtot ’t boete störmp, iech blijf!', 'Iech zegk, umdat het boete sjtaörremt … iech blief !!', 0),
(53, 'Elkaar begrijpen', 'Wij zeggen vanwege het onweer, wij blijven!	', 'We stay inside due to the thunderstorm', 'Veer zègke vaanwege ’t oonweer, veer blieve!', 'Vier zegge umdat het oengwaert: vier blieve !!', 0),
(54, 'Uitdrukkingen', 'Ik ben trots op Maastricht/Eijsden ', 'I am proud of Maastricht/Eijsden', 'Iech bin gruuts op Mestreech', 'Iech been gruuts op Eèsjde', 0),
(55, 'Uitdrukkingen', 'Hij heeft met hem een appeltje te schillen	', 'He has to deal with him', 'Heer heet mèt häöm ’n eppelke te sjèlle', 'Haer haet mit haom nog e eppelke te sjelle', 0),
(56, 'vakantie', 'Ik ben lekker aan het luilakken in mijn vakantie', 'I am doing nothing during my holidays', 'Iech bin lekker aon ’t luilakke in mien vekantie', 'Iech been lekker aon het luijlakke ien mien vekaansie', 0),
(57, 'vakantie', 'In het café zeuren ze voortdurend aan mijn hoofd	', 'They are always nagging at me in the cafe', 'In de kaffee zeure ze constant aon m’ne kop', 'Ien de kaffee zaèke ze koensjtaand aon miene kop', 0),
(58, 'vakantie', 'Op vakantie ben ik altijd tegendraads	', 'I am always recalcitrant during my holidays', 'Op vekantie bin iech altied tegedraods', 'Op vekaansie been iech altied tieëgedraods', 0),
(59, 'vakantie', 'Ik ga lekker trappelen in het gele zwembad ', 'I am going to the swimming pool', 'Iech gaon lekker trappele in ’t geel zwumbad', 'Iech gaon lekker trappele ien ’t gaele zjwumbad', 0),
(60, 'vakantie', 'Weet je zeker dat hij zich kapot verveelt? 	', 'Are you sure he is bored?', 'Wètste zeker tot heer ziech kepot verveelt?', 'Wit ste zieëker dat ‘r ziech kapot vervaelt?', 0),
(61, 'vakantie', 'Ze gelooft dat jij eerder in het café bent dan ik', ' She believes you´ll be in the cafe earlier than me', 'Zie geluif tots diech ieder in de kaffee bis es iech', 'Het geluft dats diech ieder ien de kaffee bies daan iech', 0),
(62, 'ziek', 'Haar ogen doen pijn ', 'Her eyes hurt', 'Häör ouge doen pijn', 'Haor aowwe deun ping', 0),
(63, 'ziek', 'Hij heeft last van zijn ribben ', 'His ribs ache', 'Heer heet las vaan zien ribbe', 'E haet lasj van zien ribbe', 0),
(64, 'ziek', 'Hij heeft voortdurend kippenvel', 'He has goosebumps', 'Heer heet constant hinnevel', 'E haet altied hoondervèl', 0),
(65, 'ziek', 'Mijn zonen zijn zo ongedurig, onrustig (sjravele) ', 'My sons are so restless', 'Mien zäöns zien zoe oonrösteg', 'Ming zaöns zien zoe oengrustig', 0),
(66, 'carnaval', 'Waar kan ik de zatte harmonietjes vinden? ', 'Where can I find the carnival brassbands?', 'Boe kin iech de zate hermeniekes vinde?', 'Oe kin iech d?e zaoëte herremeniekes viengde?', 0),
(67, 'carnaval', 'Kunnen we in deze zaak groene schminck kopen? ', 'Can we buy carnival''s makeup in this shop?', 'Kinne v’r in dees zaak greune sjmink koupe?', 'Kin v’r ien dies zaoëk greune sjmienk gèlle', 0),
(68, 'carnaval', 'Welke bakker heeft verse nonnevotten in de etalage liggen? 	', 'Which bakery sells fresh carnival pastry?', 'Wat veur ‘ne bekker heet veerse nonnevotte in de kiekoet ligke?', 'Welke bekker haet vieëse nonnevotte ien de etalaasj liegge?', 0),
(69, 'carnaval', 'Sjunkele, waar kan ik dat leren? ', 'Where can I learn the typical carnival''s dance movements (Sjunkele)?', 'Sjoenkele, boe kin iech dat liere?', 'Sjoenkele … oe kin iech dat liere?', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
