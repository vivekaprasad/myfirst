from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, input_message_content, user_and_chats
from pyrogram.types import ChatPermissions
from pyrogram.errors import MessageNotModified

bot = Client(
    'all subject bot',
    api_id=7009965,
    api_hash="06651b174c4f0591deb0ed1e5663c996",
    
)

START_MESSAGE='Group menu'
A0001_TEXT='Subject menu'
A0003_TEXT='secound menu'
A0004_TEXT='ICT MENU'
A0005_TEXT='build in progress🛠'
A0006_TEXT='build in progress🛠'
A0007_TEXT='build in progress🛠'
A0008_TEXT='build in progress🛠'
A0009_TEXT='build in progress🛠'
A0010_TEXT='ICT PAPERS'
A0011_TEXT='ICT NOTES & OTHERS'
A0022_TEXT='🔥2011-2020 ICT පසුගිය ප්‍රශ්නපත්‍ර🔥\n\n⭕️⭕️All Credits Goes To Rightful Owners. No Copyright Infringement Intended.⭕️⭕️'
A0023_TEXT='🔥2011-2020 A/L ICT පිලිතුරුපත්‍ර 🔥\n\n⭕️⭕️All Credits Goes To Rightful Owners. No Copyright Infringement Intended.⭕️⭕️'
A0024_TEXT='2011 සිට 2020 දක්වා ඇති සියලූම පසුගිය ප්‍රශ්න සදහා විවරණ📝\n (video සහ audio ලෙස)\n\n all credits goes to @ICTLibraryBot & @TechlogicLK'
A0025_TEXT='පසුගිය ප්‍රශ්නපත්‍ර(ONLINE TESTS)'
A0026_TEXT='පලාත් ප්‍රශ්නපත්‍ර'
A0027_TEXT='සියලුම පාඩම් වල නෝට්ස්'
CLOSE_TEXT='User closed menu!!'




M001_TEXT='2011 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2011 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M002_TEXT='2012 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2012 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M003_TEXT='2013 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2013 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M004_TEXT='2014 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2014 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M005_TEXT='2015 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2015 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M006_TEXT='2016 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2016 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M007_TEXT='2017 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2017 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M008_TEXT='2018 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2018 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M009_TEXT='2019 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2019 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'
M010_TEXT='2020 ප්‍රශ්න පත්‍ර සාකච්ඡාව\nමෙම නාලිකාව තුල 2020 උසස් පෙළ ප්‍රශ්න පත්‍රයෙහි සියලුම ගැටලු සදහා පිලිතුරු වෙන වෙනම විවරණය කොට ඇත. එම ප්‍රශ්නයට අදාළ බට්න් එක ක්ලික් කර  විවරණය ලබා ගත හැක.'


















