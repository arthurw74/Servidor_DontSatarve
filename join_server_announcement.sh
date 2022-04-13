while true
do
grep -m 1 "Join Announcement" <(tail -n 0 -F /home/dont/.klei/DoNotStarveTogether/MyDediServer/Master/server_chat_log.txt)\
&& sleep 15 && /home/dont/server_announce.sh Seja bem vindo! #Link it to the announce_server script.
done
