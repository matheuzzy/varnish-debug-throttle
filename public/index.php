<?php

$delay = 0;

if (isset($_GET['delay'])) {
	$delay = intval($_GET['delay']);
}else {
   usleep(500);
}

sleep($delay);

echo "Hello after $delay seconds";