START_BUTTONS=[
    [InlineKeyboardButton('ENTER SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('MORE',callback_data='A0003')],
    [InlineKeyboardButton('HELP',url='https://t.me/ictstudenthelper/140')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
# subject menu
A0001_BUTTONS=[
    [InlineKeyboardButton('ICT',callback_data='A0004')],
    [InlineKeyboardButton('MATHS',callback_data='A0005')],
    [InlineKeyboardButton('BIOLOGY',callback_data='A0006')],
    [InlineKeyboardButton('TECHNOLGY',callback_data='A0007')],
    [InlineKeyboardButton('COMMERCE',callback_data='A0008')],
    [InlineKeyboardButton('ART',callback_data='A0009')],
    [InlineKeyboardButton('⬅️BACK',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
#more
A0003_BUTTONS=[
    [InlineKeyboardButton('HOW TO USE',url='https://t.me/ictstudenthelper/140')],
    [InlineKeyboardButton('Useful groups and channels',callback_data='grps')],
    [InlineKeyboardButton('➕ADD TO GROUP➕',url='http://t.me/grpmenubot?startgroup=botstart')],
    [InlineKeyboardButton('⬅️BACK',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
#ict
A0004_BUTTONS=[
    [InlineKeyboardButton('PAPERS',callback_data='A0010'),InlineKeyboardButton('NOTES',callback_data='A0011')],
    [InlineKeyboardButton('⬅️BACK',callback_data='A0001'),InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
#maths
A0005_BUTTONS=[
    
    [InlineKeyboardButton('⬅️BACK',callback_data='A0001'),InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
A0006_BUTTONS=[
    
    [InlineKeyboardButton('⬅️BACK',callback_data='A0001'),InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
A0007_BUTTONS=[
    
    [InlineKeyboardButton('⬅️BACK',callback_data='A0001'),InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
A0008_BUTTONS=[
    
    [InlineKeyboardButton('⬅️BACK',callback_data='A0001'),InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]
A0009_BUTTONS=[
    
    [InlineKeyboardButton('⬅️BACK',callback_data='A0001'),InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('❌CLOSE❌',callback_data='CLOSE')],
]

grps_BUTTONS=[

]

A0010_BUTTONS=[
    [InlineKeyboardButton('පසුගිය ප්‍රශ්නපත්‍ර',callback_data='A0022')],
    [InlineKeyboardButton('පසුගිය ප්‍රශ්නපත්‍ර වල පිලිතුරු',callback_data='A0023')],
    [InlineKeyboardButton('2010-2020 MCQ විවරණ',callback_data='A0024')],
    [InlineKeyboardButton('පසුගිය ප්‍රශ්නපත්‍ර(ONLINE TESTS)',callback_data='A0025')],
    [InlineKeyboardButton('පලාත් ප්‍රශ්නපත්‍ර',callback_data='A0026')],
    [InlineKeyboardButton('පාඩම් පිලිවෙලට පසුගිය ප්‍රශ්න පත්‍ර වල කෙටි ප්‍රශ්න',url='https://t.me/ictstudenthelper/134')],
    [InlineKeyboardButton('BACK',callback_data='A0004'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]

A0011_BUTTONS=[
    [InlineKeyboardButton('සියලුම පාඩම් වල නෝට්ස්',callback_data='A0027')],
    [InlineKeyboardButton('විශය නිර්දේශය',url='https://t.me/ictstudenthelper/127')],
    [InlineKeyboardButton('ගුරු අත්පොත්',url='https://t.me/ictstudenthelper/142?single')],
    [InlineKeyboardButton('BACK',callback_data='A0004'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]


A0022_BUTTONS=[
    [InlineKeyboardButton('2011 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/94'),InlineKeyboardButton('2012 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/96')],
    [InlineKeyboardButton('2013 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/97'),InlineKeyboardButton('2014 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/99')],
    [InlineKeyboardButton('2015 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/100'),InlineKeyboardButton('2016 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/102')],
    [InlineKeyboardButton('2017 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/104'),InlineKeyboardButton('2018 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/106')],
    [InlineKeyboardButton('2019 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/108'),InlineKeyboardButton('2020 ප්‍රශ්නපත්‍රය',url='https://t.me/ictstudenthelper/110')],
    [InlineKeyboardButton('2021 MCQ PAPER',url='https://t.me/ictstudenthelper/403'),InlineKeyboardButton('2021 ESSAY PAPER',url='https://t.me/ictstudenthelper/405')],
    [InlineKeyboardButton('BACK',callback_data='A0010'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]

A0023_BUTTONS=[
    [InlineKeyboardButton('2011 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/112'),InlineKeyboardButton('2012 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/113')],
    [InlineKeyboardButton('2013 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/116'),InlineKeyboardButton('2014 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/114')],
    [InlineKeyboardButton('2015 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/115'),InlineKeyboardButton('2016 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/117')],
    [InlineKeyboardButton('2017 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/118'),InlineKeyboardButton('2018 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/119')],
    [InlineKeyboardButton('2019 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/121'),InlineKeyboardButton('2020 පිලිතුරු පත්‍රය',url='https://t.me/ictstudenthelper/122')],
    [InlineKeyboardButton('2021 පිලිතුරු පත්‍රය(mcq)',url='https://t.me/ictstudenthelper/404')],
    [InlineKeyboardButton('BACK',callback_data='A0010'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],

]

A0024_BUTTONS=[
    [InlineKeyboardButton('2011 MCQ විවරණ ',callback_data='M001'),InlineKeyboardButton('2012 MCQ විවරණ ',callback_data='M002')],
    [InlineKeyboardButton('2013 MCQ විවරණ ',callback_data='M003'),InlineKeyboardButton('2014 MCQ විවරණ ',callback_data='M004')],
    [InlineKeyboardButton('2015 MCQ විවරණ ',callback_data='M005'),InlineKeyboardButton('2016 MCQ විවරණ ',callback_data='M006')],
    [InlineKeyboardButton('2017 MCQ විවරණ ',callback_data='M007'),InlineKeyboardButton('2018 MCQ විවරණ ',callback_data='M008')],
    [InlineKeyboardButton('2019 MCQ විවරණ ',callback_data='M009'),InlineKeyboardButton('2020 MCQ විවරණ ',callback_data='M010')],
    [InlineKeyboardButton('BACK',callback_data='A0010'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]


A0025_BUTTONS=[
    [InlineKeyboardButton('2011 ප්‍රශ්නපත්‍රය',url=''),InlineKeyboardButton('2012 ප්‍රශ්නපත්‍රය',url='')],
    [InlineKeyboardButton('2013 ප්‍රශ්නපත්‍රය',url=''),InlineKeyboardButton('2014 ප්‍රශ්නපත්‍රය',url='')],
    [InlineKeyboardButton('2015 ප්‍රශ්නපත්‍රය',url=''),InlineKeyboardButton('2016 ප්‍රශ්නපත්‍රය',url='')],
    [InlineKeyboardButton('2017 ප්‍රශ්නපත්‍රය',url=''),InlineKeyboardButton('2018 ප්‍රශ්නපත්‍රය',url='')],
    [InlineKeyboardButton('2019 ප්‍රශ්නපත්‍රය',url=''),InlineKeyboardButton('2020 ප්‍රශ්නපත්‍රය',url='')],
    [InlineKeyboardButton('BACK',callback_data='A0010'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]

A0026_BUTTONS=[
        [InlineKeyboardButton('උතුරුමැද පළාත ', url ='https://t.me/+_jY5zx2QOsdkNzY1')],
        [InlineKeyboardButton('බස්නාහිර පළාත',url = 'https://t.me/+uyz8ytOlnmRlMWU1')],
        [InlineKeyboardButton('සබරගමු පළාත ',url = 'https://t.me/+Ix6MKupPs_I0YTk1')],
        [InlineKeyboardButton('දකුණු පළාත ',url = 'https://t.me/+jUYVycIaFKQxOWVl')],
        [InlineKeyboardButton('මධ්‍යම පළාත ',url='https://t.me/+okYXGuAEZNlhZDU1')],   
        [InlineKeyboardButton('BACK',callback_data='A0010'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
        [InlineKeyboardButton('START MENU',callback_data='MAIN')],
        [InlineKeyboardButton('CLOSE',callback_data='CLOSE')], 
]

A0027_BUTTONS=[
    [InlineKeyboardButton('01 පාඩම',url='https://t.me/joinchat/AAAAAE_0DlrMqfOgs0aElw'),InlineKeyboardButton('02 පාඩම',url='https://t.me/joinchat/AAAAAFAJDpi2i-lC8hJPQw')],
    [InlineKeyboardButton('03 පාඩම',url='https://t.me/joinchat/AAAAAET3bpq3VQrxY24dYQ'),InlineKeyboardButton('04 පාඩම',url='https://t.me/joinchat/AAAAAE1XqikQISW6vDneVQ')],
    [InlineKeyboardButton('05 පාඩම',url='https://t.me/joinchat/AAAAAFMa0pE6DKr3VEQ2Mw'),InlineKeyboardButton('06 පාඩම',url='https://t.me/joinchat/AAAAAEjGf-6cPk_ogahExA')],
    [InlineKeyboardButton('07 පාඩම',url='https://t.me/joinchat/AAAAAEn8DMRPAFI3dwamMw'),InlineKeyboardButton('08 පාඩම',url='https://t.me/joinchat/AAAAAFhXIqjJbaf8CvWmlg')],
    [InlineKeyboardButton('09 පාඩම',url='https://t.me/joinchat/AAAAAFbgjgjptQdaqZm5xw'),InlineKeyboardButton('10 පාඩම',url='https://t.me/joinchat/AAAAAEzL4MnUwSsd0tvKfQ')],
    [InlineKeyboardButton('11 පාඩම',url='https://t.me/joinchat/AAAAAE52AQVPQDeNl_D4eA'),InlineKeyboardButton('12 පාඩම',url='https://t.me/joinchat/AAAAAFU8Gy1-DlHK497vfQ')],
    [InlineKeyboardButton('13 පාඩම',url='https://t.me/joinchat/AAAAAFEc_PVGaAwSUkaOGA')],
    [InlineKeyboardButton('BACK',callback_data='A0010'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]



#mcq wiwarana
#----------------------------------------------------------------------------------------------------------------------------

M001_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2011/9"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2011/16"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2011/23"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2011/36")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2011/40"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2011/44"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2011/48"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2011/57")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2011/68"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2011/80"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2011/84"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2011/88")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2011/100"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2011/104"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2011/109"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2011/115")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2011/122"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2011/128"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2011/147"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2011/154")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2011/160"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2011/165"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2011/172"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2011/179")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2011/188"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2011/192"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2011/196"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2011/201")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2011/206"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2011/211"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2011/215"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2011/219")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2011/223"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2011/228"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2011/232"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2011/236")
    ],
     [
        InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2011/245"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2011/249"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2011/253"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2011/257")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2011/261"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2011/265"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2011/269"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2011/276")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2011/280"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2011/284"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2011/289"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2011/294")],
    [InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2011/307"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2011/317")],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
] 
M002_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2012/14"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2012/18"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2012/23"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2012/29")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2012/33"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2012/41"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2012/46"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2012/51")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2012/56"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2012/62"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2012/66"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2012/70")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2012/76"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2012/81"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2012/87"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2012/93")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2012/101"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2012/110"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2012/122"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2012/127")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2012/132"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2012/137"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2012/141"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2012/148")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2012/154"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2012/162"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2012/170"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2012/175")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2012/179"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2012/183"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2012/187"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2012/191")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2012/195"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2012/199"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2012/204"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2012/209")
    ],
    [
        InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2012/216"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2012/219"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2012/223"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2012/227")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2012/231"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2012/235"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2012/239"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2012/243")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2012/248"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2012/255"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2012/265"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2012/270")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2012/277"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2012/298")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M003_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2013/6"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2013/11"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2013/18"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2013/23")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2013/27"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2013/31"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2013/40"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2013/48")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2013/56"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2013/62"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2013/67"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2013/72")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2013/82"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2013/87"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2013/92"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2013/99")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2013/105"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2013/111"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2013/116"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2013/124")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2013/130"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2013/136"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2013/141"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2013/146")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2013/150"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2013/154"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2013/159"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2013/163")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2013/170"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2013/174"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2013/178"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2013/182")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2013/189"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2013/193"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2013/198"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2013/203")
    ],   
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2013/207"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2013/211"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2013/215"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2013/219")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2013/223"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2013/227"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2013/231"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2013/235")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2013/251"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2013/256"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2013/273"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2013/277")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2013/281"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2013/288")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M004_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2014/6"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2014/12"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2014/19"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2014/38")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2014/42"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2014/46"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2014/51"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2014/56")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2014/60"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2014/65"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2014/70"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2014/74")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2014/86"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2014/95"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2014/107"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2014/111")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2014/115"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2014/119"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2014/123"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2014/127")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2014/133"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2014/137"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2014/141"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2014/145")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2014/149"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2014/160"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2014/175"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2014/179")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2014/184"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2014/188"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2014/195"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2014/202")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2014/206"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2014/211"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2014/216"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2014/223")
    ],
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2014/257"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2014/262"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2014/278"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2014/284")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2014/289"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2014/296"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2014/301"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2014/307")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2014/312"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2014/321"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2014/326"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2014/331")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2014/337"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2014/345")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M005_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2015/6"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2015/14"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2015/21"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2015/26")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2015/31"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2015/37"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2015/45"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2015/51")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2015/56"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2015/61"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2015/66"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2015/76")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2015/81"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2015/99"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2015/103"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2015/107")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2015/111"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2015/118"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2015/123"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2015/128")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2015/132"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2015/147"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2015/182"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2015/188")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2015/193"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2015/197"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2015/209"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2015/214")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2015/218"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2015/222"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2015/228"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2015/235")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2015/239"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2015/255"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2015/274"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2015/279")
    ],
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2015/283"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2015/291"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2015/296"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2015/301")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2015/308"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2015/316"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2015/322"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2015/328")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2015/340"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2015/346"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2015/350"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2015/358")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2015/363"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2015/370")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M006_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2016/6"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2016/11"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2016/19"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2016/25")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2016/29"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2016/35"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2016/41"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2016/46")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2016/51"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2016/56"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2016/63"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2016/74")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2016/83"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2016/87"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2016/91"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2016/95")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2016/99"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2016/105"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2016/112"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2016/117")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2016/122"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2016/134"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2016/152"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2016/167")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2016/171"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2016/175"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2016/180"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2016/186")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2016/190"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2016/195"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2016/203"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2016/208")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2016/213"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2016/229"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2016/236"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2016/242")
    ],
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2016/246"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2016/251"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2016/256"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2016/261")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2016/265"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2016/269"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2016/273"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2016/279")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2016/294"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2016/300"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2016/304"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2016/308")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2016/314"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2016/324")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M007_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2017/6"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2017/11"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2017/18"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2017/22")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2017/29"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2017/58"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2017/66"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2017/71")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2017/75"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2017/79"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2017/89"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2017/93")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2017/97"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2017/106"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2017/113"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2017/120")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2017/130"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2017/136"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2017/142"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2017/148")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2017/163"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2017/168"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2017/173"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2017/177")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2017/182"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2017/186"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2017/190"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2017/194")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2017/198"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2017/202"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2017/219"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2017/226")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2017/230"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2017/235"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2017/239"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2017/243")
    ],
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2017/255"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2017/259"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2017/263"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2017/271")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2017/287"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2017/302"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2017/307"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2017/311")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2017/319"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2017/323"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2017/328"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2017/332")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2017/344"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2017/355")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M008_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2018/6"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2018/15"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2018/26"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2018/31")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2018/35"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2018/42"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2018/55"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2018/63")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2018/68"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2018/75"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2018/83"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2018/93")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2018/99"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2018/103"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2018/108"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2018/113")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2018/117"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2018/121"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2018/125"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2018/129")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2018/134"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2018/161"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2018/171"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2018/177")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2018/181"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2018/187"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2018/191"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2018/195")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2018/200"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2018/215"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2018/231"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2018/244")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2018/254"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2018/260"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2018/274"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2018/280")
    ],
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2018/291"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2018/298"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2018/307"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2018/316")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2018/321"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2018/336"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2018/356"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2018/362")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2018/376"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2018/385"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2018/401"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2018/408")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2018/417"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2018/421")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M009_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2019/5"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2019/9"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2019/17"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2019/21")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2019/26"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2019/33"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2019/41"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2019/51")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2019/56"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2019/65"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2019/74"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2019/86")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2019/94"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2019/98"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2019/113"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2019/117")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2019/121"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2019/126"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2019/130"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2019/135")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2019/145"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2019/152"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2019/159"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2019/166")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2019/173"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2019/180"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2019/184"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2019/188")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2019/197"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2019/205"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2019/212"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2019/221")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2019/225"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2019/232"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2019/246"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2019/255")
    ],
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2019/260"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2019/264"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2019/268"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2019/275")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2019/280"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2019/285"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2019/291"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2019/296")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2019/302"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2019/307"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2019/312"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2019/317")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2019/324"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2019/330")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]
M010_BUTTONS =[
    [
        InlineKeyboardButton('📊01',url="https://t.me/ICTMCQ2020/11"),InlineKeyboardButton('📊02',url="https://t.me/ICTMCQ2020/16"),InlineKeyboardButton('📊03',url="https://t.me/ICTMCQ2020/20"),InlineKeyboardButton('📊04',url="https://t.me/ICTMCQ2020/25")
    ],
    [
        InlineKeyboardButton('📊05',url="https://t.me/ICTMCQ2020/29"),InlineKeyboardButton('📊06',url="https://t.me/ICTMCQ2020/47"),InlineKeyboardButton('📊07',url="https://t.me/ICTMCQ2020/54"),InlineKeyboardButton('📊08',url="https://t.me/ICTMCQ2020/59")
    ],
    [
        InlineKeyboardButton('📊09',url="https://t.me/ICTMCQ2020/68"),InlineKeyboardButton('📊10',url="https://t.me/ICTMCQ2020/78"),InlineKeyboardButton('📊11',url="https://t.me/ICTMCQ2020/86"),InlineKeyboardButton('📊12',url="https://t.me/ICTMCQ2020/92")
    ],
     [
        InlineKeyboardButton('📊13',url="https://t.me/ICTMCQ2020/97"),InlineKeyboardButton('📊14',url="https://t.me/ICTMCQ2020/101"),InlineKeyboardButton('📊15',url="https://t.me/ICTMCQ2020/105"),InlineKeyboardButton('📊16',url="https://t.me/ICTMCQ2020/110")
    ],
    [
        InlineKeyboardButton('📊17',url="https://t.me/ICTMCQ2020/114"),InlineKeyboardButton('📊18',url="https://t.me/ICTMCQ2020/118"),InlineKeyboardButton('📊19',url="https://t.me/ICTMCQ2020/105"),InlineKeyboardButton('📊20',url="https://t.me/ICTMCQ2020/128")
    ],
    [
        InlineKeyboardButton('📊21',url="https://t.me/ICTMCQ2020/137"),InlineKeyboardButton('📊22',url="https://t.me/ICTMCQ2020/146"),InlineKeyboardButton('📊23',url="https://t.me/ICTMCQ2020/157"),InlineKeyboardButton('📊24',url="https://t.me/ICTMCQ2020/161")
    ],
     [
        InlineKeyboardButton('📊25',url="https://t.me/ICTMCQ2020/168"),InlineKeyboardButton('📊26',url="https://t.me/ICTMCQ2020/178"),InlineKeyboardButton('📊27',url="https://t.me/ICTMCQ2020/185"),InlineKeyboardButton('📊28',url="https://t.me/ICTMCQ2020/189")
    ],
    [
        InlineKeyboardButton('📊29',url="https://t.me/ICTMCQ2020/193"),InlineKeyboardButton('📊30',url="https://t.me/ICTMCQ2020/199"),InlineKeyboardButton('📊31',url="https://t.me/ICTMCQ2020/185"),InlineKeyboardButton('📊32',url="https://t.me/ICTMCQ2020/209")
    ],
    [
        InlineKeyboardButton('📊33',url="https://t.me/ICTMCQ2020/213"),InlineKeyboardButton('📊34',url="https://t.me/ICTMCQ2020/217"),InlineKeyboardButton('📊35',url="https://t.me/ICTMCQ2020/221"),InlineKeyboardButton('📊36',url="https://t.me/ICTMCQ2020/226")
    ],
     [
       InlineKeyboardButton('📊37',url="https://t.me/ICTMCQ2020/231"),InlineKeyboardButton('📊38',url="https://t.me/ICTMCQ2020/240"),InlineKeyboardButton('📊39',url="https://t.me/ICTMCQ2020/246"),InlineKeyboardButton('📊40',url="https://t.me/ICTMCQ2020/251")
    ],
    [
        InlineKeyboardButton('📊41',url="https://t.me/ICTMCQ2020/258"),InlineKeyboardButton('📊42',url="https://t.me/ICTMCQ2020/263"),InlineKeyboardButton('📊43',url="https://t.me/ICTMCQ2020/271"),InlineKeyboardButton('📊44',url="https://t.me/ICTMCQ2020/276")
    ],
    [
        InlineKeyboardButton('📊45',url="https://t.me/ICTMCQ2020/280"),InlineKeyboardButton('📊46',url="https://t.me/ICTMCQ2020/284"),InlineKeyboardButton('📊47',url="https://t.me/ICTMCQ2020/288"),InlineKeyboardButton('📊48',url="https://t.me/ICTMCQ2020/292")
    ],
    [
        InlineKeyboardButton('📊49',url="https://t.me/ICTMCQ2020/298"),InlineKeyboardButton('📊50',url="https://t.me/ICTMCQ2020/304")
    ],
    [InlineKeyboardButton('BACK',callback_data='A0024'),InlineKeyboardButton('SUBJECT MENU',callback_data='A0001')],
    [InlineKeyboardButton('START MENU',callback_data='MAIN')],
    [InlineKeyboardButton('CLOSE',callback_data='CLOSE')],
]


