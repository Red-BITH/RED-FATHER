import os
import requests
import time
print("""\033[0;37m
    ⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⡀⠄⡀⠄⡀⢀⠄⡀⢀⠄⡀⠄⡀⠄⠄⠄⠄⢀⠄⠄⡀⢀⠄⠄⡀⠄⠄⠄⠄
    ⠄⠄⠄⠈⠄⠁⠈⠄⠂⠄⡀⠄⠄⡀⢀⠄⢀⠄⢀⠄⡀⠠⠄⠄⠂⠁⠈⡀⠄⠄⠁⠄⠄⠄⠂⠄⡀⠁⠄⠄
    ⠄⠄⠄⠁⠄⠁⠄⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⡀⡀⠄⠄⠁⢀⢁⠄⡀⠠⠄⠁⡈⢀⠈⢀⠠⠄⢀⠄⠄
    ⠄⠄⠄⠄⠁⠄⠁⠄⠂⠄⡠⣲⢧⣳⡳⡯⣟⣼⢽⣺⣜⡵⣝⢜⢔⠔⡅⢂⠄⠄⠁⠄⢀⠄⡀⠄⡀⠄⠄⠄
    ⠄⠄⠄⠄⠈⠄⠈⠄⢀⡇⡯⡺⢵⣳⢿⣻⣟⣿⣿⣽⢾⣝⢮⡳⣣⢣⠣⡃⢅⠂⠐⠈⠄⠄⢀⠄⡀⠄⠄⠄
    ⠄⠄⠄⠄⠈⠄⠐⢀⠇⡪⡸⡸⣝⣾⣻⣯⣿⣿⡿⣟⣿⡽⣗⡯⣞⢜⢌⠢⡡⢈⠈⠄⠁⠈⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠐⠄⠈⠆⠕⢔⠡⣓⣕⢷⣻⣽⣝⢷⣻⣻⣝⢯⢿⠹⠸⡑⡅⠕⠠⠠⠄⠅⠄⠂⠄⠂⠈⠄⠄⠄
    ⠄⠄⠄⠄⠄⠂⠡⡑⢍⠌⡊⢢⢢⢱⠼⣺⢿⢝⠮⢪⣪⡺⣘⡜⣑⢤⢐⠅⠡⢂⠡⠐⡀⢀⠠⠐⠄⠐⠄⠄
    ⠄⠄⠄⠄⢈⢀⠡⠨⡢⡑⡌⡔⡮⡷⣭⢧⣳⠭⣪⣲⣼⣾⣟⣻⣽⣺⣸⣜⢌⢆⢌⠐⠄⡀⠄⡀⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠠⠄⠌⡢⡵⠺⠞⠟⠛⠯⠟⠟⠝⡫⢗⠟⠝⠙⠉⠊⠑⠉⠉⠉⠑⢒⠠⠁⠄⡀⠠⠄⠄⠄⠄
    ⠄⠄⠄⠐⡀⠄⠄⠅⡪⠄⠂⠄⠄⠄⠄⠄⠄⠄⢀⢕⢔⠄⠄⠄⠄⡀⠠⠐⠈⢀⠄⠠⠄⡁⠄⡀⠂⠠⠄⠄
    ⠄⠄⠄⠠⠄⠄⠂⡑⠄⠄⠠⠐⠄⠁⠄⠁⠄⠄⢸⣿⣿⡂⠄⠄⢀⠄⡀⠄⠂⠠⠐⠄⡐⡀⠂⢀⠐⠄⠄⠄
    ⠄⠄⠄⠄⢐⠄⠂⢕⢅⢄⠄⣀⡀⢄⠄⠁⣀⣔⡵⣿⣯⠧⡣⣢⡠⢀⢀⡠⠐⢀⢐⠠⢀⠐⠄⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠐⡔⢀⠘⢽⣻⣶⣥⣉⠥⡣⣱⣷⠻⣪⣻⣷⡣⡣⢫⣞⣗⡦⡵⢻⠺⡸⠐⡀⠐⠄⠂⡀⠄⠄⠄
    ⠄⠄⠄⠄⠂⠘⡀⠔⢀⠑⠍⠍⡽⣽⣿⣻⠂⡷⣯⡿⣟⡿⠌⡆⠘⣾⣻⢵⢕⠔⢀⠁⠠⠈⡀⠁⠄⡀⠄⠄
    ⠄⠄⠄⠄⠠⠄⠄⡐⢰⢈⢄⠱⢽⣺⢳⠁⣈⠄⠄⠈⠊⠈⠄⠄⢡⣐⢫⢯⡢⢊⢄⢪⠨⠠⠄⡀⠁⠄⠄⠄
    ⠄⠄⠄⠄⠂⠄⠂⠠⠱⣕⡣⡇⡏⢮⢕⣸⣾⠠⠄⠄⠄⠂⠄⠄⠌⢟⣜⡵⣯⢷⡴⡅⠅⡂⠠⠄⢈⠄⠄⠄
    ⠄⠄⠄⠄⠂⠁⢀⠈⠌⡪⢝⢾⣝⣎⠒⠏⠙⠠⠑⠁⠆⠒⠐⠐⠉⢀⠑⣍⡿⣽⡽⡂⠕⠄⠄⠂⢀⠠⠄⠄
    ⠄⠄⠄⠐⠄⡈⠄⢀⠄⠊⠍⢯⣷⣏⢊⢀⣈⣠⣤⣤⣤⣴⣶⢶⣴⢤⢬⣌⢻⡺⡻⠈⠄⠂⠄⠂⡀⠄⠄⠄
    ⠄⠄⠄⠄⠂⢀⠐⠄⠄⠂⠡⠑⠕⠅⡕⡽⡑⡁⠉⠉⠉⠉⠁⠁⠁⠠⢊⠊⠢⠈⠄⠨⠄⠄⠁⠐⢀⠈⠄⠄
    ⠄⠄⠄⠈⢀⠄⠄⠈⡀⢂⠐⠄⠂⠁⠠⠁⡢⡪⣢⣲⣦⣖⡔⡤⡨⡐⢄⠌⠠⠈⠐⠄⠂⠠⠁⢈⠠⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⢂⠄⠢⠂⠈⡀⠈⡀⠈⠰⠹⡨⠑⡑⠕⠕⠊⠌⠌⠄⠐⠄⠂⠁⢈⠄⡁⠐⠄⡐⢀⠂⠄
    ⠄⠄⠄⠄⡐⢄⠑⠄⠄⡇⡁⠄⠄⠄⠄⡈⠄⠄⠄⠄⢀⠠⠄⠂⢀⠐⠄⡈⠠⠈⠄⠄⠠⠐⠄⠁⠠⠄⠄⠄
    ⠄⠄⡀⢊⠨⢀⢊⠄⠨⡂⡂⠄⠂⠄⢀⠄⠠⠄⠂⠄⠄⡀⠠⠄⠄⠄⠐⠄⠄⡀⠁⡀⠂⠄⠂⠁⠨⠄⠅⠄
    ⠄⠄⠐⠄⢂⠢⡀⠄⠬⠄⠂⠅⡀⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠂⠄⠂⠄⢀⠄⠄⠄⠄⠂⠄⠂⢈⠐⠄⠄
    ⠄⠄⠈⡀⠄⠄⠄⠄⠅⠅⠐⠄⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⠂⢐⠄⠐⠄
    ⠄⠄⠄⠄⠄⠂⠄⠄⠕⠈⡂⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠄⠄⠂⠄""")
