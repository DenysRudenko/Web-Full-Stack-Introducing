from bs4 import BeautifulSoup

html_string = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Координати зображення</title>
</head>

<body>
    <img id='img' height="800" width="1400" usemap="#ukraine" alt="map" 
        src="https://uahistory.co/pidruchniki/gilberg-geography-8-class-2021/gilberg-geography-8-class-2021.files/image025.jpg">
        <div class="coord"></div>
        <div class="coords">Для фіксування декількох координат натисни на картинці на координаті</div>
    <script src="./src/code.js"></script> 
    
    <map name="ukraine">
        <area shape="poly" coords="609, 106, 627, 103, 641, 107, 646, 117, 656, 121, 671, 155, 679, 169, 701, 174, 715, 193, 748, 184, 761, 199, 769, 220, 758, 230, 750, 246, 730, 256, 712, 246, 704, 254, 692, 286, 683, 294, 646, 300, 644, 309, 622, 308, 610, 306" href="https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="kyivska" onclick="myKyiv()">
        <area shape="poly" coords="665, 120, 672, 156, 698, 169, 715, 189, 746, 183, 766, 187, 773, 207, 836, 190, 842, 169, 846, 152, 838, 145, 830, 141, 829, 132, 833, 123, 832, 107, 842, 94, 834, 78, 835, 67, 849, 59, 848, 37, 852, 24, 840, 22, 830, 30, 812, 31, 794, 23, 787, 27, 779, 46, 761, 51, 736, 41, 719, 43, 711, 47, 693, 45, 689, 48, 678, 60, 671, 68, 658, 88, 663, 103, 665, 115, 662, 123" href="https://rue.wikipedia.org/wiki/%D0%A7%D0%B5%D1%80%D0%BD%D1%97%D0%B3%D1%96%D0%B2%D1%81%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="chernigivska" onclick="chernigivska()">
        <area shape="poly" coords="562, 83, 572, 114, 571, 132, 583, 141, 586, 180, 579, 198, 594, 244, 575, 261, 576, 274, 544, 274, 544, 247, 523, 255, 450, 257, 438, 241, 447, 228, 446, 213, 432, 209, 416, 181, 423, 141, 449, 106, 467, 88, 489, 87, 522, 93, 532, 100, 553, 85" href="https://ru.wikipedia.org/wiki/%D0%96%D0%B8%D1%82%D0%BE%D0%BC%D0%B8%D1%80%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="shytomir" onclick="shutomurska()">
        <area shape="poly" coords="421, 142, 411, 177, 397, 178, 368, 198, 344, 209, 326, 202, 316, 210, 291, 209, 285, 219, 276, 220, 264, 199, 272, 177, 305, 161, 320, 172, 325, 157, 339, 131, 341, 121, 325, 103, 311, 91, 315, 71, 322, 51, 365, 61, 392, 66, 401, 72, 422, 72, 428, 81, 450, 87, 456, 90" href="https://uk.wikipedia.org/wiki/%D0%A0%D1%96%D0%B2%D0%BD%D0%B5%D0%BD%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="rivne" onclick="rivneska()">
        <area shape="poly" coords="259, 198, 265, 173, 300, 162, 313, 166, 320, 154, 327, 152, 336, 134, 337, 119, 322, 105, 311, 92, 306, 74, 314, 68, 317, 50, 292, 46, 262, 47, 226, 46, 221, 60, 204, 64, 193, 70, 178, 60, 173, 74, 180, 77, 167, 92, 170, 96, 181, 107, 190, 131, 184, 141, 187, 159, 213, 165, 228, 172, 231, 188, 259, 199" href="https://uk.wikipedia.org/wiki/%D0%92%D0%BE%D0%BB%D0%B8%D0%BD%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="lutsk" onclick="lutska()">
        <area shape="poly" coords="186, 164, 221, 171, 228, 189, 258, 200, 270, 221, 279, 239, 262, 239, 232, 263, 213, 262, 198, 269, 204, 290, 176, 296, 151, 296, 130, 329, 100, 316, 85, 298, 74, 246, 168, 180, 185, 177, 187, 161" href="https://uk.wikipedia.org/wiki/%D0%9B%D1%8C%D0%B2%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="lviv" onclick="lvivska()">
        <area shape="poly" coords="58, 293, 82, 301, 97, 332, 120, 331, 134, 335, 150, 357, 167, 361, 177, 368, 191, 388, 200, 408, 151, 404, 96, 382, 69, 383, 49, 379, 44, 365, 35, 364, 15,345, 53, 294" href="https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%B0%D1%80%D0%BF%D0%B0%D1%82%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="ushorod" onclick="zakarpatska()">
        <area shape="poly" coords="207, 266, 228, 270, 246, 316, 277, 338, 283, 345, 280, 357, 280, 371, 250, 382, 230, 397, 227, 416, 219, 427, 201, 409, 194, 391, 178, 368, 166, 356, 152, 355, 132, 328, 150, 189, 300, 202, 293, 207, 269" href="https://uk.wikipedia.org/wiki/%D0%86%D0%B2%D0%B0%D0%BD%D0%BE-%D0%A4%D1%80%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="ivano-frankivsk" onclick="ivanofrankivska()">
        <area shape="poly" coords="233, 279, 232, 267, 254, 252, 277, 242, 284, 226, 289, 217, 312, 211, 322, 209, 340, 208, 332, 247, 338, 262, 335, 286, 332, 299, 327, 323, 327, 344, 336, 364, 319, 362, 310, 352, 286, 348, 276, 334, 257, 319, 243, 306, 234, 285" href="https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D1%80%D0%BD%D0%BE%D0%BF%D0%BE%D0%BB%D1%8C%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="ternopil" onclick="ternopiska()">
        <area shape="poly" coords="412, 182, 383, 189, 342, 215, 339, 238, 337, 304, 329, 326, 338, 363, 376, 358, 414, 352, 420, 318, 433, 312, 452, 308, 448, 270, 435, 241, 433, 232, 439, 228, 441, 216, 428, 210, 414, 191, 408, 186" href="https://rue.wikipedia.org/wiki/%D0%A5%D0%BC%D0%B5%D0%BB%D1%8C%D0%BD%D0%B8%D1%86%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="hmelnutsk" onclick="hmelnicka()">
        <area shape="poly" coords="454, 312, 453, 266, 520, 257, 534, 252, 540, 279, 555, 281, 574, 275, 575, 295, 591, 319, 451, 315, 427, 330, 424, 359, 432, 371, 453, 269, 452, 285, 454, 311, 442, 316, 424, 331, 423, 373, 452, 379, 483, 402, 491, 411, 495, 409, 525, 413, 538, 404, 561, 411, 580, 415, 596, 394, 612, 380, 594, 350, 587, 333, 591, 320, 576, 304, 276, 540, 278, 534, 255, 500, 260, 459, 261" href="https://uk.wikipedia.org/wiki/%D0%92%D1%96%D0%BD%D0%BD%D0%B8%D1%86%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="vinnuca" onclick="vinnucka()">
        <area shape="poly" coords="222, 429, 228, 408, 241, 397, 254, 385, 279, 376, 283, 358, 312, 361, 332, 370, 349, 371, 365, 381, 342, 401, 322, 412, 273, 418, 249, 421, 237, 434, 229, 433" href="https://uk.wikipedia.org/wiki/%D0%A7%D0%B5%D1%80%D0%BD%D1%96%D0%B2%D0%B5%D1%86%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="chernivci" onclick="chernivci()">
        <area shape="poly" coords="615, 384, 646, 374, 663, 357, 703, 354, 717, 356, 725, 348, 732, 337, 756, 339, 777, 329, 796, 330, 821, 333, 824, 327, 798, 310, 771, 297, 746, 281, 780, 287, 811, 295, 809, 274, 794, 260, 768, 224, 758, 237, 729, 257, 716, 252, 706, 257, 690, 291, 670, 303, 654, 304, 626, 310, 604, 318, 591, 324, 589, 334, 598, 354, 614, 374" href="https://ru.wikipedia.org/wiki/%D0%A7%D0%B5%D1%80%D0%BA%D0%B0%D1%81%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="cherkasu" onclick="cherkaska()">
        <area shape="poly" coords="529, 422, 534, 407, 545, 410, 558, 417, 578, 417, 594, 407, 624, 414, 630, 430, 639, 444, 638, 453, 668, 461, 680, 472, 682, 490, 704, 502, 699, 516, 692, 520, 696, 554, 672, 559, 652, 597, 630, 575, 620, 582, 634, 595, 609, 625, 594, 637, 576, 654, 585, 677, 578, 679, 549, 663, 509, 676, 466, 659, 483, 650, 486, 634, 499, 625, 511, 611, 528, 597, 523, 567, 548, 562, 557, 563, 585, 567, 610, 573, 605, 548, 600, 533, 578, 520, 577, 503, 577, 485, 564, 486, 548, 469, 549, 443, 545, 424, 529, 420" href="https://ru.wikipedia.org/wiki/%D0%9E%D0%B4%D0%B5%D1%81%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="odessa" onclick="odesska()">
        <area shape="poly" coords="632, 418, 696, 407, 723, 418, 741, 422, 756, 446, 801, 447, 829, 837, 423, 843, 438, 837, 454, 847, 478, 837, 500, 829, 528, 803, 530, 770, 540, 737, 548, 703, 549, 696, 523, 707, 502, 682, 486, 679, 469, 665, 459, 647, 450, 630, 429, 629, 420, 807, 446, 831, 427, 838, 427, 839, 453, 843, 481, 836, 503, 830, 830, 523, 808, 528" href="https://uk.wikipedia.org/wiki/%D0%9C%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D1%97%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="mukolaiv" onclick="mukolaivska()">
        <area shape="poly" coords="613, 384, 599, 397, 605, 407, 637, 410, 661, 406, 687, 405, 702, 407, 722, 416, 747, 419, 746, 426, 756, 441, 770, 445, 709, 445, 807, 439, 813, 428, 820, 428, 834, 415, 855, 410, 870, 395, 878, 373, 892, 357, 896, 340, 855, 326, 828, 330, 801, 334, 784, 330, 771, 338, 738, 340, 734, 346, 707, 357, 662, 359, 620, 385, 606, 388,599, 399" href="https://uk.wikipedia.org/wiki/%D0%9A%D1%96%D1%80%D0%BE%D0%B2%D0%BE%D0%B3%D1%80%D0%B0%D0%B4%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="kropivnuckui" onclick="kropuvnucka()">
        <area shape="poly" coords="765, 543, 798, 534, 822, 540, 842, 514, 852, 491, 850, 467, 891, 470, 911, 470, 937, 480, 959, 494, 975, 521, 977, 544, 1005, 564, 1003, 578, 969, 605, 938, 588, 907, 587, 880, 608, 854, 596, 815, 602, 814, 572, 810, 543, 829, 540, 841, 521, 848, 497" href="https://ru.wikipedia.org/wiki/%D0%A5%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D1%81%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="herson" onclick="hersonska()">
        <area shape="poly" coords="847, 427, 844, 456, 875, 464, 914, 465, 981, 456, 979, 433, 982, 411, 996, 396, 1044, 408, 1069, 408, 1080, 423, 1106, 419, 1109, 400, 1132, 394, 1121, 361, 1095, 365, 1065, 335, 1014, 331, 979, 313, 952, 325, 938, 345, 907, 355, 890, 371, 881, 395, 860, 415, 847, 425" href="https://uk.wikipedia.org/wiki/%D0%94%D0%BD%D1%96%D0%BF%D1%80%D0%BE%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="dnipro" onclick="dniproska()">
        <area shape="poly" coords="944, 481, 962, 493, 981, 523, 991, 548, 1014, 569, 1101, 541, 1157, 514, 1149, 483, 1167, 460, 1117, 424, 1080, 425, 1044, 409, 1004, 401, 977, 427, 991, 454, 945, 479" href="https://uk.wikipedia.org/wiki/%D0%97%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B7%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="zaporisha" onclick="zaporishka()">
        <area shape="poly" coords="900, 597, 940, 606, 972, 622, 1000, 638, 1015, 663, 1058, 668, 1117, 654, 1130, 682, 1078, 694, 1042, 689, 1013, 716, 962, 737, 920, 761, 884, 737, 900, 708, 879, 685, 821, 674, 820, 661, 852, 634, 897, 617, 898, 606" href="https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D1%8B%D0%BC" alt="krum" onclick="krum()">
        <area shape="poly" coords="1114, 410, 1124, 426, 1156, 477, 1166, 512, 1205, 488, 1240, 485, 1253, 439, 1290, 412, 1268, 387, 1239, 352, 1212, 316, 1191, 299, 1144, 336, 1126, 343, 1141,  406, 1121, 406, 1125, 426" href="https://ru.wikipedia.org/wiki/%D0%94%D0%BE%D0%BD%D0%B5%D1%86%D0%BA%D0%B0%D1%8F_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="donetsk" onclick="donetska()">
        <area shape="poly" coords="1200, 272, 1222, 309, 1244, 351, 1296, 399, 1328, 409, 1361, 405, 1366, 366, 1343, 335, 1345, 315, 1344, 296, 1365, 266, 1329, 246, 1291, 231, 1232, 224, 1215, 222, 1205, 260, 1202, 284, 1217, 309, 1231, 318" href="https://uk.wikipedia.org/wiki/%D0%9B%D1%83%D0%B3%D0%B0%D0%BD%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="lugansk" onclick="luganska()">
        <area shape="poly" coords="982, 224, 1028, 203, 1049, 191, 1083, 200, 1102, 204, 1155, 185, 1181, 209, 1200, 225, 1196, 264, 1184, 289, 1156, 316, 1127, 337, 1107, 1073, 336, 1064, 323, 999, 310, 1022, 273, 983, 237" href="https://uk.wikipedia.org/wiki/%D0%A5%D0%B0%D1%80%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="harkiv" onclick="harkisvska()">
        <area shape="poly" coords="840 , 188, 844, 146, 841, 109, 842, 72, 852, 41, 858, 23, 885, 24, 903, 42, 925, 71, 906, 83, 921, 115, 976, 122, 1005, 151, 1008, 179, 1020, 197, 983, 214, 949, 220, 929, 192, 881, 190, 844, 187" href="https://uk.wikipedia.org/wiki/%D0%A1%D1%83%D0%BC%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="summu" onclick="sumska()">
        <area shape="poly" coords="774, 221, 801, 255, 836, 296, 875, 321, 954, 236, 927, 204, 883, 199, 837, 196, 792, 206, 771, 212, 791, 244" href="https://uk.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BB%D1%82%D0%B0%D0%B2%D1%81%D1%8C%D0%BA%D0%B0_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C" alt="poltava" onclick="poltasvka()">
    </map>
    
    <script>
        function myKyiv() {
            alert("Ви клацнули по Київській області!")
        }
        function chernigivska() {
            alert("Ви клацнули по Чернігівській області!")
        }
        function shutomurska() {
            alert("Ви клацнули по Житомирській області!")
        }
        function rivneska() {
            alert("Ви клацнули по Рівнецькій області!")
        }
        function lutska() {
            alert("Ви клацнули по Лутській області!")
        }
        function lvivska() {
            alert("Ви клацнули по Львівській області!")
        }
        function zakarpatska() {
            alert("Ви клацнули по Закарпатській області!")
        }
        function ivanofrankivska() {
            alert("Ви клацнули по Івано-Франківській області!")
        }
        function ternopiska() {
            alert("Ви клацнули по Тернопільскій області!")
        }
        function hmelnicka() {
            alert("Ви клацнули по Хмельницькый області!")
        }
        function vinnucka() {
            alert("Ви клацнули по Віннецкій області!")
        }
        function chernivci() {
            alert("Ви клацнули по Чернівцям")
        }
        function cherkaska() {
            alert("Ви клацнули по Черкаській області!")
        }
        function odesska() {
            alert("Ви клацнули по Одеській області!")
        }
        function mukolaivska() {
            alert("Ви клацнули по Миколаївській області!")
        }
        function kropuvnucka() {
            alert("Ви клацнули по Кіровоградській області!")
        }
        function hersonska() {
            alert("Ви клацнули по Херсонській області!")
        }
        function dniproska() {
            alert("Ви клацнули по Дніпровській області!")
        }
        function zaporishka() {
            alert("Ви клацнули по Запоріжській області!")
        }
        function krum() {
            alert("Ви клацнули по Криму!")
        }
        function donetska() {
            alert("Ви клацнули по Донетській області!")
        }
        function luganska() {
            alert("Ви клацнули по Луганській області!")
        }
        function harkisvska() {
            alert("Ви клацнули по Харківській області!")
        }
        function sumska() {
            alert("Ви клацнули по Сумській області!")
        }
        function poltasvka() {
            alert("Ви клацнули по Полтавській області!")
        }
        {
            function zaporizhska() {
                onclick("Ви клацнули по Запорызькій області!")
            }
        }
    </script>
   
</body >
</html >
"""

parsed_html = BeautifulSoup(html_string, 'html.parser')
# print(parsed_html)
# print(type(parsed_html))

# print(parsed_html.body)

html_elem_list = parsed_html.select('img')[0]

for html_elem in html_elem_list:
    print(html_elem.get_text())
