import smtplib

from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = "587"
login = "gabrieldevtestes@gmail.com"
senha = "123!!456"

server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()
server.login(login, senha)


corpo = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

body{
    font-family: Roboto;
    background-color: rgb(241, 241, 241);
}
h1{
    font-size: 60px;
    text-transform: uppercase;
    text-align: center;
}
 p{
    font-size: 25px;
}
table{
    width: 80%;
    margin: auto;
    box-shadow: 10px 10px 18px rgb(194, 194, 194);
    border-collapse: collapse;
    text-align: center;  
    background-color: white; 
   
    
}
thead{
    line-height: 50px;
    font-size: 25px;
    box-shadow: 0 5px 8px rgb(163, 163, 163);
    background-color: #35CE8D;
    color: white;
    
}
tbody tr{
    line-height: 50px;
}
tbody tr:nth-child(even){
    background-color: rgb(228, 228, 228);
}
 </style>
 
 <body>    
        <h1>Novos Leilões</h1>        
        <p style="font-size: 25px" >Clientes interessados: Gabriel, Guilherme</p>
        <p style="font-size: 25px" >Novos <strong>(5)</strong> leilões foram encontrados:</p>        
        
            <table style="text-align: center;background-color: white;">
                <thead>
                    <tr>
                        <th>Site</th>
                        <th>Categoria</th>
                        <th>Preço</th>
                        <th>Link</th>
                    </tr>
                </thead style="line-height: 50px;font-size: 25px;background-color: #35CE8D;color: white;">
                <tbody>
                    <tr style= "line-height: 50px">                        
                        <td> {n[0]} </td>
                        <td> {n[1]} </td>
                        <td> {n[2]} </td>
                        <td> {n[3]} </td>  
                    </tr>
                    <tr>                        
                        <td> {n[0]} </td>
                        <td> {n[1]} </td>
                        <td> {n[2]} </td>
                        <td> {n[3]} </td>  
                    </tr>
                    <tr>                        
                        <td> {n[0]} </td>
                        <td> {n[1]} </td>
                        <td> {n[2]} </td>
                        <td> {n[3]} </td>  
                    </tr>
                    <tr>                 
                </tbody>
            </table>        
</body>

"""

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = 'gabrielpimenttas@gmail.com'
email_msg['Subject'] = 'email automatico'
email_msg.attach(MIMEText(corpo, 'html'))

server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()
print('email enviado')