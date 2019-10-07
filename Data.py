types = {0: 'Normal', 1: 'Fighting', 2: 'Flying', 3: 'Poison', 4: 'Ground', 5: 'Rock', 6: 'Bug', 7: 'Ghost', 8: 'Steel',
         9: '???', 10: 'Fire', 11: 'Water', 12: 'Grass', 13: 'Electric', 14: 'Psychic', 15: 'Ice', 16: 'Dragon',
         17: 'Dark', 18: "Fairy"}

natures = {'Adamant': [1.1, 1, 0.9, 1, 1], 'Brave': [1.1, 1, 1, 1, 0.9], 'Lonely': [1.1, 0.9, 1, 1, 1],
           'Naughty': [1.1, 1, 1, 0.9, 1], 'Bold': [0.9, 1.1, 1, 1, 1], 'Lax': [1, 1.1, 1, 0.9, 1],
           'Relaxed': [1, 1.1, 1, 1, 0.9], 'Impish': [1, 1.1, 0.9, 1, 1], 'Timid': [0.9, 1, 1, 1, 1.1],
           'Hasty': [1, 0.9, 1, 1, 1.1], 'Jolly': [1, 1, 0.9, 1, 1.1], 'Naive': [1, 1, 1, 0.9, 1.1],
           'Mild': [1, 0.9, 1.1, 1, 1], 'Quiet': [1, 1, 1.1, 1, 0.9], 'Rash': [1, 1, 1.1, 0.9, 1],
           'Modest': [0.9, 1, 1.1, 1, 1], 'Gentle': [1, 0.9, 1, 1.1, 1], 'Calm': [0.9, 1, 1, 1.1, 1],
           'Sassy': [1, 1, 1, 1.1, 0.9], 'Careful': [1, 1, 0.9, 1.1, 1], 'Hardy': [1, 1, 1, 1, 1],
           'Docile': [1, 1, 1, 1, 1], 'Serious': [1, 1, 1, 1, 1], 'Bashful': [1, 1, 1, 1, 1], 'Quirky': [1, 1, 1, 1, 1]}

