<div>
  <h1>Repositorio Criado para gerenciar melhor os arquivos do servidor dedicado do dont starve.</h1>
  </div>
 <div>
Utilizando o sistema ubuntu-20 lts.
  <br>
*reinicio automatico
  <br>
*envio de mensagem de status
  <br>
*envio de mensagem dentro do jogo Globalmente
  <br>
*auto update de Mods.
</div>
<div>
  <h1>Arquivos</h1>
  <ul type="circle"></ul>
  <li><b>server_announce</b> <br>
  este arquivo é responsavel por mandar um anuncio Global no servidor
  <br>
  <li><b>join_server_announcement </b><br>
  ele é responsavel por fazer um anuncio de boas vindas para cada jogar que entrar no servidor
  <br>
  <li><b>MonitorProcessDont</b><br>
  Monitora o processo do servidor e o reinicia caso caia.
  <br>
  <li><b>run_dedicated_servers </b><br>
  Esse é meu arquivo de inicialização do servidor, caso queira.
  <br>
  <li> <b>WebhookDont</b><br>
  manda uma mensagem no seu servidor discord, configure seu tokem e Url.
</div>
<div>
<h1> contrab exemplo</h1>

<b>Deve ser dado permissão para executar o script.</b><br>
chmod +x /home/user/MonitorProcessDont.sh<br>
<b>Coloque no crontab:<br></b>
 */5 * * * * /home/user/MonitorProcessDont.sh<br>
 <b>Se quiser editar o arquivo do usuario atual da crontab. Pode ser permissão tbm.<br></b>
crontab -e<br>
<b>Execute o comando: <br></b>
crontab /etc/crontab<br>
<b>Reiniciei o cron<br></b>
/etc/init.d/cron restart
</div>