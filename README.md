# inicializador-biletov1

- Desenvolvedor – Sergio P. C. Junior

- Linguagem: Python  


Função: 
O inicializador Bileto tem a função de automatizar o processo de inicialização do sistema de venda de ingressos Bileto (Box Office), tornado mais prático e visual para as Bilheterias. Além disso, ele lê e dar devolutivas referentes as logs de impressora que está configurada no sistema, facilita o acesso a central de ajuda e ao chat do suporte.


# Tópico (1) Erro da Impressora: 
A Bileto (Box Office), utiliza para impressão em sua maior parte a impressora Térmica Daruma (Dr-700/800), antes de iniciar o sistema carrega o Daruma Framework, configura Daruma port e por fim verifica se a daruma está conectada na máquina. Todos esses processos são registrados e visíveis através da leitura da log System (c:\bileto\logs\System.log), e caso a bilheteria ligue a impressora depois do sistema ter iniciado, ele não realiza a impressão. 

Solução: 
Através da leitura da log System, o inicializador verifica se a impressora foi encontrada procurando o registro “Daruma successfully detected” no arquivo. Caso não encontre informa ao usuário as possíveis causas e indica clicar em “Reiniciar” para uma nova busca. 
Ao encontrar o inicializador informa que o login pode ser realizado. 

# Tópico (2) Preferência de impressão: 
A Daruma está disponível, porém não foi selecionada dentro do sistema como impressora para impressão de ingresso. 

Solução: 
Além de verificar a disponibilidade da impressora (tópico 1), o sistema ler o arquivo “printer-configuration” (C:\bileto\conf\ printer-configuration, procurando a chave "ticketPrinterName" que registra a impressora configurada como preferência de impressão. Quando identificado o link “central de Ajuda” altera para o Artigo que mostra como realizar essa alteração. 

# Tópico (3) Barra de carregamento: 
As verificações e configuração de impressora e sitef realizados enquanto o sistema inicia pode levar em torno de 3 a 5 minutos e a única forma de saber se o sistema está pronto para o login é através da log System, quando ela atinge 5KB o sistema está pronto. 
* O Windows arredonda, mas o valor correto é 4898 bytes. 

Solução: 
O Inicializador tem uma solução gráfica, apresentando uma barra de carregamento que mostra quando o sistema está pronto para login. 
Internamente o sistema ao iniciar fica verificando a quantidade de bytes do arquivo alimentando a barra conforme o progresso.



Tópico (4) Acesso ao Suporte: 
O acesso ao suporte hoje é feito através do navegador ou atalho configurado na área de trabalho.

Solução:
O Inicializador tem um botão que leva direto ao chat, e no link “Central de Ajuda” é disponibilizado um artigo referente ao horário do suporte. 


