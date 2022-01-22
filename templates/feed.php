<?php
if(isset($_POST['submit'])){
    $to = "jedan2506@gmail.com";



    $name = $_POST['name'];
    $email= $_POST['email'];
    $country= $_POST['country'];
    $sub=$_POST['subject'];
    $headers = 'From: '.$email . "\r\n";


    $body = "name : ".$name. "\r\n" .
    		"Message : " . $body;

    if(mail($to,$subject,$body,$headers))
    {
        echo "Mail Sent!";
    }
    else
    {
         echo "Failed To Send Mail";
    }
}

?>