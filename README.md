# inicializador-biletov1

- Desenvolvedor � Sergio P. C. Junior

- Linguagem: Python  


Fun��o: 
O inicializador Bileto tem a fun��o de automatizar o processo de inicializa��o do sistema de venda de ingressos Bileto (Box Office), tornado mais pr�tico e visual para as Bilheterias. Al�m disso, ele l� e dar devolutivas referentes as logs de impressora que est� configurada no sistema, facilita o acesso a central de ajuda e ao chat do suporte.


# T�pico (1) Erro da Impressora: 
A Bileto (Box Office), utiliza para impress�o em sua maior parte a impressora T�rmica Daruma (Dr-700/800), antes de iniciar o sistema carrega o Daruma Framework, configura Daruma port e por fim verifica se a daruma est� conectada na m�quina. Todos esses processos s�o registrados e vis�veis atrav�s da leitura da log System (c:\bileto\logs\System.log), e caso a bilheteria ligue a impressora depois do sistema ter iniciado, ele n�o realiza a impress�o. 

Solu��o: 
Atrav�s da leitura da log System, o inicializador verifica se a impressora foi encontrada procurando o registro �Daruma successfully detected� no arquivo. Caso n�o encontre informa ao usu�rio as poss�veis causas e indica clicar em �Reiniciar� para uma nova busca. 
Ao encontrar o inicializador informa que o login pode ser realizado. 

# T�pico (2) Prefer�ncia de impress�o: 
A Daruma est� dispon�vel, por�m n�o foi selecionada dentro do sistema como impressora para impress�o de ingresso. 

Solu��o: 
Al�m de verificar a disponibilidade da impressora (t�pico 1), o sistema ler o arquivo �printer-configuration� (C:\bileto\conf\ printer-configuration, procurando a chave "ticketPrinterName" que registra a impressora configurada como prefer�ncia de impress�o. Quando identificado o link �central de Ajuda� altera para o Artigo que mostra como realizar essa altera��o. 

# T�pico (3) Barra de carregamento: 
As verifica��es e configura��o de impressora e sitef realizados enquanto o sistema inicia pode levar em torno de 3 a 5 minutos e a �nica forma de saber se o sistema est� pronto para o login � atrav�s da log System, quando ela atinge 5KB o sistema est� pronto. 
* O Windows arredonda, mas o valor correto � 4898 bytes. 

Solu��o: 
O Inicializador tem uma solu��o gr�fica, apresentando uma barra de carregamento que mostra quando o sistema est� pronto para login. 
Internamente o sistema ao iniciar fica verificando a quantidade de bytes do arquivo alimentando a barra conforme o progresso.



T�pico (4) Acesso ao Suporte: 
O acesso ao suporte hoje � feito atrav�s do navegador ou atalho configurado na �rea de trabalho.

Solu��o:
O Inicializador tem um bot�o que leva direto ao chat, e no link �Central de Ajuda� � disponibilizado um artigo referente ao hor�rio do suporte. 


