#!/bin/bash

export dont="dont"

teste=`ps -ef| grep dedicated_serve | grep Master | awk '{print $1}'`

if  [ "$teste" == "$dont" ]
then
  echo $(date +'%m/%d/%Y %T')  "SERVICO NO AR" > /tmp/monitorarunserver.log
  pgrep -f WebhookDont.py | xargs kill -9
else
   /usr/bin/python3 ~/WebhookDont.py &
   screen -dmS dst_server1 "/home/dont/run_dedicated_servers.sh"
   screen -dmS join_server "/home/dont/join_server_announcement.sh"
   echo $(date +'%m/%d/%Y %T')  "SERVICO REINICIADO" >> /tmp/restartrunserver.l$
fi
