arg=$*
screenName=dst_server1 #The screen name of your server
screen -r $screenName -p 0 -X stuff "c_announce(\"""$arg""\")""$(echo -ne '\015')"