#------------------------------------------------------------------------------------------------------------------------------

































@bot.on_message(filters.command('start')& filters.private) #start
def start(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_message(filters.command('menu')) #start
def start(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_callback_query()
async def callback_query(client: Client, query: CallbackQuery):
    if query.data=="A0001":
        reply_markup = InlineKeyboardMarkup(A0001_BUTTONS)
        try:
            await query.edit_message_text(
                A0001_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass



    elif query.data=="A0003":
        reply_markup=InlineKeyboardMarkup(A0003_BUTTONS)
        try:
            await query.edit_message_text(
                A0003_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A0004":
        reply_markup=InlineKeyboardMarkup(A0004_BUTTONS)
        try:
            await query.edit_message_text(
                A0004_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A0005":
        reply_markup=InlineKeyboardMarkup(A0005_BUTTONS)
        try:
            await query.edit_message_text(
                A0005_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass        

    elif query.data=="A0006":
        reply_markup=InlineKeyboardMarkup(A0006_BUTTONS)
        try:
            await query.edit_message_text(
                A0006_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A0007":
        reply_markup=InlineKeyboardMarkup(A0007_BUTTONS)
        try:
            await query.edit_message_text(
                A0007_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A0008":
        reply_markup=InlineKeyboardMarkup(A0008_BUTTONS)
        try:
            await query.edit_message_text(
                A0008_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="A0009":
        reply_markup=InlineKeyboardMarkup(A0009_BUTTONS)
        try:
            await query.edit_message_text(
                A0009_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='A0010':
        reply_markup=InlineKeyboardMarkup(A0010_BUTTONS)
        try:
            await query.edit_message_text(
                A0010_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='A0011':
        reply_markup=InlineKeyboardMarkup(A0011_BUTTONS)
        try:
            await query.edit_message_text(
                A0011_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
    
    elif query.data=='A0022':
        reply_markup=InlineKeyboardMarkup(A0022_BUTTONS)
        try:
            await query.edit_message_text(
                A0022_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='A0023':
        reply_markup=InlineKeyboardMarkup(A0023_BUTTONS)
        try:
            await query.edit_message_text(
                A0023_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='A0024':
        reply_markup=InlineKeyboardMarkup(A0024_BUTTONS)
        try:
            await query.edit_message_text(
                A0024_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='A0025':
        reply_markup=InlineKeyboardMarkup(A0025_BUTTONS)
        try:
            await query.edit_message_text(
                A0025_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='A0026':
        reply_markup=InlineKeyboardMarkup(A0026_BUTTONS)
        try:
            await query.edit_message_text(
                A0026_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='A0027':
        reply_markup=InlineKeyboardMarkup(A0027_BUTTONS)
        try:
            await query.edit_message_text(
                A0027_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
#mcq wiwarana-------------------------------------------------------------------------------------------------------------

    elif query.data=='M001':
        reply_markup=InlineKeyboardMarkup(M001_BUTTONS)
        try:
            await query.edit_message_text(
                M001_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M002':
        reply_markup=InlineKeyboardMarkup(M002_BUTTONS)
        try:
            await query.edit_message_text(
                M002_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M003':
        reply_markup=InlineKeyboardMarkup(M003_BUTTONS)
        try:
            await query.edit_message_text(
                M003_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M004':
        reply_markup=InlineKeyboardMarkup(M004_BUTTONS)
        try:
            await query.edit_message_text(
                M004_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M005':
        reply_markup=InlineKeyboardMarkup(M005_BUTTONS)
        try:
            await query.edit_message_text(
                M005_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M006':
        reply_markup=InlineKeyboardMarkup(M006_BUTTONS)
        try:
            await query.edit_message_text(
                M006_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M007':
        reply_markup=InlineKeyboardMarkup(M007_BUTTONS)
        try:
            await query.edit_message_text(
                M007_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M008':
        reply_markup=InlineKeyboardMarkup(M008_BUTTONS)
        try:
            await query.edit_message_text(
                M008_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M009':
        reply_markup=InlineKeyboardMarkup(M009_BUTTONS)
        try:
            await query.edit_message_text(
                M009_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=='M010':
        reply_markup=InlineKeyboardMarkup(M010_BUTTONS)
        try:
            await query.edit_message_text(
                M010_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass        
#--------------------------------------------------------------------------------------------------------------------------------
    elif query.data=="MAIN":
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
        try:
            await query.edit_message_text(
                START_MESSAGE,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="CLOSE":
        reply_markup=InlineKeyboardButton(START_BUTTONS)
        try:
            await query.edit_message_text(
                CLOSE_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    
    

           
                         
    


print("bot alive")
bot.run()
