# Names of Gods, People, Alphabet Letters

I use a collection of various names when doing analysis or
reverse engineering to change non-human friendly hex names or
constants to friendly, easy to remember names.

Alphabets are good because the names of letters does not carry
any meaning and are easy to remember. The bad thing is that their
number is limited - combining hebrew and greek you can name around
60 entities.

Next I choose deities from greek and roman mythology. Their count
is greater than 60 but carry a meaning which is not desireble. On
the other hand these names are familiar and easy to remember.

Next comes human names from various ethnic groups. Currently my goal
is to parse the [Baby Names](http://babynames.net/) and take
names with length between 4 and 6 letters from Roman, Greek or any
other ethnic group that has:

* easy english pronunciation
* easy to remember
 
## Conventions

Object | Represented By
-------|---------------
Functions | Start names of not analyzed funcs with `ufcn.*`
Functions | Name funcs with people names
Local Vars | Use greek alphabet for local vars
Global Vars | Start names of globals with `global.[<type: struct, int, etc.>.]*`
Global Vars | Name globals with names of countries


## Alphabets

Greek | Hebrew
------|-------
Alpha | Alef
Beta | Bet
Gamma | Gimel
Delta | Dalet
Epsilon | He
Zeta | Vav
Eta | Zayin
Theta | Het
Iota | Tet
Kappa | Yodi
Lambda | Kaf
Mu | Lamedi
Nu | Memi
Xi | Nun
Omicron | Samekh
Pi | Ayini
Rho | Pei
Sigma | Tsadi
Tau | Qof
Upsilon | Resh
Phi | Shin
Chi | Tav
Psi |
Omega |


## Deities

Letter | Greek | Primary Roman | Secondary Roman
-------|------|---------------|----------------
A | Achelous, Aeolus, Aether, Alastor, Apollo, Ares, Aristaeus, Asclepius, Atlas, Attis | Apollo | Abundantia, Aesculapius, Aurora
B | Boreas | Bacchus | Bubona
C | Caerus, Castor, Cerus, Chaos, Charon, Cronos, Crios, Cronus | Ceres, Cupid | Candelifera, Carmenta, Clementia, Cloacina, Concordia, Cybele
D | Dinlas, Dionysus | Diana | Deverra, Discordia
E | Erebus, Eros, Eurus | | Edesia, Epona
F | | Fauna, Flora, Fortuna | Fabulinus, Fama, Felicitas, Fides
G | Glaucus | |
H | Hades, Helios, Hephaestus, Heracles, Hermes, Hesperus, Hymenaios, Hypnos | | Hercules, Hespera, Hippona, Honos
I | | | Invidia, Iris
J | | Janus, Juno, Jupiter, Jove | Justitia, Juventas
K | Kratos | |
L | | | Libertas, Libitina, Luna
M | Momus, Morpheus | Mars, Mercury, Minerva | Mithras, Muta
N | Nereus, Notus | Neptune | Necessita, Nemesis
O | Oceanus | | Opis
P | Pallas, Pan, Phosphorus, Plutus, Pollux, Pontus, Poseidon, Priapus, Pricus, Prometheus, Proteus | Pluto | Pax, Pietas, Pomona, Portunes, Proserpina
Q |
R |
S | | Saturn | Sancus, SolInvictus, Somnus, Sors, Spes
T | Tartarus, Thanatos, Triton, Typhon | | Tempestes, Tranquillitas, Trivia
U | Uranus ||
V | | Venus, Vesta, Vulcan | Veritas, Victoria, Voluptas, Volturnus
W |
X |
Y |
Z | Zelus, Zephyrus, Zeus ||

## Latin Numbers

Num | Cardinal | Ordinal | Root
----|----------|---------|-----
1  | Unus | Primus  | Prim
2  | Duo | Secundus | Secund
3  | Tres | Tertius | Terti
4  | Quattuor | Quartus | Quart
5  | Quinque | Quintus | Quint
6  | Sex | Sextus | Sext
7  | Septen | Septimus | Septim
8  | Octo | Octavus | Octav
9  | Novem | Nonus | Non
10 | Decem | Decimus | Decim



## People Names

Letter | African | Latin | Germanic | Japanese
-------|---------|-------|----------|---------
A | Adisa, Akachi, Amara, Arusi, Ashanti | Ace, Adria, Amadeo, Ange, Anton | Ada, Adele, Akela, Alfred, Amory | Akio, Akira
B | Berko, Bongani, Bosede, Baako | Balaz, Basil, Bella, Benita, Benz, Bras | Bach, Berman, Berta, Bianca, Bogart, Bruno, Burke |
C | Cayman, Chipo, Chikere | Caesar, Callum, Candida, Cato, Cicero | Carla, Charlie, Chuck, Clovis, Conrad, Curt |
D | Dada, Delu, Desta, Dubaku | Dante, Dea, Decima, Destin, Diva, Dominic | Derek, Dixon, Dolph | Daisuke
E | Ebele, Ekene, Emem | Elba, Emil, Erroll, Estela | Earnest, Edlyn, Elke, Elvira, Emma, Enzo, Ernesto, Evette | Eito
F | Femi, Furaha | Fabia, Faust, Felicia, Felix, Fidel, Floris, Franco | Fedor, Fernando, Frank, Fred, Frodo | Fumihiro
G |  | Galo, Gemini, Gina, Graciela, Gusta | Gary, Gerald, Gerda, Gilbert, Guido, Gustav | Giichi
H |  | Honor, Horacio | Hamlet, Harry, Heidi, Helmut, Henry, Hilda, Hudson, Hugo | Hansuke, Haruki, Hirohito, Hisato, Hitoshi
I | Ife, Imari | Ignatia, Isa, Isabel, Izzy | Irma, Ives, Iveta, Ivona | Ichiro, Ikki, Itsuki, Izumi
J | Jabari, Jaz | Julek, Julio, Justin | Jager, Jeff, Jerry |
K | Kanye, Kofi, Kunto | Kai, Kalem, Kia, Kimo, Klara, Kliment | Karl, Karolina, Konrad, Kramer | Katsumi, Kobe, Kosuke
L | Lekan, Lerato | Lamar, Larkin, Laura, Leon, Livia | Lance, Leonard, Liam, Linda, Ludvik, Luiza, Luther |
M | Makena, Masika, Mesi, Monifa | Magnus, Mandy, Marcel, Marcus, Marius, Maximus, Myra | Matilda, Milo, Mina | Mao
N | Nakato, Nomusa, Nuru | Narda, Nero, Nova, Nydia | Nilda, Norman | Naoki, Nariko, Nozomi
O | Obasi, Oni | Octavian, Onora, Ora, Ova, Ovid | Oberon, Oliver, Orlando, Oswald, Otto |
P |  | Pablo, Paco, Pascal, Pasha, Patrik, Paula, Pavla, Perla, Proctor  | Perry |
Q |  | Quentin |  |
R | Rufaro, Rutendo | Randy, Remus, Renata, Renzo, Rex, Rita, Romano, Rufina | Ramon, Randy, Raul, Ricardo, Robert, Rocco, Rodrigo, Rolf, Ronaldo,  | Raiden, Ren
S | Sade, Sauda, Sekai, Simba, Subira | Sabrina, Sage, Scipio, Severin, Sidra, Silvio | Saxon, Selma, Sigmund | Saburo, Sachi, Subaru
T | Talib, Tuma | Tanya, Terra, Titus, Trinity | Terry, Truman, Tudor | Tadashi, Tamiko, Tatsuo, Toshiro
U |  | Urbana, Ursula | Umberto | Umeko
V |  | Vale, Venus, Vera, Vesta, Vicente, Vidal, Virgil, Vitus, Vivian | Valter, Vonda |
W | Wekesa | Wikolia | Wagner, Warner, Wayland, Wilma, Wilson, Wolfgang |
X |  |  |  |
Y |  | Yolanda, Yustina |  | Yamato, Yoshi, Yosuke, Yuri
Z | Zaire, Zalika, Zuberi, Zula | Zetta, Zisel |  |


## People Names 2

Letter | Women | Man
-------|-------|----
A | Anna, Andrea, Anabel, Amanda, Adisa, Adelina, Ada,  | Anton, Adrian, Amadeos, Alfred, Adolf
B | Biliana, Bella, Berta, Benita, Bianca | Boris, Barko, Boyan, Bogdan, Branimir, Bratan, Bruno, Bogart, Berko, Bogani, Bach
C | Carla, Clovis, Candida, Ceca | Caesar, Cato, Ciceron, Chuck, Conrad, Curt, Cvetan, Charlie
D | Desi, Darina, Doris, Diva, Dimana, Dobrinka, Diana, Daria, Donka | Dobrin, Dido, Damiyan
E | Elena | Emil
F |  | Filip
G |  | Gabriel, Gosho, Grigor
H |  |
I |  | Ivan
J |  | Jeremy
K |  |
L |  |
M |  |
N |  |
O |  |
P |  |
Q |  |
R |  |
S |  |
T |  |
U |  |
V |  |
W |  |
X |  |
Y |  |
Z |  |

## Countries

Letter | Country
-------|--------
A | Afghanistan, Albania, Algeria, Andorra, Angola, Anguilla, Antigua, Argentina, Armenia, Australia, Austria, Azerbaijan
B | Bahamas, Bahrain, Bangladesh, Barbados, Belarus, Belgium, Belize, Benin, Bermuda, Bhutan, Bolivia, Bosnia & Herzegovina, Botswana, Brazil, Brunei Darussalam, Bulgaria, Burkina Faso, Burma, Burundi, Barbuda
C | Cambodia, Cameroon, Canada, Cape Verde, Cayman Islands, Central African Republic, Chad, Chile, China, Colombia, Comoros, Congo, Costa Rica, Croatia, Cuba, Cyprus, Czech Republic,
D | Denmark, Djibouti, Dominican Republic, Dominica
E | Ecuador, Egypt, El Salvador, Equatorial Guinea, Eritrea, Estonia, Ethiopia
F | Fiji, Finland, France, French Guiana
G | Gabon, Gambia, Georgia, Germany, Ghana, Great Britain, Greece, Grenada, Guadeloupe, Guatemala, Guinea, Guinea-Bissau, Guyana, Grenadines
H | Haiti, Honduras, Hungary
I | Iceland, India, Indonesia, Iran, Iraq, Israel, Italy, Ivory Coast
J | Jamaica, Japan, Jordan
K | Kazakhstan, Kenya, Kosovo, Kuwait, Kyrgyzstan
L | Laos, Latvia, Lebanon, Lesotho, Liberia, Libya, Liechtenstein, Lithuania, Luxembourg
M | Macedonia, Madagascar, Malawi, Malaysia, Maldives, Mali, Malta, Martinique, Mauritania, Mauritius, Mayotte, Mexico, Moldova, Monaco, Mongolia, Montenegro, Montserrat, Morocco, Mozambique, Myanmar
N | Namibia, Nepal, Netherlands, New Zealand, Nicaragua, Niger, Nigeria, North Korea, Norway
O | Oman
P | Pacific Islands, Pakistan, Panama, Papua New Guinea, Paraguay, Peru, Philippines, Poland, Portugal, Puerto Rico
Q | Qatar
R | Romania, Russia, Rwanda
S | Samoa, Saudi Arabia, Senegal, Serbia, Seychelles, Sierra Leone, Singapore, Slovakia, Slovenia, Solomon Islands, Somalia, South Africa, South Korea, South Sudan, Spain, Sri Lanka, Sudan, Suriname, Swaziland, Sweden, Switzerland, Syria, Sao Tome And Principe, Saint Kitts and Nevis, Saint Lucia, Saint Vincent
T | Tajikistan, Tanzania, Thailand, Timor Leste, Togo, Trinidad, Tobago, Tunisia, Turkey, Turkmenistan
U | Uganda, Ukraine, United Arab Emirates, USA, Uruguay, Uzbekistan
V | Venezuela, Vietnam, Virgin Islands
W |
X |
Y | Yemen
Z | Zambia, Zimbabwe

## Capitals

Letter | Capital City
-------|-------------


## Colors

* white
* silver
* gray
* black
* navy
* blue
* turquoise
* azure
* teal
* cyan
* green
* lime
* olive
* yellow
* gold
* amber
* orange
* brown
* red
* maroon
* pink
* magenta
* purple
* indigo
* violet
* ochre


## References

* https://greekgodsandgoddesses.net/gods/
* http://babynames.net

