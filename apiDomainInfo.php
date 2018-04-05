<?php
require_once 'XML/RPC2/Client.php';

$domain_api = XML_RPC2_Client::create(
    'https://rpc.ote.gandi.net/xmlrpc/',
    array( 'prefix' => 'domain.', 'sslverify' => False  )
);

$apikey = '<MY OTE API KEY>';

$domain_name = "joutytest03.com";

$result = $domain_api->info($apikey, $domain_name);
print_r($result);
?>
