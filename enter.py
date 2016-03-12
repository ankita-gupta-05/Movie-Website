import media
import fresh_tomatoes

movie1=media.Movie("Game of Thrones","War for thrones.. Saga of Ice and Fire",
                   "https://wallpaperscraft.com/image/game_of_thrones_daenerys_targaryen_emilia_clarke_jorah_mormont_iain_glen_dragons_94900_602x339.jpg",
                   "https://youtu.be/CuH3tJPiP-U")

movie2=media.Movie("Divergent","World of Fractions",
"http://t1.gstatic.com/images?q=tbn:ANd9GcT-2Rh2ekmgcEts-N5knGpiNDNJV9ZFLWyMNLQfKAlrIcf2EkDL",
"https://youtu.be/sutgWjz10sM")
                   
movie3=media.Movie("Friends","6 Guys hangiong out in Cafe",
"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSSuEGNSaqgXwkEncjt-zqt-cKhqyGne9j1wfhwYyy1foBhFtLT_g",
"https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=video&cd=2&cad=rja&uact=8&sqi=2&ved=0ahUKEwjM_oybn7bLAhWGKaYKHeOYDcMQtwIIHjAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DFLzfXQSPBOg&usg=AFQjCNHg67KsaHyHJxrXK1s4X5pm4MU9OQ&sig2=IKCfJKFVAPaqnEiPqbGCPQ&bvm=bv.116573086,d.dGY")

movie4=media.Movie("Gravity","Travel out in space",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpJMKyU9gsCAaCjoaz83yy_-I1jWB7n6xiJo8GY5jrIi_4nz_IWA",
"https://youtu.be/OiTiKOy59o4")

movie5=media.Movie("Sex and the City","Life of 4 girls around Love",    
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6jo0S7xa6Dvr2vH7u45z3c84T3-Xfln7BB15mLW0erIQ_1fo-hA",
"https://youtu.be/y6U8o9Ed0VI")

movie6=media.Movie("Lucy","an extraordinary story of an ordinary woman",               
"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSGWM7DX54s17Jy6_EXU4pb495TM825c6TDGHh9gu7iiJ2SGDwphw",
"https://youtu.be/RnKVv8Lp_xU")

movies=[movie1,movie2,movie3,movie4,movie5,movie6]
fresh_tomatoes.open_movies_page(movies)
