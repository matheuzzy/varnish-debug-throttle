<?php

$delay = 0;

if (isset($_GET['delay'])) {
	$delay = intval($_GET['delay']);
}

sleep($delay);

echo "Hello after $delay seconds";
