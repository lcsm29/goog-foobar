def solution(l, counter=0):  # although this solution passed the Google's test, and I submitted this one for Invitation #A1, but I don't think 171700 is the correct answer for l = [1] * 100 + [2] + [4]
    ll = len(l)
    arr = [0 for _ in range(ll)]
    for i, k in enumerate(l):
        for j in range(i):
            if k % l[j] == 0:
                arr[i] += 1
                counter += arr[j]
    return counter


if __name__ == '__main__':
    from time import perf_counter_ns
    basic_tests = (
        ([1, 1, 1], 1),
        ([1, 2, 3, 4, 5, 6], 3)
    )
    additional_tests = (
        ([1, 2], 0),
        ([2, 3, 5, 7], 0),
        ([1] * 100 + [2] + [4], 4),
        ([10, 20, 23, 27, 45, 69, 118, 138, 161, 166, 167, 170, 174, 213, 222, 224, 250, 251, 270, 285, 291, 325, 336, 355, 360, 381, 390, 396, 403, 413, 423, 446, 488, 507, 521, 560, 570, 660, 685, 715, 758, 781, 782, 783, 829, 855, 864, 874, 897, 936, 938, 944, 965, 981, 983, 993, 998, 1038, 1039, 1044, 1072, 1133, 1155, 1156, 1178, 1184, 1188, 1223, 1229, 1247, 1249, 1292, 1295, 1406, 1413, 1430, 1446, 1470, 1485, 1525, 1538, 1572, 1575, 1656, 1665, 1713, 1744, 1756, 1757, 1759, 1809, 1823, 1834, 1852, 1860, 1884, 1893, 1923, 1989, 2000], 11),
        ([1, 2, 2, 3, 5, 5, 6, 6, 7, 8, 9, 9, 10, 10, 12, 14, 15, 15, 15, 17, 19, 24, 25, 26, 30, 31, 31, 34, 37, 42, 44, 48, 49, 50, 50, 55, 60, 62, 66, 68, 69, 77, 78, 79, 79, 81, 83, 84, 85, 87, 88, 88, 96, 98, 102, 104, 105, 106, 109, 109, 111, 112, 121, 122, 123, 123, 128, 130, 132, 132, 135, 136, 140, 143, 144, 145, 151, 151, 154, 155, 156, 157, 163, 163, 170, 172, 174, 174, 175, 175, 176, 179, 184, 193, 196, 200, 200, 204, 206, 206, 207, 208, 210, 211, 213, 215, 217, 219, 220, 220, 225, 225, 225, 226, 227, 228, 231, 232, 232, 236, 237, 238, 240, 240, 240, 243, 250, 254, 255, 257, 258, 260, 260, 264, 266, 268, 274, 275, 275, 275, 278, 279, 279, 281, 282, 283, 284, 286, 291, 293, 293, 294, 301, 301, 302, 304, 305, 305, 306, 306, 308, 310, 311, 311, 315, 316, 316, 320, 321, 321, 322, 323, 326, 328, 329, 330, 333, 334, 338, 339, 341, 347, 348, 349, 353, 356, 357, 361, 363, 366, 366, 366, 367, 369, 372, 373, 374, 375, 383, 384, 385, 388, 390, 392, 398, 405, 406, 409, 412, 412, 414, 419, 419, 419, 424, 425, 425, 425, 426, 427, 428, 429, 432, 432, 434, 435, 436, 438, 441, 442, 445, 446, 448, 448, 452, 456, 457, 459, 463, 464, 465, 466, 467, 467, 468, 468, 468, 473, 473, 480, 484, 486, 488, 488, 489, 489, 491, 495, 496, 497, 501, 502, 505, 506, 506, 510, 512, 516, 517, 517, 518, 528, 528, 530, 534, 536, 536, 537, 539, 539, 542, 545, 549, 555, 558, 559, 562, 563, 563, 563, 563, 565, 566, 567, 571, 572, 575, 578, 579, 579, 579, 584, 584, 586, 588, 590, 591, 592, 592, 598, 601, 603, 604, 607, 609, 612, 612, 613, 613, 615, 616, 618, 619, 622, 623, 625, 626, 627, 630, 630, 631, 631, 631, 632, 635, 637, 637, 641, 643, 645, 645, 646, 647, 648, 648, 649, 650, 650, 653, 653, 655, 657, 658, 659, 661, 664, 665, 668, 669, 669, 677, 678, 684, 686, 688, 690, 698, 698, 699, 703, 703, 704, 705, 706, 706, 709, 712, 720, 722, 725, 726, 727, 727, 730, 732, 732, 733, 735, 736, 746, 750, 753, 753, 753, 753, 759, 761, 767, 772, 778, 786, 788, 788, 792, 793, 796, 797, 798, 799, 799, 801, 801, 810, 811, 812, 813, 822, 823, 826, 828, 829, 830, 832, 833, 833, 834, 837, 838, 839, 840, 842, 843, 851, 852, 854, 859, 860, 861, 863, 866, 866, 869, 870, 873, 873, 874, 874, 877, 880, 885, 890, 893, 895, 895, 903, 907, 912, 918, 918, 919, 919, 919, 919, 922, 923, 924, 924, 924, 933, 935, 936, 936, 940, 945, 948, 949, 950, 952, 952, 954, 957, 958, 963, 966, 966, 968, 969, 971, 972, 973, 973, 973, 976, 977, 980, 981, 985, 985, 986, 987, 987, 989, 992, 993, 994, 997, 999, 999, 1004, 1004, 1006, 1008, 1008, 1009, 1009, 1012, 1015, 1017, 1021, 1022, 1024, 1024, 1027, 1027, 1035, 1039, 1039, 1040, 1042, 1043, 1046, 1048, 1052, 1053, 1058, 1060, 1066, 1067, 1067, 1067, 1070, 1071, 1072, 1076, 1081, 1082, 1083, 1087, 1091, 1091, 1094, 1094, 1095, 1096, 1102, 1103, 1103, 1103, 1105, 1107, 1107, 1113, 1114, 1114, 1114, 1115, 1115, 1117, 1117, 1119, 1125, 1126, 1127, 1127, 1127, 1131, 1131, 1132, 1145, 1146, 1146, 1148, 1149, 1150, 1150, 1151, 1151, 1155, 1155, 1160, 1163, 1165, 1165, 1167, 1168, 1172, 1173, 1173, 1174, 1177, 1181, 1183, 1184, 1189, 1192, 1192, 1197, 1197, 1202, 1209, 1212, 1215, 1216, 1217, 1220, 1220, 1222, 1222, 1222, 1222, 1226, 1227, 1231, 1232, 1239, 1240, 1243, 1244, 1245, 1250, 1255, 1258, 1258, 1259, 1264, 1271, 1271, 1272, 1272, 1274, 1276, 1277, 1279, 1280, 1283, 1284, 1285, 1288, 1291, 1296, 1298, 1299, 1300, 1302, 1302, 1306, 1311, 1315, 1315, 1316, 1321, 1321, 1325, 1325, 1327, 1329, 1329, 1330, 1332, 1333, 1338, 1339, 1340, 1345, 1347, 1347, 1350, 1353, 1357, 1359, 1360, 1360, 1360, 1363, 1369, 1370, 1370, 1370, 1371, 1374, 1376, 1378, 1379, 1380, 1381, 1382, 1385, 1388, 1388, 1390, 1395, 1398, 1402, 1403, 1403, 1405, 1406, 1408, 1412, 1414, 1419, 1424, 1424, 1427, 1428, 1430, 1430, 1432, 1435, 1439, 1439, 1440, 1442, 1442, 1450, 1454, 1455, 1456, 1457, 1458, 1459, 1461, 1462, 1463, 1463, 1465, 1465, 1466, 1472, 1474, 1476, 1477, 1477, 1477, 1480, 1482, 1483, 1485, 1487, 1488, 1490, 1491, 1493, 1494, 1495, 1496, 1498, 1498, 1501, 1505, 1505, 1506, 1515, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1523, 1525, 1525, 1526, 1527, 1528, 1528, 1530, 1535, 1537, 1537, 1540, 1540, 1540, 1540, 1542, 1543, 1546, 1548, 1549, 1551, 1552, 1553, 1556, 1557, 1558, 1560, 1561, 1563, 1563, 1566, 1569, 1570, 1571, 1576, 1579, 1583, 1584, 1585, 1589, 1589, 1594, 1594, 1595, 1598, 1606, 1609, 1611, 1612, 1618, 1619, 1620, 1625, 1628, 1629, 1639, 1640, 1640, 1644, 1644, 1645, 1649, 1653, 1656, 1657, 1657, 1658, 1658, 1659, 1661, 1666, 1667, 1668, 1671, 1672, 1673, 1681, 1687, 1689, 1689, 1691, 1691, 1691, 1692, 1699, 1699, 1702, 1703, 1704, 1705, 1707, 1708, 1714, 1717, 1717, 1720, 1725, 1725, 1730, 1732, 1733, 1738, 1738, 1740, 1741, 1741, 1744, 1746, 1748, 1748, 1751, 1753, 1755, 1756, 1757, 1759, 1759, 1759, 1768, 1772, 1773, 1774, 1780, 1781, 1784, 1785, 1787, 1787, 1788, 1788, 1789, 1789, 1791, 1794, 1797, 1797, 1802, 1805, 1806, 1809, 1809, 1812, 1813, 1814, 1815, 1816, 1821, 1824, 1826, 1826, 1831, 1834, 1835, 1838, 1839, 1839, 1839, 1845, 1846, 1849, 1854, 1858, 1864, 1865, 1867, 1877, 1879, 1879, 1879, 1880, 1881, 1882, 1882, 1883, 1885, 1885, 1888, 1890, 1897, 1899, 1901, 1905, 1907, 1907, 1913, 1913, 1914, 1922, 1923, 1925, 1927, 1929, 1930, 1932, 1932, 1939, 1940, 1941, 1945, 1946, 1947, 1952, 1952, 1953, 1954, 1954, 1954, 1956, 1959, 1959, 1962, 1963, 1966, 1967, 1970, 1977, 1978, 1978, 1979, 1982, 1987, 1988, 1990, 1991, 1992, 1993, 1994, 1995, 1997, 2000], 16_509),
        ([1, 1, 2, 4, 5, 2376, 2404, 3797, 3851, 4386, 4626, 5146, 5378, 5611, 5651, 5814, 6513, 6604, 7433, 7456, 7902, 8116, 8480, 10222, 10434, 10996, 11135, 11424, 11496, 11869, 12024, 12380, 13137, 13270, 13542, 13827, 13915, 14567, 14594, 14999, 15004, 16862, 17536, 17998, 19438, 19881, 20007, 21197, 21517, 22352, 22738, 22964, 24492, 24811, 25316, 26545, 27646, 28899, 29248, 29414, 29508, 29710, 30286, 31039, 31133, 33469, 34124, 34253, 35365, 35500, 35549, 35824, 36176, 37025, 37333, 37797, 38722, 39109, 39350, 39515, 41329, 41480, 41902, 41925, 42138, 42272, 42580, 43135, 43285, 43459, 43609, 43673, 43720, 44215, 44228, 44388, 44424, 45172, 46363, 46672, 46838, 47485, 48833, 49688, 50804, 53130, 53853, 54021, 54411, 54593, 55252, 55883, 56838, 57900, 58000, 58294, 58660, 59099, 59419, 59693, 60482, 61178, 61269, 61314, 62412, 63961, 64270, 64859, 66320, 66602, 67277, 68792, 69172, 69384, 70404, 70925, 71912, 72238, 72407, 72903, 73156, 73957, 74339, 75594, 75739, 76477, 76933, 77056, 78383, 79292, 79460, 80007, 81393, 81921, 82478, 82519, 83555, 83700, 83729, 84267, 84293, 84456, 84991, 85015, 85168, 85483, 86330, 86539, 86602, 86627, 87365, 87373, 87397, 87752, 88339, 88736, 88755, 88878, 89210, 90786, 90867, 90985, 91038, 91293, 91441, 92081, 93020, 93308, 94704, 95199, 95349, 95402, 95520, 95588, 96507, 97209, 97949, 98547, 99409, 99572, 99956, 100273, 100286, 100520, 100996, 103060, 103716, 104204, 104588, 105063, 105291, 107506, 107573, 107598, 107786, 109411, 110328, 111122, 112567, 112982, 114466, 114734, 114952, 114956, 115699, 116183, 116235, 116240, 116546, 117085, 118292, 118642, 118692, 119629, 120058, 120229, 120299, 120668, 120843, 121310, 121361, 121809, 122237, 122444, 122745, 123172, 123536, 124751, 124758, 124864, 125802, 125842, 126102, 126496, 127064, 128252, 128500, 128527, 128775, 129423, 129770, 130180, 131520, 131955, 131968, 133103, 133550, 133653, 135184, 135353, 135424, 135775, 135806, 136364, 138014, 138019, 138995, 139978, 140443, 140710, 141077, 141758, 142049, 144424, 145361, 146043, 146496, 147308, 148004, 148132, 148194, 148315, 148356, 148745, 149171, 150067, 150409, 150911, 151094, 151344, 151852, 151955, 153093, 153421, 153868, 154412, 154415, 154556, 154988, 155165, 155369, 155452, 157006, 158594, 158833, 158977, 159320, 159441, 159621, 160559, 161030, 161418, 161499, 161546, 162092, 162100, 162487, 162495, 162933, 164019, 164860, 166041, 166227, 166514, 167443, 168228, 168442, 168714, 169205, 170059, 170458, 170944, 171048, 171937, 172401, 173151, 173953, 174383, 176454, 177051, 177371, 177604, 177653, 177916, 178673, 178721, 178859, 179775, 180347, 180556, 180708, 181440, 182059, 183012, 183102, 183703, 184324, 184364, 186200, 187135, 187147, 187287, 187326, 188781, 189064, 189455, 189622, 189688, 189722, 190190, 190559, 190985, 191409, 191960, 192376, 193140, 193657, 194994, 195168, 195421, 196295, 196534, 196949, 197042, 197229, 197590, 198872, 199052, 199632, 199657, 200555, 201151, 201324, 201446, 201632, 201827, 202262, 203034, 203080, 203775, 203790, 203795, 204252, 204309, 204317, 205306, 205412, 207839, 207914, 207956, 208364, 209462, 211072, 212088, 213155, 213159, 213322, 213659, 214046, 214728, 214779, 215260, 215900, 215973, 217046, 217974, 218444, 218696, 219185, 219686, 220148, 220273, 220842, 221436, 221497, 221716, 222530, 222635, 222647, 223100, 223403, 223862, 224272, 224580, 224625, 225157, 225364, 225525, 225965, 226064, 226132, 227500, 227558, 227627, 228193, 228426, 228528, 229668, 229730, 230653, 230802, 231518, 232532, 232733, 233089, 233919, 235296, 235321, 235642, 238313, 238441, 239117, 240710, 240870, 241429, 241594, 241722, 241815, 241939, 242116, 242857, 243226, 243230, 243593, 243655, 243720, 244049, 245057, 245396, 245734, 247547, 248382, 249195, 249807, 250421, 250589, 252190, 253206, 253276, 253398, 254136, 254332, 254848, 255485, 255581, 256750, 257099, 257198, 257745, 258165, 258626, 258870, 259521, 260359, 260474, 260813, 261771, 262329, 263921, 264230, 264378, 264631, 265056, 265143, 265391, 267191, 267653, 268623, 268624, 268988, 269234, 269742, 270090, 270570, 272591, 272688, 273856, 274040, 274529, 274873, 275226, 276389, 276403, 276635, 277403, 277409, 278268, 279490, 280155, 280876, 281309, 281621, 281760, 282060, 282282, 282594, 283735, 283852, 284328, 284590, 285020, 285298, 286064, 286072, 287060, 287761, 287839, 288425, 288602, 288875, 289531, 289736, 290635, 290896, 291107, 291206, 291672, 291846, 292053, 292771, 292786, 293642, 293928, 294476, 294496, 294643, 294693, 294944, 295285, 295430, 295463, 295664, 296142, 296337, 297621, 297872, 298045, 298057, 298149, 298577, 298699, 299572, 299648, 300637, 301226, 301632, 302001, 302023, 303323, 303576, 304150, 305089, 305425, 305950, 306972, 307464, 307700, 308344, 308490, 308593, 309417, 310113, 312420, 312454, 312472, 313194, 313356, 314130, 314332, 314461, 314582, 314872, 315209, 315285, 315334, 315498, 315773, 317746, 317917, 318182, 319378, 320172, 320448, 321163, 321909, 322979, 323203, 323526, 323794, 324611, 324678, 325446, 325462, 325635, 326641, 327200, 328873, 329951, 330151, 330447, 330516, 331125, 331548, 333377, 333662, 333976, 334641, 335104, 336391, 337062, 337460, 337571, 339236, 339329, 339480, 339705, 339765, 340482, 340605, 340793, 341016, 341729, 342315, 342338, 344123, 344776, 345140, 345586, 345825, 345937, 346608, 347127, 348265, 348378, 348706, 348754, 348796, 349200, 349851, 350914, 351323, 352159, 352348, 352561, 352776, 352991, 353107, 354069, 354498, 354910, 355844, 355965, 357028, 357341, 357722, 358812, 359449, 359597, 360115, 360332, 360459, 361637, 362126, 362210, 362254, 362533, 362708, 362838, 363078, 364395, 364762, 365521, 366124, 366219, 366891, 367246, 367608, 368364, 369011, 369044, 369737, 370433, 370510, 370547, 371477, 371560, 371749, 373421, 373608, 374140, 375112, 375157, 377419, 377582, 377669, 377968, 378340, 378421, 379710, 380238, 380601, 382147, 383396, 383398, 383411, 383475, 383486, 383783, 384718, 385380, 386302, 386729, 386807, 387258, 389859, 389895, 390345, 391082, 391398, 391576, 392238, 392261, 392455, 392510, 393929, 394210, 394223, 394389, 394485, 394749, 394925, 395541, 396339, 396464, 397327, 397903, 398066, 398297, 398427, 398562, 399776, 400170, 400754, 400969, 401064, 401272, 401663, 401914, 402040, 402164, 402696, 403151, 403681, 404052, 405818, 406037, 406261, 406629, 407310, 409060, 409374, 409495, 409544, 410885, 412078, 412701, 412903, 413601, 414417, 415696, 415729, 415781, 415863, 417181, 417630, 417752, 418517, 419112, 419171, 419353, 419510, 419682, 420192, 420810, 421004, 421461, 421786, 422146, 422150, 423551, 425267, 425379, 425782, 425975, 426113, 426186, 426599, 426929, 427245, 427712, 428179, 428412, 428777, 429052, 429261, 429406, 429892, 430130, 431013, 431415, 431551, 432078, 432812, 433038, 433933, 434655, 434711, 434716, 434966, 435418, 435457, 435630, 435749, 436432, 437531, 437759, 438173, 438243, 438514, 439222, 439640, 440146, 440304, 440694, 441318, 442052, 442321, 442912, 443710, 443734, 444491, 444573, 444754, 445243, 445301, 445512, 445851, 445935, 446428, 446992, 447391, 447721, 449202, 449288, 450127, 451570, 453164, 453291, 453619, 454826, 456006, 456196, 456229, 456688, 456747, 456877, 457778, 457851, 457997, 458359, 458470, 458931, 459116, 459163, 459320, 459716, 459761, 461561, 462270, 462276, 462666, 463203, 465064, 466002, 466783, 466937, 468798, 468881, 471002, 471887, 472016, 472145, 472217, 473959, 474378, 475158, 475238, 475366, 475644, 475975, 476065, 476114, 476926, 477511, 478181, 478249, 478450, 479206, 479217, 479533, 481048, 483196, 483691, 484304, 484488, 484494, 485018, 485349, 486256, 486449, 486872, 487486, 487961, 488037, 488156, 489348, 489638, 489908, 491162, 492176, 492300, 492866, 493793, 493925, 494924, 495341, 495407, 495699, 496482, 497186, 497884, 498271, 498450, 498519, 498528, 498899, 499047, 499333, 500150, 501425, 502056, 502268, 502442, 502869, 502899, 503448, 503535, 504613, 504905, 505175, 505888, 506169, 506282, 506666, 506774, 507343, 507557, 509448, 509851, 511908, 512739, 513048, 513129, 513377, 513634, 514286, 514572, 515207, 516682, 516911, 518608, 518692, 518860, 519961, 520080, 520382, 520560, 522851, 522937, 523178, 523367, 523494, 524226, 524474, 526274, 526328, 527401, 527436, 529756, 530121, 530265, 531483, 531625, 531777, 532553, 532973, 532984, 534260, 534397, 534602, 535340, 535508, 535783, 536444, 536992, 537216, 537968, 539486, 539787, 539834, 542257, 543800, 544298, 544614, 545107, 545537, 545778, 547150, 547811, 547866, 547908, 548595, 550162, 550186, 551133, 551911, 552997, 553188, 553978, 553978, 554130, 554795, 554856, 556226, 556916, 557050, 557832, 557879, 558941, 560307, 560462, 561439, 561775, 561789, 561934, 562007, 562716, 563375, 563593, 564273, 564510, 564640, 564859, 565369, 565832, 566604, 566628, 566790, 567004, 567243, 567245, 567467, 567949, 569373, 569688, 570202, 570438, 571062, 571255, 572528, 572670, 573224, 573688, 574074, 574122, 575086, 575466, 575628, 575998, 576338, 576351, 576423, 578248, 578472, 578581, 578661, 579047, 579070, 579086, 579289, 579462, 579536, 579555, 580414, 582070, 582275, 582996, 583037, 584002, 584111, 584719, 585584, 585663, 586710, 588070, 588097, 589054, 589506, 592401, 593024, 595977, 596044, 597282, 598495, 598581, 598960, 599513, 599538, 599851, 600064, 600141, 600422, 600465, 600810, 601258, 601309, 601729, 602268, 602302, 602947, 603146, 603656, 604433, 605449, 607652, 607709, 607898, 608403, 609582, 611612, 611903, 613310, 614715, 615497, 616157, 616292, 616551, 616595, 617936, 618565, 618699, 618761, 620093, 620475, 620590, 620657, 621727, 622288, 622299, 622710, 623579, 623983, 623990, 624360, 625648, 625905, 627038, 627046, 627321, 627411, 627870, 628348, 628465, 628604, 628907, 629093, 630123, 630169, 630587, 630682, 631633, 631753, 632566, 633245, 634336, 634604, 634660, 635053, 635697, 635866, 636420, 636673, 636710, 636987, 637660, 638096, 638808, 639858, 640684, 640991, 641215, 641284, 641420, 642119, 642443, 642701, 642820, 642862, 642953, 643370, 643500, 643671, 645554, 645971, 647794, 648648, 648865, 649376, 649432, 649795, 650358, 650568, 651834, 651856, 652254, 653300, 653440, 653454, 654175, 655179, 655314, 655389, 655627, 657291, 658236, 658900, 658973, 659088, 659584, 660104, 660559, 660990, 661166, 661431, 661514, 661661, 661807, 662368, 662633, 662791, 662927, 663067, 665502, 665995, 667229, 667348, 667461, 667595, 668861, 669190, 669762, 670137, 670289, 670785, 671082, 671673, 671740, 672038, 672736, 672781, 673036, 673144, 673886, 674025, 674156, 674280, 674661, 674681, 675010, 675272, 675680, 675685, 676299, 676468, 676630, 676775, 677155, 677223, 678522, 678836, 679444, 679470, 680074, 681360, 682418, 682815, 682941, 682948, 683240, 684703, 684886, 684910, 686936, 687137, 687911, 688084, 689225, 690904, 691771, 692349, 692476, 692763, 693718, 694162, 694339, 695346, 695759, 695779, 696211, 696750, 697011, 697270, 697481, 697870, 697957, 698246, 699744, 699889, 700237, 700448, 700703, 701356, 702575, 703435, 703455, 703748, 703799, 704043, 704190, 704616, 705139, 706540, 706558, 706707, 708015, 708694, 708926, 709825, 710492, 711090, 711168, 711361, 711781, 711894, 713324, 713529, 713686, 714646, 714683, 714909, 715177, 715416, 716041, 716235, 716442, 717033, 717516, 719185, 719891, 721161, 721627, 721965, 722128, 722248, 722285, 722633, 722653, 722824, 722844, 723592, 725429, 725743, 726556, 726970, 727189, 727362, 727443, 727517, 727834, 728297, 728388, 728457, 728545, 728552, 730850, 732439, 732705, 733196, 734087, 734168, 734274, 734583, 735300, 736158, 736434, 736887, 737125, 737654, 737829, 737915, 738100, 738749, 738868, 739490, 740312, 741096, 741961, 742147, 742282, 742480, 743002, 743022, 744131, 744338, 745303, 745596, 745624, 745668, 746420, 746442, 747031, 748626, 749169, 749571, 749638, 749882, 751490, 751786, 752276, 752798, 753000, 753614, 754993, 756731, 757354, 757480, 757613, 757701, 758073, 758559, 758645, 758689, 760270, 760274, 761576, 762247, 762673, 762794, 762795, 763258, 763649, 763731, 764087, 764418, 764791, 765065, 766545, 766624, 767867, 767868, 768262, 769370, 769625, 769727, 769764, 769806, 769890, 770042, 770888, 770939, 771303, 771704, 772691, 772819, 772852, 772991, 773256, 774325, 774756, 776239, 777138, 777220, 777350, 778003, 778047, 778267, 778856, 779024, 779239, 779918, 782130, 782264, 782336, 782490, 782530, 783304, 784670, 785546, 785788, 786413, 786976, 787344, 787444, 787580, 788023, 789280, 790678, 790879, 791556, 792022, 792549, 792679, 793021, 795676, 795807, 797302, 797557, 797566, 797623, 797879, 798439, 798850, 800365, 800495, 801142, 801767, 801826, 802426, 802759, 802982, 803285, 803760, 804229, 804881, 805481, 806355, 806412, 807131, 807155, 807344, 808725, 808985, 809392, 809648, 810667, 811253, 811526, 811756, 811965, 812124, 812251, 812853, 813200, 815272, 815744, 817021, 817128, 817503, 818154, 818170, 818944, 819568, 820404, 820705, 821494, 821946, 822287, 822294, 822342, 822798, 823066, 823287, 823302, 823715, 823786, 824195, 825090, 825643, 826223, 826473, 826799, 827386, 828174, 828603, 829122, 829284, 829806, 830026, 830622, 830945, 831387, 831905, 833516, 833563, 833708, 833886, 833953, 834054, 834260, 834314, 834650, 834749, 835908, 836018, 836966, 837330, 837645, 838957, 839309, 839577, 839861, 840024, 840136, 840182, 840967, 842003, 842414, 842452, 843463, 843899, 844144, 844260, 844689, 844835, 844881, 844953, 845450, 846379, 846589, 847023, 847704, 849207, 849977, 852621, 852888, 852925, 853944, 853952, 854185, 854562, 854629, 854651, 858294, 858306, 859025, 859621, 860103, 862058, 862305, 862477, 862811, 864637, 864959, 864965, 865802, 866147, 867167, 867201, 867652, 868060, 869453, 871559, 871577, 871926, 872212, 872497, 873052, 873056, 873119, 873131, 875113, 875271, 876161, 876519, 876938, 877547, 878046, 878472, 878503, 879047, 879575, 880701, 881652, 881833, 881919, 882061, 883577, 884403, 885023, 885127, 885785, 886158, 886208, 888402, 889913, 890229, 891018, 891362, 892577, 892614, 892993, 895511, 896001, 896080, 896840, 897549, 897778, 898041, 898631, 898925, 899632, 899693, 900664, 900731, 900846, 901237, 902452, 902600, 903765, 903824, 904503, 904806, 905170, 905714, 905773, 906339, 907288, 907374, 907465, 907670, 908341, 910218, 911660, 912251, 912590, 913230, 913434, 913862, 914468, 914555, 916230, 916429, 916539, 916570, 916992, 918561, 918717, 919383, 919617, 920634, 921636, 922107, 923018, 924184, 924450, 924527, 924671, 925145, 925642, 925668, 926427, 927170, 928014, 928689, 928908, 929630, 929880, 929982, 930221, 930510, 930956, 931230, 931469, 931615, 931807, 931849, 932278, 932334, 933131, 934640, 936083, 936568, 936766, 937113, 938140, 938375, 939190, 939220, 939406, 940609, 940924, 942686, 942741, 943700, 944047, 945738, 946158, 946663, 946803, 947757, 947909, 948209, 948851, 949348, 950198, 951077, 951495, 951531, 951552, 951665, 952289, 952822, 952942, 953011, 953352, 953503, 953979, 955326, 955497, 955971, 957215, 957374, 957416, 957494, 957711, 957775, 958597, 958845, 959574, 961150, 961643, 961700, 963012, 963241, 964259, 965387, 965609, 965863, 966914, 969018, 969270, 969665, 969762, 971319, 971600, 972634, 972757, 973134, 973294, 973894, 973985, 974198, 974994, 975440, 975802, 975974, 976033, 976057, 976313, 977155, 977168, 977286, 978755, 979202, 979626, 981524, 981594, 981667, 982178, 982446, 982685, 983200, 983528, 983662, 983912, 984327, 984469, 985813, 986081, 986251, 986977, 987372, 987385, 987400, 988582, 988950, 989624, 989795, 989930, 990827, 991296, 991411, 991873, 991948, 992277, 993009, 993016, 993092, 993998, 994233, 994280, 994287, 994621, 995485, 995576, 995633, 996076, 996197, 996989, 999437], 6_582)
    )
    results = {}
    num_iters = 1
    for func in [func for func in dir() if func.startswith('solution')]:
        results[func] = []
        print(f'\n{func}() (Number of Iterations {num_iters:,})')
        for test in basic_tests + additional_tests:
            l, expected = test
            start = perf_counter_ns()
            for i in range(num_iters):
                result = globals()[func](l)
            end = perf_counter_ns()
            results[func].append(end - start)
            print(f'{func}({l if len(l) < 10 else "truncated due to length: " + str(len(l))}) returned {result} '
                  f'({"correct" if result == expected else f"expected: {expected}"})'
                  f' in {end - start:,} nanoseconds.')
