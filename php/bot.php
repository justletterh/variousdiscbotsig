<?php
#imports the included modified yasmin lib
include __DIR__.'/vendor/autoload.php';

#creates the bot obj
$loop = \React\EventLoop\Factory::create();
$client = new \CharlotteDunois\Yasmin\Client(array(), $loop);

#the ready event sets the bot's status and prints in the console once it logs in
$client->on('ready', function () use ($client) {
    echo 'Logged in as '.$client->user->tag.PHP_EOL;
    $client->user->setPresence(
    array(
        'since' => null,
        'game' => array(
            'name' => '',
            'type' => 0,
            'url' => null
        ),
        'status' => 'idle',
        'afk' => false
    )
);
});

#the on message event tells the bot to respond to messages
$client->on('message', function ($message) use ($client) {
if ($message->content === "ping--"){
  $message->channel->send('im shitty bc i kill myself as soon as i see exit() and i have no embeds or built in latency function, my authors cant be bothered to make their own bc php is stupid in general, have a nice day! ***-php***');
}
if ($message->content === "chat--yes"){
  $message->channel->send('no');
}
if ($message->content === "chat--no"){
  $message->channel->send('yes');
}
if ($message->content === "chat--how are you"){
  $message->channel->send('stfu');
}
if ($message->content === "chat--stfu"){
  $message->channel->send('ok');
}
if ($message->content === "chat--no u"){
  $message->channel->send('reverse uno card for you too');
}
if ($message->content === "chat--are you ok"){
  $message->channel->send('no');
}
if ($message->content === "stopphp--"){
  $message->channel->send('i want to kill me too')->then(function($new_message) use ($client){
    $client ->destroy();
  });
}
if ($message->content === "kys--"){
  $message->channel->send('Bye! ***-php***')->then(function($new_message) use ($client){
    $client ->destroy();
  });
}
});

#logs in the bot
$client->login('BOT-TOKEN-HERE');
$loop->run();