typechart= [[10, 10, 10, 10, 10,  5, 10, 00,  5, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [20, 10,  5,  5, 10, 20,  5, 00, 20, 10, 10, 10, 10, 10,  5, 20, 10, 20,  5],
            [10, 10, 10, 10, 10,  5, 20, 10,  5, 10, 10, 10, 20,  5, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  5, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]

exptable = {1: [0, 0, 0, 0, 0, 0],
 2: [4, 10, 9, 8, 6, 15],
 3: [13, 33, 57, 27, 21, 52],
 4: [32, 80, 96, 64, 51, 122],
 5: [65, 156, 135, 125, 100, 237],
 6: [112, 270, 179, 216, 172, 406],
 7: [178, 428, 236, 343, 274, 637],
 8: [276, 640, 314, 512, 409, 942],
 9: [393, 911, 419, 729, 583, 1326],
 10: [1250, 560, 1000, 800, 1800],
 11: [745, 1663, 742, 1331, 1064, 2369],
 12: [967, 2160, 973, 1728, 1382, 3041],
 13: [1230, 2746, 1261, 2197, 1757, 3822],
 14: [1591, 3430, 1612, 2744, 2195, 4719],
 15: [1957, 4218, 2035, 3375, 2700, 5737],
 16: [2457, 5120, 2535, 4096, 3276, 6881],
 17: [3046, 6141, 3120, 4913, 3930, 8155],
 18: [3732, 7290, 3798, 5832, 4665, 9564],
 19: [4526, 8573, 4575, 6859, 5487, 11111],
 20: [5440, 10000, 5460, 8000, 6400, 12800],
 21: [6482, 11576, 6458, 9261, 7408, 14632],
 22: [7666, 13310, 7577, 10648, 8518, 16610],
 23: [9003, 15208, 8825, 12167, 9733, 18737],
 24: [10506, 17280, 10208, 13824, 11059, 21012],
 25: [12187, 19531, 11735, 15625, 12500, 23437],
 26: [14060, 21970, 13411, 17576, 14060, 26012],
 27: [16140, 24603, 15244, 19683, 15746, 28737],
 28: [18439, 27440, 17242, 21952, 17561, 31610],
 29: [20974, 30486, 19411, 24389, 19511, 34632],
 30: [23760, 33750, 21760, 27000, 21600, 37800],
 31: [26811, 37238, 24294, 29791, 23832, 41111],
 32: [30146, 40960, 27021, 32768, 26214, 44564],
 33: [33780, 44921, 29949, 35937, 28749, 48155],
 34: [37731, 49130, 33084, 39304, 31443, 51881],
 35: [42017, 53593, 36435, 42875, 34300, 55737],
 36: [46656, 58320, 40007, 46656, 37324, 59719],
 37: [50653, 63316, 43808, 50653, 40522, 63822],
 38: [55969, 68590, 47846, 54872, 43897, 68041],
 39: [60505, 74148, 52127, 59319, 47455, 72369],
 40: [66560, 80000, 56660, 64000, 51200, 76800],
 41: [71677, 86151, 61450, 68921, 55136, 81326],
 42: [78533, 92610, 66505, 74088, 59270, 85942],
 43: [84277, 99383, 71833, 79507, 63605, 90637],
 44: [91998, 106480, 77440, 85184, 68147, 95406],
 45: [98415, 113906, 83335, 91125, 72900, 100237],
 46: [107069, 121670, 89523, 97336, 77868, 105122],
 47: [114205, 129778, 96012, 103823, 83058, 110052],
 48: [123863, 138240, 102810, 110592, 88473, 115015],
 49: [131766, 147061, 109923, 117649, 94119, 120001],
 50: [142500, 156250, 117360, 125000, 100000, 125000],
 51: [151222, 165813, 125126, 132651, 106120, 131324],
 52: [163105, 175760, 133229, 140608, 112486, 137795],
 53: [172697, 186096, 141677, 148877, 119101, 144410],
 54: [185807, 196830, 150476, 157464, 125971, 151165],
 55: [196322, 207968, 159635, 166375, 133100, 158056],
 56: [210739, 219520, 169159, 175616, 140492, 165079],
 57: [222231, 231491, 179056, 185193, 148154, 172229],
 58: [238036, 243890, 189334, 195112, 156089, 179503],
 59: [250562, 256723, 199999, 205379, 164303, 186894],
 60: [267840, 270000, 211060, 216000, 172800, 194400],
 61: [281456, 283726, 222522, 226981, 181584, 202013],
 62: [300293, 297910, 234393, 238328, 190662, 209728],
 63: [315059, 312558, 246681, 250047, 200037, 217540],
 64: [335544, 327680, 259392, 262144, 209715, 225443],
 65: [351520, 343281, 272535, 274625, 219700, 233431],
 66: [373744, 359370, 286115, 287496, 229996, 241496],
 67: [390991, 375953, 300140, 300763, 240610, 249633],
 68: [415050, 393040, 314618, 314432, 251545, 257834],
 69: [433631, 410636, 329555, 328509, 262807, 267406],
 70: [459620, 428750, 344960, 343000, 274400, 276458],
 71: [479600, 447388, 360838, 357911, 286328, 286328],
 72: [507617, 466560, 377197, 373248, 298598, 296358],
 73: [529063, 486271, 394045, 389017, 311213, 305767],
 74: [559209, 506530, 411388, 405224, 324179, 316074],
 75: [582187, 527343, 429235, 421875, 337500, 326531],
 76: [614566, 548720, 447591, 438976, 351180, 336255],
 77: [639146, 570666, 466464, 456533, 365226, 346965],
 78: [673863, 593190, 485862, 474552, 379641, 357812],
 79: [700115, 616298, 505791, 493039, 394431, 367807],
 80: [737280, 640000, 526260, 512000, 409600, 378880],
 81: [765275, 664301, 547274, 531441, 425152, 390077],
 82: [804997, 689210, 568841, 551368, 441094, 400293],
 83: [834809, 714733, 590969, 571787, 457429, 411686],
 84: [877201, 740880, 613664, 592704, 474163, 423190],
 85: [908905, 767656, 636935, 614125, 491300, 433572],
 86: [954084, 795070, 660787, 636056, 508844, 445239],
 87: [987754, 823128, 685228, 658503, 526802, 457001],
 88: [1035837, 851840, 710266, 681472, 545177, 467489],
 89: [1071552, 881211, 735907, 704969, 563975, 479378],
 90: [1122660, 911250, 762160, 729000, 583200, 491346],
 91: [1160499, 941963, 789030, 753571, 602856, 501878],
 92: [1214753, 973360, 816525, 778688, 622950, 513934],
 93: [1254796, 1005446, 844653, 804357, 643485, 526049],
 94: [1312322, 1038230, 873420, 830584, 664467, 536557],
 95: [1354652, 1071718, 902835, 857375, 685900, 548720],
 96: [1415577, 1105920, 932903, 884736, 707788, 560922],
 97: [1460276, 1140841, 963632, 912673, 730138, 571333],
 98: [1524731, 1176490, 995030, 941192, 752953, 583539],
 99: [1571884, 1212873, 1027103, 970299, 776239, 591882],
 100: [1640000, 1250000, 1059860, 1000000, 800000, 600000]}
